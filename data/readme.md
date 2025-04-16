Effibench dataset_with_difficulty_and_algorithms.json is too large for upload. Referenced here as "data.json"

Use clean_data.py to extract our problem set from data.json (https://github.com/huangd1999/EffiBench/blob/main/data/dataset_with_difficulty_and_algorithm.json):
1) Removes uneeded algorithms from data.json.
2) Removes problems sets with typos or code errors.
3) Selects group of 10 Easy, 10 Medium and 10 Hard Problems

run_test_cases.py currently only runs tests for the human generated code. This outputs the execution time for each of the 30 problems. Working on adding functionality
for reading/executing LLM generated code saved in LLM folders.
