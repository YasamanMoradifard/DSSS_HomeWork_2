import unittest
from math_quiz import Random_number, Operation, Operation_on_numbers


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = Random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
        print("\nFunction_A is OK")

    def test_function_B(self):
        #Test the Operation function
        # Number of tests
        num_tests = 1000

        for _ in range(num_tests):
            result = Operation()

            # Check if the result is one of the expected operations
            valid_operations = {'+', '-', '*'}
            assert result in valid_operations, f"Unexpected operation: {result}"

        print(f"\nFunction_B is OK.")

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
            (-4, 6, '*', '-4 * 6', -24),
         ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            result_problem, result_answer = Operation_on_numbers(num1, num2, operator)
            assert result_problem == expected_problem, f"Test failed for problem: {result_problem}"
            assert result_answer == expected_answer, f"Test failed for answer: {result_answer}"

        print("\nFunction_c is OK.")

if __name__ == "__main__":
    unittest.main()
