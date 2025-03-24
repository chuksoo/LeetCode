class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import heapq

        # heapify data
        heapq.heapify(nums)

        heap_lst = []
        while nums:
            smallest = heapq.heappop(nums)
            heap_lst.append(smallest)
        return heap_lst

        