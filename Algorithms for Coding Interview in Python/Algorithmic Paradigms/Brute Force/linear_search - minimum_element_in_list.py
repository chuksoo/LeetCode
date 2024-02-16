#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 23:09:05 2023

@author: chuksokoli
"""

def minimum_index(lst):
    min_index = -1
    min_value = 9999
    for i in range(len(lst)):
        if min_value > lst[i]:
            min_value = lst[i]
            min_index = i
    return min_index

# Code to test 
if __name__ == "__main__":
    nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]
    min = minimum_index(nums)
    print("Minimum number in the list is", nums[min],
          "at index ", min);     
            