import json
import os
import random
import subprocess
import time

def execute_test_case(test_case_code):
    """
    Executes the test case code.
    """
    try:
        # Dynamically execute the test case using exec
        exec(test_case_code)
        print("Test case passed!")
    except AssertionError:
        print("Test case failed!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():

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

    execution_times = []

    # Iterate through each problem in the dataset
    for i in range(len(data)):
        # print(f"Executing test cases for problem: {problem['task_name']}")

        problem = data[i]

        # Get the test_case_generator and test_case
        test_case_generator_code = "from bisect import bisect_right, bisect_left\nimport math\nimport time\n" + problem.get("test_case_generator") + "\nsolution = Solution()"
        test_case_generator_code = test_case_generator_code.replace("if __name__ == \"__main__\":\n    num_tests = 100\n    test_case_generator_results = test_generated_test_cases(num_tests)\n", "")
        test_case_generator_code = test_case_generator_code.replace("if __name__ == \"__main__\":\n    num_tests = 100  # You can change this to generate more test cases\n    test_case_generator_results = test_generated_test_cases(num_tests)\n", "")
        test_case_code = problem.get("test_case")

        # print(test_case_generator_code)

        # Execute the test case generator
        if test_case_generator_code:
            print("Generating test cases...")
            try:
                exec(test_case_generator_code, globals())
            except Exception as e:
                print(f"An error occurred while generating test cases: {e}")
                continue

        # Execute the test case
        if test_case_code:
            start_time = time.time()
            execute_test_case(test_case_code)
            end_time = time.time()
            total_time = end_time - start_time
            execution_times.append([i,total_time, problem.get("difficulty")])
    
    results_easy = []
    results_medium = []
    results_hard = []

    for i in range(len(execution_times)):
        if execution_times[i][2] == "Easy":
            results_easy.append(execution_times[i])
        if execution_times[i][2] == "Medium":
            results_medium.append(execution_times[i])
        if execution_times[i][2] == "Hard":
            results_hard.append(execution_times[i])

    results = results_easy + results_medium + results_hard

    for i in range(len(results)):
        print(f"Problem #{i + 1}\t({results[i][2]}): \t{(results[i][1] * 1000):.4f} ms")

if __name__ == "__main__":
    main()