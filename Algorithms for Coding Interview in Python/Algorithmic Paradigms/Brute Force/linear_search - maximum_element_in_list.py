#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:59:34 2023

@author: chuksokoli
"""

def maximum_index(lst):
    # initialize index to 0
    max_index = -1
    # set max value to least number
    max_value = -99999 
    for i in range(len(lst)):
        if max_value < lst[i]:
            max_value = lst[i]
            max_index = i
    
    return max_index

# Code to test above
if __name__ == "__main__":
    
    nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]
    max = maximum_index(nums)
    print("Maximum number in the list is", nums[max],
          "at index ", max);    
            