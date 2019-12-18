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
        expected_matrix = [[11,-14, 22]]
        actual_matrix = math.mult(A_matrix, B_matrix)
        self.assertEqual(actual_matrix, expected_matrix)
        
    def test_sigmoid_function_for_1x1_vector(self):
        math = MathFunction()
        num_input = [[5]]
        expected = [[0.9933071267165111]]
        actual = math.sigmoid(num_input)
        self.assertEqual(actual, expected)
        
    def test_sigmoid_function_for_1x4_vector(self):
        math = MathFunction()
        num_input = [[5,0,-2]]
        expected = [[0.9933071267165111,
                     0.5,
                     0.11920306327063111]]
        
        actual = math.sigmoid(num_input)
        self.assertEqual(actual, expected)

class TestDigitRead(TestCase):
    def test_next_layer_outputs_correct_vector(self):
        digit = Digit()
        in_vector = [[0.5,0.75]]
        wieghts = [[2,1], #bias weights
                   [3,4],
                   [0,1]]
        expected_output = [[0.970687702262056,
                            0.9770225734624428]]
        actual = digit.calc_next_layer(in_vector, wieghts)
        self.assertEqual(actual, expected_output)
        
    def test_save_wieght_and_read_wieght_work_together(self):
        digit = Digit()
        digit.file_location = "test_wieghts.txt"
        wieghts0 = [[1.2,2.0,3.0,4.0],
                    [4.0,2.0,3.0,1.5]]
        wieghts1 = [[5.0,6.3,7.0,8.0],
                    [2.0,3.0,1.0,4.0]]
        wieghts2 = [[3.0,1.0,5.0,9.0],
                    [2.9,7.0,9.0,9.0]]
        my_wieghts = [wieghts0, wieghts1, wieghts2]
        digit.mywieghts3D = [wieghts0, wieghts1, wieghts2]
        digit.save_wieghts()
        digit.mywieghts3D =[[[]]] #to make sure it doesnt cheat test
        digit.read_wieghts()
        actual = digit.mywieghts3D
        self.assertEqual(actual, my_wieghts)
    
    def test_save_wieght_and_read_wieght_work_together_2(self):
        digit = Digit()
        digit.file_location = "test_wieghts2.txt"
        wieghts0 = [[1.2,2.0],
                    [4.0,2.0]]
        wieghts1 = [[5.0,6.3,7.0,8.0],
                    [2.0,3.0,1.0,4.0],
                    [2.9,7.0,9.0,9.0]]
        my_wieghts = [wieghts0, wieghts1]
        digit.mywieghts3D = [wieghts0, wieghts1]
        digit.save_wieghts()
        digit.mywieghts3D =[[[]]] #to make sure it doesnt cheat test
        digit.read_wieghts()
        actual = digit.mywieghts3D
        self.assertEqual(actual, my_wieghts)
    
    def test_make_network_creates_correct_wieght_array_for_given_nodes_in_layer(self):
        digit = Digit()
        digit.file_location = "text_make_network.txt"
        num_nodes_in_layer = [2,3,1]
        wieghts0 = [[1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0]]
        wieghts1 = [[1.0],
                    [1.0],
                    [1.0],
                    [1.0]]
        expected_my_wieghts = [wieghts0, wieghts1]
        digit.make_network(num_nodes_in_layer, 1.0)
        actual = digit.mywieghts3D
        self.assertEqual(actual,expected_my_wieghts)
        