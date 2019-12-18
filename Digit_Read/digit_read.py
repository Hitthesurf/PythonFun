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
        num_matrix = len(self.mywieghts3D)
        save_lines = []
        for m in range(0,num_matrix):
            height = len(self.mywieghts3D[m])
            for i in range(0, height):
                save_lines.append(','.join(
                        str(q) for q in self.mywieghts3D[m][i]))
            save_lines.append("E")
        my_file = open(self.file_location, 'w')
        for line in save_lines:
            my_file.write(line + '\n')
        my_file.close()
        
    def read_wieghts(self):
        self.mywieghts3D = [[]]
        my_file = open(self.file_location, 'r')
        wieghts_matrix_counter = 0
        for saved_lines in my_file:
            if saved_lines[0] == "E":
                wieghts_matrix_counter += 1
                self.mywieghts3D.append([])
            else:
                temp_line = saved_lines.split(',')
                for i in range(0,len(temp_line)):
                    temp_line[i] = float(temp_line[i])
                self.mywieghts3D[wieghts_matrix_counter].append(temp_line)
        self.mywieghts3D.pop(-1) #As E on last line
        my_file.close()   
           
    def make_network(self, num_nodes_in_layer, value):
        num_wieght_layers = len(num_nodes_in_layer)-1
        self.mywieghts3D = []
        for i in range(0, num_wieght_layers):
            width = num_nodes_in_layer[i+1]
            hieght = num_nodes_in_layer[i]+1
            temp_matrix = []
            #fill temp matrix
            row_in_matrix = []
            for k in range(0, width):
                row_in_matrix.append(value)
            for k in range(0, hieght):
                temp_matrix.append(row_in_matrix)
            self.mywieghts3D.append(temp_matrix)
    
