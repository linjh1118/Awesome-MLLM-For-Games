import arxiv
import argparse
import re
import pandas as pd
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path as p



def show_md(markdown_table_content: str):
    console = Console()
    md = Markdown(markdown_table_content)
    console.print(md)
    
    
def make_survey_markdown(input_df, output_file, do_show_md=True):
    original_term_file = output_file.with_stem(output_file.stem.replace('final_survey_', 'terms_'))
    terms = p(original_term_file).read_text().strip().split()
    
    # two content， one for table of content, one for tldr
    table_content = '# Paper List of Terms(' + '+'.join(terms) + ')\n'
    tldr_content = '# TLDR/Notes\n'
    
    for a_paper in input_df:
        # >>>>>> prepare info 
        # >>> title
        title = a_paper['title']
        # >>> month and year
        url = a_paper['url']
        pattern = r"abs/(\d{4})\."
        match = re.search(pattern, url)
        if match:
            number = match.group(1)
        else:
            number = "2500"
        year_month_str = f"{number[:2]}/{number[2:]}"
        # >>> project page
        page_url = re.findall(r'https?://[^\s]+', a_paper['summary'])
        code_or_page = page_url[0] if page_url else ""
        
        
        # >>>>>> inject output markdown
        # >>> table content
        no_biaodian_title = re.sub(r'[,:.?"\']', ' ', title).replace(' ', '-').lower()
        markdown_table_content = """- [{year_month_str}] **{title}**  
[[Paper]({paper_url})] [[Code/Page]({code_or_page})] [[TLDR/Notes]({link_2_node})]""".format(
    year_month_str=year_month_str, title=title, paper_url=a_paper['pdf_url'], code_or_page=code_or_page,
    link_2_node=f"#{no_biaodian_title}"
    )
        print(markdown_table_content)
        table_content += markdown_table_content + '\n\n'
        
        # >>>>>> tldr cont
        cur_paper_tldr = ''
        cur_paper_tldr += f"## {no_biaodian_title}\n"
        cur_paper_tldr += f"### Abstract\n{a_paper['summary']}\n"
        cur_paper_tldr += a_paper['llm_summary_res'].replace('##', '###')
        tldr_content += cur_paper_tldr + '\n\n'
        
    to_file_content = table_content + '\n\n' + tldr_content
    
        
    if do_show_md:
        show_md(to_file_content)
    p(output_file).write_text(to_file_content, encoding='utf-8')
    print(f"Saved the markdown content to {output_file}")


def get_args():
    parser = argparse.ArgumentParser(description="Get the arXiv URL for a file which each line is a title.")
    parser.add_argument("--input_file", type=str, help="The file containing the titles.", default='./tools/arxiv_tools/asset/update_0323/game_vlm/tldr_game_vlm.jsonl')
    args = parser.parse_args()
    args.output_file = p(args.input_file).with_stem(p(args.input_file).stem.replace('tldr_', 'final_survey_')).with_suffix('.md')
    for k, v in vars(args).items():
        print(f">>> {k}: {v}")
    return args

def main():
    args = get_args()
    input_df = pd.read_json(args.input_file, lines=True).to_dict(orient='records')
    make_survey_markdown(input_df, args.output_file)
            
if __name__ == "__main__":
    main()
        


    
