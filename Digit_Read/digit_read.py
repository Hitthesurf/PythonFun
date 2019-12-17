#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:31:46 2019

@author: pi
"""
import math_functions as MathFunctions

class Digit:
    def __init__(self):
        self.mymath = MathFunctions.MathFunction()
        self.mywieghts3D = [[[]]]
        self.file_location = "my_wieghts.txt"
    
    def calc_next_layer(self, in_vector, wieghts):
        #weights are a matrix len(in_vector)+1 x len(output)
        #Add 1 for bias node at start
        in_vector[0].insert(0,1)
        next_layer = self.mymath.mult(in_vector, wieghts)
        next_layer = self.mymath.sigmoid(next_layer)
        return next_layer
    
    def save_wieghts(self):
        pass
    
    def read_wieghts(self):
        pass
    
