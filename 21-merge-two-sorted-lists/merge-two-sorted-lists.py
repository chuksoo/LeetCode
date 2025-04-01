# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is None and list2 is not None:
        #     return list2
        # elif list1 is not None and list2 is None:
        #     return list1

        # dummy_node = ListNode(0)
        # current = dummy_node

        # while list1 is not None and list2 is not None:
        #     if list1.val <= list2.val:
        #         current.next = list1
        #         list1 = list1.next                
        #     else:
        #         current.next = list2
        #         list2 = list2.next 
        #     current = current.next
        
        # # attach any remaining node        
        # if list1 is not None:
        #     current.next = list1
        # else:
        #     current.next = list2            
        # return dummy_node.next

    #def merge_timelines(list1, list2):
        if list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        
        merged_node = ListNode(0)
        merged = merged_node

        node_one = list1
        node_two = list2
        while node_one and node_two:
            if node_one.val <= node_two.val:
                merged.next = node_one
                node_one = node_one.next
            else:
                merged.next = node_two
                node_two = node_two.next
            merged = merged.next
        
        if node_one is not None:
            merged.next = node_one
        else:
            merged.next = node_two
        return merged_node.next

        