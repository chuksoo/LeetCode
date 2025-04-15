# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time - O(N), Space - O(N)
        # lst_stack = []
        # current = head
        # res = None
        # popped = None

        # while current is not None:
        #     if lst_stack and lst_stack[-1] == current.val:
        #         popped = lst_stack.pop()
        #     else:
        #         lst_stack.append(current.val)
        #         if lst_stack[-1] == popped:
        #             lst_stack.pop()
        #     current = current.next
        
        # while lst_stack:
        #     new_node = ListNode(lst_stack.pop())
        #     new_node.next = res
        #     res = new_node
        # return res
            
        # Time - O(N), Space - O(1)
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        current = head

        while current is not None:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return dummy.next



        