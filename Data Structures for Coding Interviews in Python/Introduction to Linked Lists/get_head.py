#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:55:16 2024

@author: chuksokoli
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node


def main():
    lst = LinkedList()  # Linked List created
    print(lst.get_head())  # Returns None since headNode does not contain any data

"""
Time complexity: O(1)
"""

if __name__ == '__main__':
    main()