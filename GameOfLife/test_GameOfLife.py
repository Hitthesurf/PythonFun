#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:33:26 2020

@author: pi
"""

from unittest import TestCase
from GameOfLife import GameOfLifeGrid

class TestGameOfLife(TestCase):
    def test_get_neighbour_count_is_correct_when_point_not_on_boundary(self):
        grid = GameOfLifeGrid()
        #grid.grid_size = [6,6]
        input_grid = [[0,1,1,0,0],
                      [1,1,0,0,1],
                      [0,0,1,0,0]]
        grid.curent_grid = input_grid
        in_right = 3
        in_down = 2
        expected = 3
        actual = grid.get_neighbour_count(in_down, in_right)
        self.assertEqual(expected, actual)