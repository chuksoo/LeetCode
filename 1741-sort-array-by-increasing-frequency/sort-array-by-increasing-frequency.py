class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        import heapq
        from collections import Counter

        sort_freq = Counter(nums)

        heap = []
        for num, freq in sort_freq.items():
            heapq.heappush(heap, (freq, -num))

        result = []
        while heap:
            freq, num = heapq.heappop(heap)
            num = -num
            result.extend([num] * freq)
        return result

        