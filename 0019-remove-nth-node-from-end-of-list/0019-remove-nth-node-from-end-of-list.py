# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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

    
    # Naive approach
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # Calculate the length of the linked list by traversing it
#         length = 0
#         current = head
#         while current:
#             length += 1
#             current = current.next

#         # Calculate the position of the node to be removed
#         position = length - n

#         # Handle edge case where the head needs to be removed
#         if position == 0:
#             return head.next

#         # Find the node before the target node
#         ptr = head
#         for _ in range(position - 1):
#             ptr = ptr.next

#         # Relink the nodes to remove the target node
#         ptr.next = ptr.next.next

#         return head
        