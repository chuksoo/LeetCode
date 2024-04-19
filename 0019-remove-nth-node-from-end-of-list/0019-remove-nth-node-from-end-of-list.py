# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Calculate the length of the linked list by traversing it
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Calculate the position of the node to be removed
        position = length - n

        # Handle edge case where the head needs to be removed
        if position == 0:
            return head.next

        # Find the node before the target node
        ptr = head
        for _ in range(position - 1):
            ptr = ptr.next

        # Relink the nodes to remove the target node
        ptr.next = ptr.next.next

        return head

        