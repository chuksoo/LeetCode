class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0]
        for num in gain:
            prefix_sum.append(num + prefix_sum[-1])
        return max(prefix_sum)
        