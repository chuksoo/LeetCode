#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:32:53 2024

@author: chuksokoli

You’re given an integer array height of length n, and there are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines from the input array that, together with the x-axis, form a container that 
holds as much water as possible. Return the maximum amount of water a container can store.

Note: You may not slant the container.

Constraints:
- n = height.length
- 2 ≤ n ≤ 10**3
- 0 ≤ height[i] ≤ 10**3
"""

def container_with_most_water(height):
    max_area = 0
    start = 0
    end = len(height) - 1

    while start < end:
        width = end - start
        max_area = max(max_area, min(height[start], height[end])*(width))
        if height[start] <= height[end]:
            start += 1
        else:
            end -= 1
    return max_area


# Driver code
def main():
    heights = [
                [1, 8, 6, 2, 5, 4, 8, 3, 7], 
                [20, 30, 9, 69],
                [13, 18, 12, 8],
                [45, 32, 56, 99], [23, 20]
                ]
    index = 1
    for i in heights:
        print(str(index)+".\tHeights: "+str(i))
        print("\n\tMaximum Area: " + str(container_with_most_water(i)))
        index += 1
        print("-" * 100)


if __name__ == "__main__":
    main()