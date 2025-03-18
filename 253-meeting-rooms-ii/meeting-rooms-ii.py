class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        if not intervals:
            return 0

        # sort by start time
        intervals.sort(key = lambda x: x[0])

        heap = []
        heapq.heappush(heap, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
        return len(heap)

       



        