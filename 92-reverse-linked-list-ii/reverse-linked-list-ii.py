# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # move 'prev' to point to node before sublist to be reversed
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next 

        start = prev.next
        then = start.next 

        # reverse sublist between left and right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        return dummy.next


        