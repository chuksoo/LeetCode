#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:38:48 2024

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
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True       
    
def delete_at_head(lst):
    # Get Head and firstElement of List
    first_element = lst.get_head()

    # if List is not empty then link head to the
    # nextElement of firstElement.
    if first_element is not None:
        lst.head_node = first_element.next_element
        first_element.next_element = None
    return


lst = LinkedList()
for i in range(11):
    lst.insert_at_head(i)

lst.print_list()

delete_at_head(lst)
delete_at_head(lst)

lst.print_list()