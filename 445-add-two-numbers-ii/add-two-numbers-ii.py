# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create stack for storing values
        s1 = []
        s2 = []

        # append to stack
        while l1 is not None:
            s1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        res = None

        while s1 or s2 or carry:
            total = carry
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            
            # create new node for current digit
            new_node = ListNode(total % 10)
            new_node.next = res
            res = new_node

            carry = total // 10 
        return res



        