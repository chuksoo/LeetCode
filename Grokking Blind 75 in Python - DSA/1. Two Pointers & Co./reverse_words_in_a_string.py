#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:18:18 2024

@author: chuksokoli

Given a sentence, reverse the order of its words without affecting the order of letters within the given word.

Constraints:

- The sentence contains English uppercase and lowercase letters, digits, and spaces.
- 1 ≤  sentence.length ≤ 10**4
- The order of the letters within a word is not to be reversed.

"""
from typing import List

class Solution:
    def reverse_list(self, lst: List[str], left: int, right: int) -> None:
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1    
            right -= 1

    def reverse_each_word(self, lst: List[str]) -> None:
        n = len(lst)
        start = end = 0
        while start < n:
            while end < n and lst[end] != " ":
                end += 1
            self.reverse_list(lst, start, end - 1) 
            start = end + 1
            end += 1
           
    def reverse_words(self, sentence: str) -> str:
        s = " ".join(sentence.strip().split())
        lst = list(s)
        self.reverse_list(lst, 0, len(lst) - 1)
        self.reverse_each_word(lst)
        return "".join(lst)
    

# Driver code
def main():
    sol = Solution()
    string_to_reverse = ["This is Python Hello World",
                         "a   string   with   multiple   spaces",
                        "Case Sensitive Test 1234",
                        "a 1 b 2 c 3 d 4 e 5",
                        "     trailing spaces",
                        "case test interesting an is this"]

    for sentence in string_to_reverse:
        reversed_sentence = sol.reverse_words(sentence)
        print(reversed_sentence)
        
    
if __name__ == '__main__':
    main()
