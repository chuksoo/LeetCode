#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:15:07 2024

@author: chuksokoli
"""
class Node:
    def __init__(self, value, next = None):
        self.value = value  # Stores data
        self.next = next  # Stores pointer to previous element
        
def print_linked_list(head):
  current = head
  while current is not None:
    print(current.value, end = " -> " if current.next else "")
    current = current.next
  print()
        

def insertNodeAtHead(head, data):
    # Write your code here
    if not head:
        return Node(data)
        
    new_node = Node(data)
    
    current = head
    new_node.next = current
    current = current.next
    return new_node

# linked list: 3 -> 8 -> 12 -> 9
num4 = Node(9)
num3 = Node(12, num4)
num2 = Node(8, num3)
num1 = Node(3, num2)
head = num1
print_linked_list(head)
print()
print_linked_list(insertNodeAtHead(head, 2))