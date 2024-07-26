#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:31:01 2024

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
        
def insertNodeAtPosition(head, data, position):
    new_node = Node(data)
    
    # If inserting at the head (position 0)
    if position == 0:
        new_node.next = head
        return new_node
    
    current = head
    current_position = 0
    
    # Traverse to the node just before the desired position
    while current is not None and current_position < position - 1:
        current = current.next
        current_position += 1
    
    # Insert the new node
    new_node.next = current.next
    current.next = new_node
    
    return head

# linked list: 3 -> 8 -> 12 -> 9
num4 = Node(9)
num3 = Node(12, num4)
num2 = Node(8, num3)
num1 = Node(3, num2)
head = num1
print_linked_list(head)
print()
print_linked_list(insertNodeAtPosition(head, 1, 2))