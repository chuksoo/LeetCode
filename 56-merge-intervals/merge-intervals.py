class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_interval = [intervals[0]]
        if not intervals:
            return merged_interval

        for i in range(1, len(intervals)):
            if merged_interval[-1][1] >= intervals[i][0]:
                merged_interval[-1][1] = max(merged_interval[-1][1], intervals[i][1])
            else:
                merged_interval.append(intervals[i])
        return merged_interval

        
        