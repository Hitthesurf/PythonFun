#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 23:28:44 2019

@author: pi
"""

class MathFunction:
    def __init__(self):
        pass
    
    def mult(self, A, B):
        #nxm for A
        #mxk for B
        n = len(A)
        m = len(A[0])
        k = len(B[0])
        matrix = []
        for i in range(0,n):
            matrix_row = []
            for j in range(0,k):
                c_i_j = 0
                for p in range(0,m):
                    c_i_j += A[i][p]*B[p][j]
                matrix_row.append(c_i_j)
            matrix.append(matrix_row)           
        return matrix