# tools/arxiv_tools/asset/update_0323/geo_cite/list_geo_cite.md
# tools/arxiv_tools/asset/update_0323/baai_cite/list_baai_cite.md
# cur_id="geo"
# cur_id="baai"
# cur_name=${cur_id}_cite


# cur_name="method_papers"
cur_name="unify"
echo ">>>>> [START] 1_gen_paper_content.py"
python3 tools/arxiv_tools/1_gen_paper_content.py \
    --input_file tools/arxiv_tools/asset/update_0323/${cur_name}/list_${cur_name}.md \
    --do_from_list

echo ">>>>> [END] 1_gen_paper_content.py"


echo ">>>>> [START] 15_gen_tldr_research.py"
python3 tools/arxiv_tools/15_gen_tldr_research.py \
    --input_file tools/arxiv_tools/asset/update_0323/${cur_name}/source_${cur_name}.jsonl \
    --output_file tools/arxiv_tools/asset/update_0323/${cur_name}/tldr_${cur_name}.jsonl

echo ">>>>> [END] 15_gen_tldr_research.py"

echo ">>>>> [START] 16_gen_final_md.py"
python3 tools/arxiv_tools/16_gen_final_md.py \
    --input_file tools/arxiv_tools/asset/update_0323/${cur_name}/tldr_${cur_name}.jsonl \

echo ">>>>> [END] 16_gen_final_md.py"