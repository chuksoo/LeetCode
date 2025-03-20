class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        heap = []
        num_freq = Counter(nums)

        for num, freq in num_freq.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = [num for freq, num in heap]
        return result
        