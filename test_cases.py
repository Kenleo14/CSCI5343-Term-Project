import json
import os
import random
import subprocess
import time
import re

def execute_test_case(test_case_code):
    """
    Executes the test case code.
    """
    try:
        # Dynamically execute the test case using exec
        exec(test_case_code)
        print("\t\tTest case passed!")
    except AssertionError:
        print("\t\tTest case failed!")
    except Exception as e:
        print(f"\t\tAn error occurred: {e}")

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

        execution_times = []
        # Iterate through each problem in the dataset
        for i in range(len(data)):
            # Get the dictionary for each problem
            problem_dictionary = data[i]
            test_case_string = data[i]['test_case']
            match = re.search(r"solution\.(\w+)\(", test_case_string)
            if match:
                function_name = match.group(1)

            if code_source == "human_code":
                # Get the test_case_generator and test_case
                source_code = "from bisect import bisect_right, bisect_left\nimport math\nimport time\n" + problem_dictionary.get("test_case_generator") + "\nsolution = Solution()"
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
                # function_list = ['shipWithinDays','peakIndexInMountainArray','reachNumber','nums','findKthPositive','countNegatives','arraysIntersection','isMajorityElement','searchInsert','missingNumber','intersection','intersect','isPerfectSquare','search','nextGreatestLetter','fairCandySwap','fixedPoint','findMin','findPeakElement','minSubArrayLen','hIndex','findDuplicate','kthSmallest','findRadius','mySqrt','findRadius','findPairs','singleNonDuplicate','findKthNumber','preimageSizeFZF','maximizeSweetness','closestToTarget','minWastedSpace','minOperations','maxTotalFruits']
                # for function in function_list:
                #     test_case_code = test_case_code.replace(f"solution.{function}","Solution")
                #test_case_code = test_case_code.replace("solution.searchInsert","Solution").replace("solution.mySqrt", "Solution").replace("solution.missingNumber", "Solution").replace("solution.intersection", "Solution").replace("solution.intersect", "Solution").replace("solution.isPerfectSquare", "Solution").replace("solution.search", "Solution").replace("solution.nextGreatestLetter", "Solution").replace("solution.fairCandySwap", "Solution").replace("solution.fixedPoint", "Solution").replace("solution.findMin", "Solution").replace("solution.findPeakElement", "Solution").replace("solution.minSubArrayLen", "Solution").replace("solution.", "Solution")

            exec(source_code, globals())

            # Execute the test case generator
            start_time = time.time()
            execute_test_case(test_case_code)
            end_time = time.time()
            total_time = end_time - start_time
            execution_times.append([i,total_time, problem_dictionary.get("difficulty")])
            print(f"Problem #{i + 1}\t({execution_times[i][2]}): \t{(execution_times[i][1] * 1000):.4f} ms")
        # for i in range(len(execution_times)):
            

def main():

    test_code("human_code")
    test_code("GPT4o")
    #add return to functions for execution times and test case passed
    #add Human/LLM to Problem name

if __name__ == "__main__":
    main()