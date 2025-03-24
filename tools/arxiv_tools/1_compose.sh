cur_id=game_bench
# cur_id=game_vlm

# echo ">>>>> [START] 1_gen_paper_content.py"
# python3 tools/arxiv_tools/1_gen_paper_content.py \
#     --input_file tools/arxiv_tools/asset/update_0323/${cur_id}/terms_${cur_id}.md \
#     --n_paper 200

# echo ">>>>> [END] 1_gen_paper_content.py"


# echo ">>>>> [START] 15_gen_tldr_research.py"
# python3 tools/arxiv_tools/15_gen_tldr_research.py \
#     --input_file tools/arxiv_tools/asset/update_0323/${cur_id}/source_${cur_id}.jsonl \
#     --output_file tools/arxiv_tools/asset/update_0323/${cur_id}/tldr_${cur_id}.jsonl

# echo ">>>>> [END] 15_gen_tldr_research.py"

echo ">>>>> [START] 16_gen_final_md.py"
python3 tools/arxiv_tools/16_gen_final_md.py \
    --input_file tools/arxiv_tools/asset/update_0323/${cur_id}/tldr_${cur_id}.jsonl \

echo ">>>>> [END] 16_gen_final_md.py"