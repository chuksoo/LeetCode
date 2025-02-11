class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # One Pass - Time: O(N), Space: O(N)
        # prefix_sum = [0]
        # for num in gain:
        #     prefix_sum.append(num + prefix_sum[-1])
        # return max(prefix_sum)

        # Simple, faster approach - Time: O(N), Space: O(1)
        max_altitude = 0
        current_altitude = 0
        for num in gain:
            current_altitude += num
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude
        