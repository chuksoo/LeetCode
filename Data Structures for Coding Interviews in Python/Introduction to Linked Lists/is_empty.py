#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:00:18 2024

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

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False

def main():
    lst = LinkedList()  # Linked List created
    print(lst.is_empty())  # Returns true
    
"""
Time complexity: O(1)
"""

if __name__ == '__main__':
    main()