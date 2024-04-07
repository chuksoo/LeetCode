#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:02:03 2023

@author: chuksokoli


Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.

Constraints:
1 ≤ s.length ≤ 2*10^5
The string s will not contain any white space and will only consist of ASCII characters.
"""

def is_palindrome(s):
    if not s:
        return False
    
    s = s.lower()
    s = ''.join(s.strip())
    
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start = start + 1
        end = end - 1
    return True

# Test code
def main():
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("Is it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)
        
if __name__ == "__main__":
    main()
        