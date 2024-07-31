# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
             return 0
            
        answer = 0
        current = head
        while current:
            answer = 2 * answer + current.val
            current = current.next
        return answer
            
        