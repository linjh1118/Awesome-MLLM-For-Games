from concurrent.futures import ThreadPoolExecutor
import time
import arxiv
import argparse
import re
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path as p
import pandas as pd
import arxiv
import fitz  # PyMuPDF
import os
from fuzzywuzzy import fuzz
def set_proxies():
    os.environ['http_proxy'] = 'http://10.93.0.6:8899'
    os.environ['https_proxy'] = 'http://10.93.0.6:8899'
PDF_SAVE_DIR = 'tools/arxiv_tools/asset/pdf/'

set_proxies()


def show_md(markdown_content: str):
    console = Console()
    md = Markdown(markdown_content)
    console.print(md)
    
def get_arxiv_result_from_paper_titles(paper_title):
    """
    Get the arXiv URL for a given title.
    """
    # if isinstance(paper_title, list):
    #     return [get_arxiv_result_from_paper_titles(t) for t in paper_title if t is not None]
    if isinstance(paper_title, list):
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(
                lambda t: get_arxiv_result_from_paper_titles(t) if t is not None else None,
                paper_title
            ))
        return [result for result in results if result is not None]
    
    tidy_title = paper_title
    if ':' in paper_title:
        tidy_title = paper_title.split(':')[1].strip()
    tidy_title = ' '.join(tidy_title.split()) # 将多余空格删除
    client = arxiv.Client()
    
    search = arxiv.Search(query = f'ti:{tidy_title}', max_results=20)
    try:
        results = list(client.results(search))
        if not results:
            raise Exception("No results found")
        best_match = max(results, key=lambda result: fuzz.ratio(paper_title.lower(), result.title.lower()))
        first_result = best_match
    except Exception as e:
        print(f"- Error: {e} for title: {paper_title}")
        return None
    print(f"\ntarget title: >>{paper_title}<<\nsearch title: >>{first_result.title}<<\n")
    return first_result
    
def get_search_result(terms = ['VLM', 'Games'], n_papers = 5) -> str:
    client = arxiv.Client()
    query_string = " AND ".join([f'ti:"{term}"' for term in terms])
    
    # abs
    query_string_abs = " AND ".join([f'abs:"{term}"' for term in terms])
    
    # final query
    query_string = f"({query_string}) OR ({query_string_abs})"
    
    search = arxiv.Search(
        query = query_string, 
        max_results = n_papers,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    arxiv_results = list(client.results(search))  # you can get something by [x.title for x in results]
    arxiv_results = [x for x in arxiv_results if x is not None]
    return arxiv_results

def save_arxiv_search_results(arxiv_results, output_file):
    """
    Save the arXiv search results to a jsonl file.
    
    Args:
    - arxiv_results: List of arXiv paper results.
    - filename: The name of the CSV file to save the results to.
    """
    
    
    data_list = []
    
    for result in arxiv_results:
        try:
            each_data = dict(
                title = result.title,
                authors = ', '.join([str(author) for author in result.authors]),
                summary = result.summary,
                url = result.entry_id,
                pdf_url = result.pdf_url,
                published = result.published,
                comment = result.comment,
            )
        except Exception as e:
            print(f"Error: {e} when processing {result.title}")
            continue
        data_list.append(each_data)
        pdf_save_dir = PDF_SAVE_DIR
        
        pdf_path = f"{pdf_save_dir}/{result.title}.pdf"
        
        if not os.path.exists(pdf_path):
            for i in range(2):
                try:
                    result.download_pdf(filename=pdf_path)
                    break
                except Exception as e:
                    print(f"Error: {e} when downloading {result.title}.pdf")
                    # sleep
                    time.sleep(1)
                
        
        if os.path.exists(pdf_path):
            # parse pdf content
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            each_data['pdf_text'] = text
            each_data['pdf_path'] = pdf_path
        else:
            each_data['pdf_text'] = ""
            each_data['pdf_path'] = ""
        
        print(f"Saved {result.title} to {pdf_path}")
    
    df = pd.DataFrame(data_list)
    assert str(output_file).endswith('.jsonl')
    df.to_json(output_file, orient='records', lines=True, force_ascii=False)


def get_args():
    parser = argparse.ArgumentParser(description="Get the arXiv URL for a file which each line is a title.")
    # parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='./tools/arxiv_tools/asset/update_0319/terms_0319.md')
    # parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='./tools/arxiv_tools/asset/update_0319/terms_merge.md')
    # parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='./tools/arxiv_tools/asset/update_0319/terms_game_generative.md')
    parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='tools/arxiv_tools/asset/update_0323/terms_game_bench.md')
    parser.add_argument("--n_papers", type=int, help="The number of papers to get for each search term.", default=100)
    parser.add_argument("--do_from_list", action='store_true', help="Whether to get the search results from a list of terms.", default=False)
    args = parser.parse_args()
    for k, v in vars(args).items():
        print(f">>> {k}: {v}")
    return args


def main():
    # >>> 1. args
    args = get_args()
    output_file = p(args.input_file).with_stem('source_' + p(args.input_file).stem.split('_', maxsplit=1)[1]
                                               ).with_suffix('.jsonl')
    if output_file.exists():
        print(f"Output file {output_file} exists. Skip.")
        return
    if not args.do_from_list:
        # >>> 2. read the input file
        lines = p(args.input_file).read_text().strip().split('\n')
        terms_list = [l.strip().split() for l in lines]
        # >>> 3. get the arxiv paper content
        for terms in terms_list:
            search_results = get_search_result(terms, n_papers=args.n_papers) 
            save_arxiv_search_results(search_results, output_file)
    else:
        paper_list = p(args.input_file).read_text().strip().split('\n')
        search_results = get_arxiv_result_from_paper_titles(paper_list)
        save_arxiv_search_results(search_results, output_file)
        
        
        
if __name__ == '__main__':
    main()
    
    
    


    
