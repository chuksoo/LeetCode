#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:54:59 2023

@author: chuksokoli

Given an array of integers, nums, and an integer value, target, determine if 
there are any three integers in nums whose sum is equal to the target, 
that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such 
integers exist in the array. Otherwise, return FALSE.

Constraints:

− 3 ≤ nums.length ≤ 500
− 10^3 ≤ nums[i] ≤ 10^3
− 10^4 ≤ target ≤ 10^4
"""

def find_sum_of_three(nums, target):
    nums.sort()
    
    for i  in range(0, len(nums) - 2):
        low = i + 1
        high = len(nums) - 1
        
        while low < high:
            triplets = nums[i] + nums[low] + nums[high]
            if triplets == target:
                return True
            elif triplets < target:
                low += 1
            else:
                high -= 1
    return False

# Driver code
def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

"""
Time complexity: O(n^2)
Space complexity: O(n)
"""


if __name__ == '__main__':
    main()
        
    