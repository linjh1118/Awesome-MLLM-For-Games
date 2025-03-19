import arxiv
import argparse
import re
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path as p
import sys
# sys.path.append(str(p(__file__).parent))
# 切换到当前文件所在目录


def show_md(markdown_content: str):
    console = Console()
    md = Markdown(markdown_content)
    console.print(md)
    
    
def get_arxiv_url(terms = ['VLM', 'Games'], output_file=None, do_show_md=False, n_papers = 2) -> str:
    """
    Get the arXiv URL for a given title.
    """
    to_file_content = '### ' + '+'.join(terms) + '\n---\n'
    print(to_file_content)
    client = arxiv.Client()
    
    query_string = " AND ".join([f'ti:"{term}"' for term in terms])
    # query_string = 'ti:' + ' '.join(terms[:-1])
    search = arxiv.Search(
        query = query_string, 
        max_results = 100,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    
    results = client.results(search) # print(len(list(results)))
    for a_paper in results:
        title = a_paper.title
        year_month_str = f'{a_paper.updated.year}/{str(a_paper.updated.month).zfill(2)}'
        urls = re.findall(r'https?://[^\s]+', a_paper.summary)
        code_or_page = urls[0] if urls else ""

        markdown_content = """- [{year_month_str}] **{title}**  
[[Paper]({paper_url})] [[Code/Page]({code_or_page})]""".format(year_month_str=year_month_str, title=title, paper_url=a_paper.pdf_url, code_or_page=code_or_page)
        print(markdown_content)
        to_file_content += markdown_content + '\n\n'
    
    if do_show_md:
        show_md(to_file_content)
    output_file.write_text(to_file_content)


def get_args():
    parser = argparse.ArgumentParser(description="Get the arXiv URL for a file which each line is a title.")
    # parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='./tools/arxiv_tools/asset/terms_0319.md')
    # parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='./tools/arxiv_tools/asset/terms_merge.md')
    parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='./tools/arxiv_tools/asset/terms_game_bench.md')
    return parser.parse_args()


def main():
    args = get_args()
    with open(args.input_file, "r") as f:
        lines = f.readlines()
    lines = [t.strip() for t in lines]
    output_file = p(args.input_file).with_stem(p(args.input_file).stem + "_url")
    for l in lines:
        terms = l.split()
        urls = get_arxiv_url(terms, output_file)
    
        
if __name__ == "__main__":
    main()
    
# python get_arxiv_url.py --input_file ./asset/paper_0319.txt
    


    
