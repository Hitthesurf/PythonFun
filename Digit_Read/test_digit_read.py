#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:33:14 2019

@author: pi
"""

from unittest import TestCase
from digit_read import Digit
from math_functions import MathFunction

class TestMathFucntions(TestCase):
    def test_mult_can_mult_can_multiply_1_by_1_matrix(self):
        math = MathFunction()
        A_matrix = [[5]]
        B_matrix = [[10]]
        expected_matrix = [[50]]
        actual_matrix = math.mult(A_matrix, B_matrix)
        self.assertEqual(actual_matrix, expected_matrix)
        
    def test_mult_can_mult_can_multiply_3x2_by_2x2_matrix(self):
        math = MathFunction()
        A_matrix = [[1, 3],
                    [4,-1],
                    [5, 2]]
        B_matrix = [[5, 1],
                    [2,-5]]
        expected_matrix = [ [11,-14],
                            [18,  9],
                            [29, -5]]
        actual_matrix = math.mult(A_matrix, B_matrix)
        self.assertEqual(actual_matrix, expected_matrix)
        
    def test_mult_can_mult_can_multiply_3x2_by_2x3_matrix(self):
        math = MathFunction()
        A_matrix = [[1, 3],
                    [4,-1],
                    [5, 2]]
        B_matrix = [[5, 1, 5],
                    [2,-5, 2]]
        expected_matrix = [ [11,-14, 11],
                            [18,  9, 18],
                            [29, -5, 29]]
        actual_matrix = math.mult(A_matrix, B_matrix)
        self.assertEqual(actual_matrix, expected_matrix)
        
    def test_mult_can_mult_can_multiply_1x2_by_2x3_matrix(self):
        math = MathFunction()
        A_matrix = [[1, 3]]
        B_matrix = [[5, 1, 4],
                    [2,-5, 6]]
        expected_matrix = [ [11,-14, 22]]
        actual_matrix = math.mult(A_matrix, B_matrix)
        self.assertEqual(actual_matrix, expected_matrix)

class TestDigitRead(TestCase):
    def test_next_layer_outputs_correct_vector(self):
        comp = Digit()
        in_vector = matrix([0.5,0.75])
        weights = matrix([2,1], #bias weights
                               [3,4],
                               [0,1])
        expected_output = matrix([1])
        self.assertEqual("m", "p")