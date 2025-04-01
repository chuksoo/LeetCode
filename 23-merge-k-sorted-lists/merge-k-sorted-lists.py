# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        count = 0
        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, (lst.val, count, lst))
                count += 1
        
        dummy = ListNode(0)
        current = dummy

        while minHeap:
            value, _, min_node = heapq.heappop(minHeap)

            current.next = min_node
            current = current.next

            if min_node.next is not None:
                heapq.heappush(minHeap, (min_node.next.val, count, min_node.next))
                count += 1
        return dummy.next
        