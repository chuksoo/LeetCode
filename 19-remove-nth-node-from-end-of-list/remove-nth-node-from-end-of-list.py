# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialize slow and fast at the head of node
        slow, fast = head, head
        # return nothing is we only have one head
        if not fast.next:
            return 
        # move fast n steps ahead
        for i in range(n):
            fast = fast.next
        # if fast reaches NULL, return the head
        if not fast:
            return head.next
        # otherwise, move fast until it reaches the end
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # update slow.next to point to slow.next.next
        slow.next = slow.next.next
        # return head
        return head
        