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
        
    def test_get_neighbour_count_gets_correct_count_in_corner_1(self):
        grid = self.before_each_test()
        in_right = 1
        in_down = 1
        expected = 4
        actual = grid.get_neighbour_count(in_down, in_right)
        self.assertEqual(expected, actual)
        
    def test_get_neighbour_count_gets_correct_count_in_corner_2(self):
        grid = self.before_each_test()
        in_right = 5
        in_down = 1
        expected = 2
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
        
    def test_get_value_gets_the_correct_value_for_position_out_of_range(self):
        grid = self.before_each_test()
        in_right = 6
        in_down = 4
        expected = 0
        actual = grid.get_value(in_down, in_right)
        self.assertEqual(expected, actual)
    
    
        
class TestGameOfLifeGridNextState(TestCase):
    def test_next_state_is_death_when_neighbours_is_1_and_current_state_1(self):
        grid = GameOfLifeGrid()
        in_neighbours = 1
        in_current_state = 1
        expected = 0
        actual = grid.next_state(in_neighbours, in_current_state)
        self.assertEqual(expected, actual)
    
    def test_next_state_is_life_when_neighbours_is_2_and_current_state_1(self):
        grid = GameOfLifeGrid()
        in_neighbours = 2
        in_current_state = 1
        expected = 1
        actual = grid.next_state(in_neighbours, in_current_state)
        self.assertEqual(expected, actual)
    
    def test_next_state_is_life_when_neighbours_is_3_and_current_state_1(self):
        grid = GameOfLifeGrid()
        in_neighbours = 3
        in_current_state = 1
        expected = 1
        actual = grid.next_state(in_neighbours, in_current_state)
        self.assertEqual(expected, actual)
        
    def test_next_state_is_death_when_neighbours_is_4_and_current_state_1(self):
        grid = GameOfLifeGrid()
        in_neighbours = 4
        in_current_state = 1
        expected = 0
        actual = grid.next_state(in_neighbours, in_current_state)
        self.assertEqual(expected, actual)
    
    def test_next_state_is_life_when_neighbours_is_3_and_current_state_0(self):
        grid = GameOfLifeGrid()
        in_neighbours = 3
        in_current_state = 0
        expected = 1
        actual = grid.next_state(in_neighbours, in_current_state)
        self.assertEqual(expected, actual)
        
    def test_next_state_is_death_when_neighbours_is_not_3_and_current_state_0(self):
        grid = GameOfLifeGrid()
        in_neighbours = 2
        in_current_state = 0
        expected = 0
        actual = grid.next_state(in_neighbours, in_current_state)
        self.assertEqual(expected, actual)
        
class TestGameOfLifeNextGrid(TestCase):
    def test_next_grid_calculates_the_correct_grid_given_no_live_cells_next_to_boundary(self):
        grid = GameOfLifeGrid()
        #Beacon Oscillator
        input_grid = [[0,0,0,0,0,0,0],
                      [0,1,1,0,0,0,0],
                      [0,1,0,0,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,1,1,0,0],
                      [0,0,0,0,0,0,0]]
        
        expected =   [[0,0,0,0,0,0,0],
                      [0,1,1,0,0,0,0],
                      [0,1,1,0,0,0,0],
                      [0,0,0,1,1,0,0],
                      [0,0,0,1,1,0,0],
                      [0,0,0,0,0,0,0]]
        grid.current_grid = input_grid
        grid.next_grid()
        actual = grid.current_grid
        self.assertEqual(expected, actual)
        
    def test_next_grid_calculates_the_correct_grid_when_life_on_edge(self):
        grid = GameOfLifeGrid()
        #Blinker Oscillator
        input_grid = [[1,1,0,0,1],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0]]
        expected = [[1,0,0,0,0],
                    [1,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,0]]
        grid.current_grid = input_grid
        grid.next_grid()
        actual = grid.current_grid
        self.assertEqual(expected, actual)
        