# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        left, right = 0, len(stack) - 1
        while left <= right:
            if stack[left] != stack[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
        