#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:33:24 2020

@author: pi
"""

class GameOfLifeGrid:
    def __init__(self):
        self.grid_size = [5,5]
        self.current_grid = []
    
    def get_neighbour_count(self, down, right):
        return 3