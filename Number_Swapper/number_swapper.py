#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:10:13 2019

@author: pi
"""
def mult(n):
    num = ["235", "146", "147", "238", "167", "258", "358", "467"]
    start_string = "235"
    n -= 1
    for i in range(0,n):
        temp_string = ""
        for char in start_string:
            temp_string += num[int(char)-1]
        start_string = temp_string
    return start_string

def other_diaganol_side(n):
    paths = mult(n).count("8")
    inverse_chance_per_path = 3**n
    return (paths/inverse_chance_per_path)