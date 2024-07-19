#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:22:58 2024

@author: chuksokoli

This is an implementation of the Linkedlist in Python
"""

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

# Create a LinkedList instance
linked_list = LinkedList()

# Insert nodes into the linked list
linked_list.insert_beginning(3)
linked_list.insert_beginning(2)
linked_list.insert_beginning(1)

# Print the string representation of the linked list
print("Linked List:")
print(linked_list.stringify_list())

# Remove a node from the linked list
linked_list.remove_node(2)

# Print the string representation of the linked list after removal
print("\nLinked List after removing '2':")
print(linked_list.stringify_list())