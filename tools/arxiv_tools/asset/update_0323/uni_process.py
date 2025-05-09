import re
from datetime import datetime

# 读入原始 markdown 文件
with open('uni.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 匹配每个条目：假定格式为 "- [YY/MM] **标题** ..."；使用 DOTALL 让内容能跨行
pattern = re.compile(r'(- \[\d{2}/\d{2}\].*?)(?=\n- \[\d{2}/\d{2}\]|$)', re.DOTALL)
items = pattern.findall(text)

# 清理 Code/Page 链接后多余的点
cleaned_items = []
for item in items:
    # 移除 Code/Page 链接闭合后紧跟的 '.'
    item = re.sub(r"(\[\[Code/Page\]\(.*?\)\])\.", r"\1", item)
    cleaned_items.append(item)
items = cleaned_items

# 按标题分组，记录每条的日期、文本及非空链接数
groups = {}
for item in items:
    date_str = re.search(r'\[(\d{2}/\d{2})\]', item).group(1)
    dt = datetime.strptime(date_str, '%y/%m')
    title = re.search(r'\*\*(.*?)\*\*', item).group(1).strip()
    # 统计非空链接数量 (Code/Page, TLDR/Notes)
    links = re.findall(r'\[\[(?:Code/Page|TLDR/Notes)\]\((.*?)\)\]', item)
    link_count = sum(1 for url in links if url.strip())
    groups.setdefault(title, []).append({
        'dt': dt,
        'text': item.strip(),
        'link_count': link_count
    })

# 打印所有重复的内容（包括所有版本）
has_duplicates = False
for title, entries in groups.items():
    if len(entries) > 1:
        has_duplicates = True
        print(f"Duplicate entries for title: {title}")
        for e in sorted(entries, key=lambda x: x['dt'], reverse=True):
            print(f"  - [{e['dt'].strftime('%y/%m')}] links={e['link_count']}: {e['text'].splitlines()[0]}...")
        print()
if not has_duplicates:
    print("No duplicate entries found.")

# 去重：
# 单条记录：去除空链接; 多条记录：选 link_count 最大的那条，若相同则选最新日期
unique = {}
for title, entries in groups.items():
    if len(entries) == 1:
        e = entries[0]['text']
        # 移除空的 Code/Page 与 TLDR/Notes 链接
        e = re.sub(r"\[\[Code/Page\]\(\s*\)\]", "", e)
        e = re.sub(r"\[\[TLDR/Notes\]\(\s*\)\]", "", e)
        # 清理多余空格
        e = re.sub(r"[ \t]+", " ", e).strip()
        unique[title] = {'dt': entries[0]['dt'], 'text': e}
    else:
        # 多条，优先 link_count，再日期
        best = sorted(entries, key=lambda x: (x['link_count'], x['dt']), reverse=True)[0]
        unique[title] = {'dt': best['dt'], 'text': best['text']}

# 按日期降序排序
sorted_items = sorted(unique.values(), key=lambda x: x['dt'], reverse=True)

# 写入新文件
with open('uni_output.md', 'w', encoding='utf-8') as f:
    for entry in sorted_items:
        f.write(entry['text'] + '\n\n')

print(f"处理完成，共 {len(sorted_items)} 条，已写入 uni_output.md")
