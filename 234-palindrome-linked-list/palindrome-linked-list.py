# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_half = self.reverse_linked_list(slow)
        left, right = head, reversed_half
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse_linked_list(self, head):
        current = head
        prev = None
        while current is not None:
            temp_node = current.next # store current's next node
            current.next = prev      # swap nodes
            prev = current           # update previous
            current = temp_node      # update current
        return prev
        