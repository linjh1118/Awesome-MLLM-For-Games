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



# ==============================================================================
# Aim: 调用api
# ==============================================================================
args = nlp.Args.get_args(
        # sample_size=-1, max_workers=1,
        # sample_size=32, max_workers=16,
        # sample_size=32, max_workers=8,
        # sample_size=-1, max_workers=16,
        sample_size=-1, max_workers=32,
        # ==============================================================================
        # >>>>> rollout model （ 需要组合工作流，参考：/workspace/linjh/CoT_Factory/exps/1212_long_cot/code/0219_gen_and_optim_r1/3_gen_32b/both_verify/0_gen_and_verify_on_perfect_cap.py）
        # model_name='claude-3-5-sonnet-20241022',
        # model_name='vllm-qwen',
        # model_name='gpt-4o-2024-11-20',
        # model_name='gpt-4o-mini-2024-07-18',
        model_name='glm-4-air',
        # ==============================================================================
        input_file='/workspace/linjh/github/learn/Awesome-MLLM-For-Games/tools/arxiv_tools/asset/update_0323/source_game_bench.jsonl',
        output_file='/workspace/linjh/github/learn/Awesome-MLLM-For-Games/tools/arxiv_tools/asset/update_0323/tldr_source_game_bench.jsonl',
        # output_file='/workspace/linjh/CoT_Factory/exps/1212_long_cot/code/0306_rewrite_search_format/output/cap@simple@r1_qw32b_mathvl_train_0218.jsonl',
        output_suffix='.jsonl',
        do_show_html=True
)                                                                                                      
textual_model = ['glm-4-public', 'gpt-4', 'gpt35-turbo-16k', 'glm-4-air', 'gpt-4o-mini-2024-07-18', 'glm-zero-preview', 'local-R1-32b', 'claude-3-5-sonnet-20241022']  # 如果不是文本模型，则process_one请求时，会要求从item中抽取图片

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>> prepare data: read / (sample) / filter /resume  <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 1. Read:  for tar format, can't just pd.read_json(), so we need to use get_orig_sample

if args.input_file != 'input_file':
    # from a file
    meta_jsonl_data = get_orig_sample(args.input_file, show_change=False, do_not_care_img=args.model_name in textual_model)
else:
    # from a dir. But you can do --input_dir INPUT_FILE_OR_DIR, which is more convenient for shell
    meta_jsonl_data = get_meta_jsonl_data(input_file_or_dir=args.input_dir, sample_size=args.sample_size)  
    
# 1.5 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻 set anything here 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻
# 1.5 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻 set anything here 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻
# 1.5 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻 set anything here 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻
# 1.5 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻 set anything here 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻
# >>>> set input
response_template = """### 任务
你是一个人工智能领域的专家，你能够快速阅读arxiv上的各种AI前沿论文，并给出非常好的论文总结。
现在请你阅读以下论文，并给出你对这篇论文的详细介绍，从而放到你的博客上，让更多人了解这篇论文。

### 论文信息
###  1. 论文标题
```
{title}
```
#### 2. 论文摘要
```
{summary}
```

#### 3. 论文全文
```
{pdf_text}
```

请输出论文总结
### 输出格式（输出语言用中文）
```
## 🌟 论文解读 | <想一个，宣传该论文的文案标题>

## 📌 背景痛点/本文动机
...(介绍论文的背景或痛点，或者本文的动机)

## 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
...

💡 创新点2
...

## 📈 实验结果
...

## 💬 可借鉴之处
...(介绍论文的可借鉴之处)


.....
```
"""



for item in meta_jsonl_data:    
    # 1. 准备query_prompt
    
    pdf_text = item['pdf_text'].split('\nReferences\n')
    item['pdf_text'] = pdf_text[0]
    item['query_prompt'] = response_template.format(**item)
    

# INPUT_COLS = ['query_prompt']
INPUT_COLS = ['title', 'summary']

# >>> set output (在process_one中，检查如果已经有boxed，则直接生成RES_COL，调用do_more_parse，否则调用LLM，生成RES_COL，再调用do_more_parse)
# def do_more_parse(item):
#     llm_summmary_res = item[RES_COL]
#     thinking_process = re.search(r'<think>(.*?)</think>', item['generated_answer'], re.DOTALL).group(0)
#     item['long_cot_with_boxed'] = f'{thinking_process}\n<answer>\n{add_boxed_answer}\n</answer>'
do_more_parse = None

RES_COL = 'llm_summary_res'
MORE_COLS = []


# 1.5 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻 set anything here 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻
# 1.5 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻 set anything here 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻
# 1.5 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻 set anything here 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻
# 1.5 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻 set anything here 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻

# 2. sample for tagger, or for debugging
if args.is_debug or 0 < args.sample_size < len(meta_jsonl_data):
    print(f'Do sampling with sample_size={args.sample_size}')
    random.seed(88)
    meta_jsonl_data = random.sample(meta_jsonl_data, min(args.sample_size, len(meta_jsonl_data)))

# 3. filter
# def is_perfect_caption(item):
#     return item['succ_reach_by_caption']
# print(f'Before filter flaw caption: {len(meta_jsonl_data)}')
# meta_jsonl_data = [x for x in meta_jsonl_data if is_perfect_caption(x)]; print(f'After filter flaw caption: {len(meta_jsonl_data)}')

# print('Before filter </think> ', len(meta_jsonl_data))
# meta_jsonl_data = [x for x in meta_jsonl_data if re.search(r'<think>(.*?)</think>', x['generated_answer'], re.DOTALL)]
# print('After filter </think> ', len(meta_jsonl_data))

# 4. resume
# RES_COL = 'subject_judge'
do_resume = (args.sample_size == -1)
res_status_col, res_status_value = RES_COL + '_status', 200


old_df = pd.read_json('/workspace/linjh/github/learn/Awesome-MLLM-For-Games/tools/arxiv_tools/asset/update_0323/all_paper.jsonl', lines=True).to_dict(orient='records')
paper2info = {x['title']: x for x in old_df}
waited_processed_data = []
for i in range(len(meta_jsonl_data)):
    if meta_jsonl_data[i]['title'] in paper2info:
        meta_jsonl_data[i] = deepcopy(paper2info[meta_jsonl_data[i]['title']])
    else:
        waited_processed_data.append(meta_jsonl_data[i])

save_jsonl_data = meta_jsonl_data
print(f'Not done: {len(waited_processed_data)}, total: {len(meta_jsonl_data)}')





Convert_Back_Conversation = False
    
# 5. save when three conditions are met: 1. meet-except;   2. meet ctrl-c;   3. meet the find end of the program
def save_data(**kwargs):
    if args.output_file.exists():
        print(f'File {args.output_file} already exists, skip the Saving.')
        return False
    out_info = dict(orient='records', indent=2) if str(args.output_file).endswith('.json') else dict(orient='records', lines=True)
    if Convert_Back_Conversation:
        for item in save_jsonl_data:
            item['conversations'] = item['ori_conversations']
    pd.DataFrame(save_jsonl_data).to_json(args.output_file, force_ascii=False, **out_info)
    print(f'File {args.output_file} generated.')
    return True
    

def register_save_at_any_exit():
    def save_at_exception(exc_type, exc_value, exc_traceback):
        if args.output_file.exists(): return
        print(f'Save at exception: {exc_type}, {exc_value}, {exc_traceback} --> ', end='\t'); save_data()
    def save_at_interrupt(signal, frame):
        if args.output_file.exists(): return 
        print(f'Save at interrupt: {signal}, {frame} --> ', end='\t'); save_data()
    def save_at_exit():
        if args.output_file.exists(): return 
        print('Save at exit --> ', end='\t'); save_data()
    sys.excepthook = save_at_exception
    signal.signal(signal.SIGINT, save_at_interrupt)
    atexit.register(save_at_exit)
# register_save_at_any_exit()



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>> Call LLM  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## >>>>>>>>> 1. get prompt
class GetPrompt:
    """Wrap Two step(get info of {..}, fill it into template), then we get prompt"""
    def __init__(self, get_info_func_id=None, template=None):
        self.get_info_func = getattr(self, f'get_info_from_item_of_{get_info_func_id}' )
        self.template = template
        
    def get_info_from_item_of_annot(self, item, merge_item=True):
        question = item['reference'].split('![【插图】]')[0].strip()
        return {'question': question, **item} if merge_item else {'question': question}

    def get_info_from_item_of_alpaca(self, item, merge_item=True):
        assert item['conversations'][0]['role'] == 'user' and item['conversations'][1]['role'] == 'assistant'
        question, answer = item['conversations'][0]['text'], item['conversations'][1]['text']
        input_info = {'question': question, 'answer': answer, **item}
        return input_info if merge_item else {'question': question, 'answer': answer}

    def __call__(self, item):
        input_info = self.get_info_func(item)
        return self.template.format(**input_info)


## >>>>>>>>> 2. get image
def get_image_from_item(item) -> io.BytesIO:
    if 'img_file_io_param' in item:
        if not isinstance(item['img_file_io_param'], list):
            img_bytes_io_arr = get_image_file(**item['img_file_io_param'])
            image_path_or_obj = img_bytes_io_arr
        else:
            # 多图
            # filter_out_useless_img(item)
            image_path_or_obj = [
                get_image_file(**img_file_io_param)
                for img_file_io_param in item['img_file_io_param']
            ]
    else:
        image_path_or_obj = item['image_path']
        # 如果是url，则先读取成bytes
        if image_path_or_obj.startswith('http'):
            response = requests.get(image_path_or_obj)  # 发起 HTTP GET 请求
            image_bytes = response.content  # 获取响应的内容作为字节流
            image_path_or_obj = BytesIO(image_bytes)
    return image_path_or_obj

## >>>>>>>>> 3. get server
chatapi = ChatAPI(model_name=args.model_name)

##### 套两个装饰器（重试+打印错误）
def retry_request(max_retries=2, delay=0.5, retry_break_checker=lambda x: x[0] == 200):
    """可以弄一个retry_precess_one，解码失败等，都可以retry"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                result = func(*args, **kwargs)
                if retry_break_checker(result): # break
                    return result
                retries += 1
                time.sleep(delay)
            return None
        return wrapper
    return decorator


def print_error_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred in function '{func.__name__}': {str(e)}")
            return -1, ''
    return wrapper
# 尽量不要并发的时候，不要开，变慢了非常多。。。。。
# chatapi.get_gpt_response = retry_request()(chatapi.get_gpt_response)  # 不在request套，而是在request_parse_and_save套用
# chatapi.get_gpt_response = print_error_decorator(chatapi.get_gpt_response)


## >>>>>>>>> 4. call server
####### >>>>>>>> 4.1 two process func to define logic <<<<<<<<<<<
# @print_error_decorator
def process_one(item, follow_process_one_list=None):
    # import pdb; pdb.set_trace()
    # 1. get answer and image
    if 'query_prompt' in item:
        prompt = item['query_prompt']
    else:
        prompt = prompt_getter(item)
    request_gpt_args = dict(prompt=prompt)
    if args.model_name not in textual_model:
        request_gpt_args.update(image=get_image_from_item(item))
    if 'local-R1-32b' == args.model_name:
        request_gpt_args.update(Local_R1_IP = '0.0.0.0', tokenizer_path = '/workspace/yangzhen/DeepSeek-R1-Distill-Qwen-32B')
    
    # 2. get response and save
    # @retry_request(max_retries=2, delay=0.5, retry_break_checker=lambda x: x[0] == 200)
    def request_parse_and_save():
        status, result = chatapi.get_gpt_response(**request_gpt_args)                               
        parse_result = nlp.Parser.match_any_in_paragraph(result)
        item[RES_COL] = parse_result
        item[res_status_col] = status
        # >>> if you need any else, save it here
        # item[RES_COL+'_prompt'] = request_gpt_args['prompt']
        if do_more_parse:
            do_more_parse(item)
        return status, result
    
    request_parse_and_save()
        
    # 3. do the follow process if you want to compose a chain
    if follow_process_one_list is not None:
        for f in follow_process_one_list:
            f(item)
    return ''



####### >>>>>>>> 4.2 Rollout and judge prompt (for res of llm)👇🏻 <<<<<<<<<<<
# 1. if your info is fixed
# prompt_getter = GetPrompt(get_info_func_id='alpaca', template=response_template)

# 2. if your info is dynamic, set yourself

####### >>>>>>>> Rollout prompt 👆🏻 <<<<<<<<<<<



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>> Save jsonl and show  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

if not args.output_file.exists():
    try:
        # process_one(waited_processed_data[0])
        nlp.Parrallel.process_parallel_in_all_case(item_list=waited_processed_data, max_workers=args.max_workers, process_one=process_one, model_name=args.model_name)
        save_data()
    except Exception as e:
        print(f'Error occurred during parallel processing: {e}')
        print(f'File {args.output_file} Will be generated with partial data due to error.')    
else:
    print(f'File {args.output_file} already exists, skip the generation.')


if args.do_show_html:
    try:
        show_gen_cot_data(
            input_file_or_dir_or_df=str(args.output_file),
            output_html_path=args.output_file.with_suffix('.html'),
            keep_some_col_for_just_add_a_col=INPUT_COLS + [RES_COL] if not do_more_parse else INPUT_COLS + MORE_COLS,
            sample_size=50,
            process_func=None,
            just_need_single_graph=True
        )
    except Exception as e:
        if os.path.exists(args.output_file):
            df = pd.read_json(args.output_file, lines=True)

        print(f'df columns: {df.columns}')
        # df.drop(columns=['image_path'], inplace=True)
        df = df[ INPUT_COLS + [RES_COL] + MORE_COLS ]
        openitem_to_html(
            df,
            output_html_path=args.output_file.with_suffix('.html'),
            textual_cols = INPUT_COLS + [RES_COL] if not do_more_parse else INPUT_COLS + [RES_COL] + MORE_COLS,
        )

        
