"""

"""

import json
import os
import random
import subprocess
import time

def remove_non_binary_search():
    with open('data.json', 'r') as file:
        data = json.load(file)

    algorithm = "binary_search"

    for i in range(len(data)):
        try:
            while data[i]['algorithms'][0] != algorithm:
                    del data[i]
        except IndexError:
            print(f"Other algorithms removed from data.json")
            break
        
    with open('binary_search_data.json', 'w') as file:
        json.dump(data, file, indent = 4)

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
        return 1

def main():
    # Load the effibench dataset from the JSON file and only keep binary_search problems
    remove_non_binary_search()

    binary_search_dataset = "binary_search_data.json"
    try:
        with open(binary_search_dataset, "r") as file:
            binary_search_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{binary_search_dataset}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in '{binary_search_dataset}'.")
        return

    removeErrors = []

    # Iterate through each problem in the dataset
    for i in range(len(binary_search_data)):
        try:
        # print(f"Executing test cases for problem: {problem['task_name']}")
            problem = binary_search_data[i]

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
                    removeErrors.insert(0, i)
                    continue

            # Execute the test case
            if test_case_code:
                if execute_test_case(test_case_code) == 1:
                    removeErrors.insert(0, i)
                # execute_test_case(test_case_code)

        except IndexError:
            print(f"Reached end of list")
            break

    print(f"Binary Search Problems: {len(binary_search_data)}")

    print(f"Problems with errors: {removeErrors}")

    for i in removeErrors:
        del binary_search_data[i]

    easyCount = 0
    medCount = 0
    hardCount = 0
    deleteList = []

    for i in range(len(binary_search_data)):
        try:
            if binary_search_data[i]['difficulty'] == "Easy" and easyCount < 10:
                easyCount += 1
            elif binary_search_data[i]['difficulty'] == "Medium" and medCount < 10:
                medCount += 1
            elif binary_search_data[i]['difficulty'] == "Hard" and hardCount < 10:
                hardCount += 1
            else: 
                deleteList.insert(0, i)
                
        except IndexError:
            print(f"Reached end of list")
            break

    for i in deleteList:
        del binary_search_data[i]

    with open(binary_search_dataset, 'w') as file:
        json.dump(binary_search_data, file, indent=4)

    with open(binary_search_dataset, 'r') as file:
        binary_search_data = json.load(file)

    print(f"Final Problem Count (binary_search_data.json): {len(binary_search_data)}")

if __name__ == "__main__":
    main()