# CSCI5343-Term-Project

Project Description:
https://tamusa.blackboard.com/ultra/courses/_268909_1/cl/outline

Effibench dataset_with_difficulty_and_algorithms.json is too large for upload. Referenced here as "data.json"

Use clean_data.py to extract our problem set from data.json (https://github.com/huangd1999/EffiBench/blob/main/data/dataset_with_difficulty_and_algorithm.json):

    Removes uneeded algorithms from data.json.
    Removes problems sets with typos or code errors.
    Selects group of 10 Easy, 10 Medium and 10 Hard Problems

test_cases.py currently only runs tests for the human generated code located in binary_search_data.json. This outputs the execution time for each of the 30 problems. Working on adding functionality for reading/executing LLM generated code saved in LLM folders.
