#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:10:04 2024

@author: chuksokoli

You’re given an integer array, arr. Return a resultant array so that res[i] is equal to the product of all 
the elements of arr except arr[i].

Write an algorithm that runs in O(n) time without using the division operation.

Constraints:
- 2 ≤ arr.length ≤ 10**5 
- -30 ≤ arr[i] ≤ 30

The product of any prefix or suffix of arr is guaranteed to fit in a 32-bit integer.
"""

def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    left_product, right_product = 1, 1
    l = 0
    r = n - 1

    while l < n and r > -1:
        res[l] *= left_product
        res[r] *= right_product

        left_product *= nums[l]
        right_product *= nums[r]

        l += 1
        r -= 1
    return res

# Driver code
def main():
    
    inputList = [[1, 5, 10], [3, 5, 0, -3, 1], [7, 8, 9, 10, 11], [2, -4, -8, -11, 11], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5]]
    
    # For each input, print the input and its maximum depth
    for i in range(len(inputList)):
        print (str(i + 1) + '.\tnums:', inputList[i])
        print ('\tres:', product_except_self(inputList[i]))
        print ('-' * 100)

if __name__ == '__main__':
    main()


# Second method
# def product_except_self(arr):
#     n = len(arr)
    
#     # Initialize prefix and suffix arrays
#     prefix = [1] * n
#     suffix = [1] * n
    
#     # Compute prefix products
#     for i in range(1, n):
#         prefix[i] = prefix[i - 1] * arr[i - 1]

#     # Compute suffix products
#     for i in range(n - 2, -1, -1):
#         suffix[i] = suffix[i + 1] * arr[i + 1]

#     # Compute result array
#     res = [prefix[i] * suffix[i] for i in range(n)]
    
#     return res

# # Example usage
# arr = [1, 2, 3, 4]
# print(product_except_self(arr))  # Output: [24, 12, 8, 6]
