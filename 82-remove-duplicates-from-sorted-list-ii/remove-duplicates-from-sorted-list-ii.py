# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst_stack = []
        current = head
        res = None
        popped = None

        while current is not None:
            if lst_stack and lst_stack[-1] == current.val:
                popped = lst_stack.pop()
            else:
                lst_stack.append(current.val)
                if lst_stack[-1] == popped:
                    lst_stack.pop()
            current = current.next
        
        while lst_stack:
            new_node = ListNode(lst_stack.pop())
            new_node.next = res
            res = new_node
        return res
            



        