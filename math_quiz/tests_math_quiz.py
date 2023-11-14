import unittest
from math_quiz import operand_fetch, operator_fetch, res_calc
"""
imports the methods from mathquiz.py for testing
"""

class TestMathGame(unittest.TestCase):
    """generates test cases for math_quiz.py

    Args:
        unittest (object): a set mathematical problems are given to math_quiz.py
        for validation
    """
    def sample_datagen(self):
        """
        generates large number of random data in the range of 1 to 10
        """            
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = operand_fetch(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def sample_operatorgen(self):
        """
        generates a large set of random operators among '+' '-' '*'
        """        
        for _ in range(250):  
            operation = operator_fetch()
            self.assertIn(operation, ['+', '-', '*'])
        

    def random_tests(self):
        """
        7 test cases were given to check for the logical errors in 
        mathquiz.py
        """        
        test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 3, '*', '6 * 3', 18),
                (7, 4, '-', '7 - 4', 3),
                (18, 5, '-', '18 - 5', 13),
                (6, 9, '*', '6 * 9', 54),
                (5, 0, '+', '5 + 0', 5),
                (2 , 2, '-', '2 - 2', 0)
            ]
            #looping through the test cases taking the inputs and passing it to res_calc method
        for data1, data2, operator, testproblem, testanswer in test_cases:
            problem, answer = res_calc(data1, data2, operator)
            #calls the res_calc method to generate problem and answer
            self.assertEqual(problem, testproblem)
            #verifies generated problems with test problems.
            self.assertEqual(answer, testanswer)
            #verifies generated answers with expected answer.

if __name__ == "__main__":
    unittest.main()
