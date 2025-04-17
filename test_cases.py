import json
import os
import random
import subprocess
import time
import re
import csv

results = []

def execute_test_case(test_case_code):
    """
    Executes the test case code.
    """
    try:
        # Dynamically execute the test case using exec
        exec(test_case_code)
        return "Test case passed!"
    except AssertionError:
        return "Test case failed!"
    except Exception as e:
        print(f"An error occurred: {e}")

def test_code(code_source):

        dataset_file = "binary_search_data.json"
        try:
            with open(dataset_file, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{dataset_file}' was not found.")
            return
        except json.JSONDecodeError:
            print(f"Error: Failed to parse JSON in '{dataset_file}'.")
            return

        # Iterate through each problem in the dataset
        for i in range(len(data)):
            # Get the dictionary for each problem
            problem_dictionary = data[i]
            test_case_string = data[i]['test_case']
            match = re.search(r"solution\.(\w+)\(", test_case_string)
            if match:
                function_name = match.group(1)

            if code_source == "Human":
                # Get the test_case_generator and test_case
                source_code = "from bisect import bisect_right, bisect_left\nimport math\nfrom collections import Counter\nimport time\n" + problem_dictionary.get("test_case_generator") + "\nsolution = Solution()"
                source_code = source_code.replace("if __name__ == \"__main__\":\n    num_tests = 100\n    test_case_generator_results = test_generated_test_cases(num_tests)\n", "")
                source_code = source_code.replace("if __name__ == \"__main__\":\n    num_tests = 100  # You can change this to generate more test cases\n    test_case_generator_results = test_generated_test_cases(num_tests)\n", "")
                test_case_code = problem_dictionary.get("test_case")
            else:              
                folder_name = f"{code_source}_Outputs"
                file_name = f"Problem_{i+1}_{function_name}.py"
                file_path = os.path.join(folder_name, file_name)
                with open(file_path, 'r') as file:
                    source_code = file.read() + "\nsolution = Solution()"
                test_case_code = problem_dictionary.get("test_case")

            exec(source_code, globals())

            # Execute the test case generator
            start_time = time.time()
            test_pass = execute_test_case(test_case_code)
            end_time = time.time()
            total_time = end_time - start_time
            results.append([i+1,function_name,code_source,total_time, problem_dictionary.get("difficulty"), test_pass])

def main():

    test_code("Human")
    test_code("GPT4o")
    # test_code("Gemini")
    # test_code("Deepseek")
    
    for i in range(len(results)):
            results.sort()
            print(f"Problem #{results[i][0]} ({results[i][2]}): \t{(results[i][3] * 1000):.4f} ms\t{results[i][5]} Task:{results[i][1]}")
            
    with open('results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == "__main__":
    main()