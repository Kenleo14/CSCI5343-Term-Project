import json
import random

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
    # Load the effibench dataset from the JSON file
    dataset_file = "data_binary_search.json"
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
    for problem in data:
        # print(f"Executing test cases for problem: {problem['task_name']}")
        
        # Get the test_case_generator and test_case
        test_case_generator_code = problem.get("test_case_generator")
        test_case_code = problem.get("test_case")

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
            execute_test_case(test_case_code)

if __name__ == "__main__":
    main()