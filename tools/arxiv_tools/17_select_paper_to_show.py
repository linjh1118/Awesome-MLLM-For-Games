from copy import deepcopy
import functools
from io import BytesIO
import io
import signal
import sys
sys.path.append('/workspace/linjh/CoT_Factory/src'); from common_start import *
import time
import requests
from to_html import show_html




input_file = 'tools/arxiv_tools/asset/update_0323/select_paper/paper_bench.md'

lines = p(input_file).read_text().split("\n")
target_papers = []
for l in lines:
    target_papers.append(l.strip())
    
all_paper_file = '/workspace/linjh/github/learn/Awesome-MLLM-For-Games/tools/arxiv_tools/asset/update_0323/all_paper.jsonl'
input_df = pd.read_json(all_paper_file, lines=True)
input_data = input_df.to_dict(orient='records')

# 计算input_df的title列和target_papers的交集
title_set = set(input_df['title'].values)
intersect_set = title_set.intersection(set(target_papers))
print(f"intersect_set: {intersect_set}, len: {len(intersect_set)}")

selected_df = input_df[input_df['title'].isin(set(intersect_set))]
# sort by order in target_papers: selected_df['title'].apply(lambda x: target_papers.index(x))
selected_df['order'] = selected_df['title'].apply(lambda x: target_papers.index(x))
selected_df = selected_df.sort_values('order')
# 标题列去重
selected_df = selected_df.drop_duplicates('title')


df = selected_df
print(f'df columns: {df.columns}')
# df.drop(columns=['image_path'], inplace=True)
INPUT_COLS = ['title', 'summary']
RES_COL = 'llm_summary_res'
MORE_COLS = []
df = df[ INPUT_COLS + [RES_COL] + MORE_COLS ]
openitem_to_html(
    df,
    output_html_path=p(input_file).with_suffix('.html'),
    textual_cols = INPUT_COLS + [RES_COL] + MORE_COLS,
)