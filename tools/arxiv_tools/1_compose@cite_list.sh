# tools/arxiv_tools/asset/update_0323/geo_cite/list_geo_cite.md
# tools/arxiv_tools/asset/update_0323/baai_cite/list_baai_cite.md
# cur_id="geo"
cur_id="baai"

echo ">>>>> [START] 1_gen_paper_content.py"
python3 tools/arxiv_tools/1_gen_paper_content.py \
    --input_file tools/arxiv_tools/asset/update_0323/${cur_id}_cite/list_${cur_id}_cite.md \
    --do_from_list

echo ">>>>> [END] 1_gen_paper_content.py"


echo ">>>>> [START] 15_gen_tldr_research.py"
python3 tools/arxiv_tools/15_gen_tldr_research.py \
    --input_file tools/arxiv_tools/asset/update_0323/${cur_id}_cite/source_${cur_id}_cite.jsonl \
    --output_file tools/arxiv_tools/asset/update_0323/${cur_id}_cite/tldr_${cur_id}_cite.jsonl

echo ">>>>> [END] 15_gen_tldr_research.py"

echo ">>>>> [START] 16_gen_final_md.py"
python3 tools/arxiv_tools/16_gen_final_md.py \
    --input_file tools/arxiv_tools/asset/update_0323/${cur_id}_cite/tldr_${cur_id}_cite.jsonl \

echo ">>>>> [END] 16_gen_final_md.py"