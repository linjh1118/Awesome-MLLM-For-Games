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

import os

def set_proxies():
    os.environ['http_proxy'] = 'http://10.93.0.6:8899'
    os.environ['https_proxy'] = 'http://10.93.0.6:8899'

set_proxies()

def show_md(markdown_content: str):
    console = Console()
    md = Markdown(markdown_content)
    console.print(md)

from fuzzywuzzy import fuzz
    
def get_arxiv_url(title = "ING-VP: MLLMs cannot Play Easy Vision-based Games Yet", output_file=None, do_show_md=False) -> str:
    """
    Get the arXiv URL for a given title.
    """
    if isinstance(title, list):
        return [get_arxiv_url(t) for t in title]
    tidy_title = title
    if ':' in title:
        tidy_title = title.split(':')[1].strip()
    # 将多余空格删除
    tidy_title = ' '.join(tidy_title.split())
    client = arxiv.Client()
    search = arxiv.Search(query = f'ti:{tidy_title}', max_results=10)
    
    try:
        results = list(client.results(search))
        if not results:
            raise Exception("No results found")
        best_match = max(results, key=lambda result: fuzz.ratio(tidy_title.lower(), result.title.lower()))
        
        first_result = best_match
    except Exception as e:
        content = f"- Error: {e} for title: {title}"
        print(content)
        if output_file:
            print(content, file=output_file)
        return content

    print(f"target title: >>{title}<<\nsearch title: >>{first_result.title}<<")
    year_month_str = f'{first_result.updated.year}/{str(first_result.updated.month).zfill(2)}'
    urls = re.findall(r'https?://[^\s]+', first_result.summary)
    code_or_page = urls[0] if urls else ""

    markdown_content = """- [{year_month_str}] **{title}**  
[Paper]({paper_url}) [Code/Page]({code_or_page})""".format(year_month_str=year_month_str, title=title, paper_url=first_result.pdf_url, code_or_page=code_or_page)
    print(markdown_content)
    if output_file:
        print(markdown_content, file=output_file)
    
    if do_show_md:
        show_md(markdown_content.replace('\n', '\n\n'))
    

def get_args():
    parser = argparse.ArgumentParser(description="Get the arXiv URL for a file which each line is a title.")
    # parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='./asset/paper_0319.txt')
    parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='tools/arxiv_tools/asset/update_0319/gm_paper.txt')
    return parser.parse_args()


def main():
    args = get_args()
    with open(args.input_file, "r") as f:
        titles = f.readlines()
    titles = [t.strip() for t in titles]
    output_file = p(args.input_file).with_stem(p(args.input_file).stem + "_url")
    urls = get_arxiv_url(titles, output_file)
    
        
if __name__ == "__main__":
    main()
    
# python get_arxiv_url.py --input_file ./asset/paper_0319.txt
    


    
