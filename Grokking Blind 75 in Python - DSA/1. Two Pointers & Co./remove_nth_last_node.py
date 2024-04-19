from linked_list import LinkedList
from print_list import print_list_with_forward_arrow

def remove_nth_last_node(head, n):
    # Two pointers, right and left, are set at the head node
    right = head
    left = head

    # Move the right pointer n steps forward
    for i in range(n):
        right = right.next

    # If right reaches NULL, return head's next node
    if not right:
        return head.next
    
    # Move both right and left pointers forward till right reaches the last node
    while right.next:
        right = right.next
        left = left.next
    
    # Relink the left node to the node at left's next to the next node
    left.next = left.next.next
    # Return head
    return head

# Driver code
def main():
    lists = [[23, 89, 10, 5, 67, 39, 70, 28], [34, 53, 6, 95, 38, 28, 17, 63, 16, 76], [288, 224, 275, 390, 4, 383, 330, 60, 193],
    [1, 2, 3, 4, 5, 6, 7, 8, 9], [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]]
    n = [4, 1, 6, 9, 11]

    for i in range(len(n)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print(i+1, ". Linked List:\t", end='')
        print_list_with_forward_arrow(input_linked_list.head)
        print()
        print("n = ", n[i])
        result = remove_nth_last_node(input_linked_list.head, n[i])
        print("Updated Linked List:\t", end='')
        print_list_with_forward_arrow(result)
        print()
        print("-"*100)

"""
Time complexity: O(n)
Space complexity: O(1)
"""

if __name__ == '__main__':
    main()