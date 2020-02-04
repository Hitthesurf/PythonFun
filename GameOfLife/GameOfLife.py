#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:33:24 2020

@author: pi
"""

class GameOfLifeGrid:
    def __init__(self):
        #self.grid_size = [5,5]
        self.current_grid = []
    
    def get_neighbour_count(self, down, right):
        blocks = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        neighbour_count = 0
        for direction in blocks:
            temp_right = right + direction[0]
            temp_down = down + direction[1]
            value = self.get_value(temp_down, temp_right)
            if value:
                neighbour_count += 1
        return neighbour_count
            
    def get_value(self, down, right):
        down_length = len(self.current_grid)
        right_length = len(self.current_grid[0])
        return self.current_grid[down%down_length-1][right%right_length-1]
    
    def next_state(self, neighbours, current_state):
        n = neighbours
        if current_state == 1:
            #alive
            if n < 2:
                return 0
            if ((n==2) + (n==3)):
                return 1
            if n>3:
                return 0
        
        if current_state == 0:
            if n==3:
                return 1
            else:
                return 0
            
    def next_grid(self):
        temp_grid = []
        down_length = len(self.current_grid)
        right_length = len(self.current_grid[0])
        for down_pos in range(1, down_length + 1):
            temp_row = []
            for right_pos in range(1, right_length + 1):
                current_state = self.get_value(down_pos, right_pos)
                neigh_count = self.get_neighbour_count(down_pos, right_pos)
                my_next_state = self.next_state(neigh_count, current_state)
                temp_row.append(my_next_state)
            temp_grid.append(temp_row)
        self.current_grid = temp_grid
        