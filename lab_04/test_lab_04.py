import unittest
from lab_04 import infix_to_rpn, evaluate_rpn

class TestCalculator(unittest.TestCase):
    def test_infix_to_rpn(self):
        self.assertEqual(infix_to_rpn(['3', '+', '4']), ['3', '4', '+'])
        self.assertEqual(infix_to_rpn(['5', '*', '(', '2', '+', '3', ')']), ['5', '2', '3', '+', '*'])
        self.assertEqual(infix_to_rpn(['(', '1', '+', '2', ')', '*', '3']), ['1', '2', '+', '3', '*'])

    def test_evaluate_rpn(self):
        self.assertEqual(evaluate_rpn(['3', '4', '+']), 7)
        self.assertEqual(evaluate_rpn(['5', '2', '3', '+', '*']), 25)
        self.assertEqual(evaluate_rpn(['1', '2', '+', '3', '*']), 9)

    def test_combined_functionality(self):
        infix_expression = ['3', '+', '4']
        rpn_expression = infix_to_rpn(infix_expression)
        result = evaluate_rpn(rpn_expression)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()