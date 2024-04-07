#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 04:25:24 2024

@author: chuksokoli

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""


def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # Using Two Pointer
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
    
    # One line solution
    #return s.reverse()
        
# Test code
def main():
    test_cases = [["h","e","l","l","o"], ["H","a","n","n","a","h"]]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string array is: ", test_cases[i])
        print("The output string after reversal is: ", reverseString(test_cases[i]))
        print("-" * 100)
        
if __name__ == "__main__":
    main()