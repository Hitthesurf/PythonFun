#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:33:26 2020

@author: pi
"""

from unittest import TestCase
from GameOfLife import GameOfLifeGrid

class TestGameOfLifeGridCount(TestCase):
    def before_each_test(self):
        grid = GameOfLifeGrid()
        #grid.grid_size = [6,6]
        input_grid = [[0,1,1,0,0],
                      [1,1,0,0,1],
                      [0,0,1,0,0]]
        grid.current_grid = input_grid
        return grid
        
    def test_get_neighbour_count_is_correct_when_point_not_on_boundary_1(self):
        grid = self.before_each_test()
        in_right = 3
        in_down = 2
        expected = 4
        actual = grid.get_neighbour_count(in_down, in_right)
        self.assertEqual(expected, actual)
        
    def test_get_neighbour_count_is_correct_when_point_not_on_boundary_2(self):
        grid = self.before_each_test()
        in_right = 4
        in_down = 2
        expected = 3
        actual = grid.get_neighbour_count(in_down, in_right)
        self.assertEqual(expected, actual)
    
    def test_get_value_gets_the_correct_value_for_position_in_range_1(self):
        grid = self.before_each_test()
        in_right = 3
        in_down = 2
        expected = 0
        actual = grid.get_value(in_down, in_right)
        self.assertEqual(expected, actual)
        
    def test_get_value_gets_the_correct_value_for_position_in_range_2(self):
        grid = self.before_each_test()
        in_right = 3
        in_down = 1
        expected = 1
        actual = grid.get_value(in_down, in_right)
        self.assertEqual(expected, actual)
    
    
    