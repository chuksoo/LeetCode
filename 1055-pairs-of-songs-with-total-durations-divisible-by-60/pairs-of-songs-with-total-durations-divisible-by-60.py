class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Brute Force - Time: O(N^2), Space: O(N)
        # num_pairs = 0
        # for i in range(len(time)):
        #     for j in range(i+1, len(time)):
        #         num_pairs += (time[i] + time[j]) % 60 == 0
        # return num_pairs

        # Optimize approach
        remainder_count = [0] * 60
        num_pairs = 0
        for num in time:
            remainder = num % 60
            complement = (60 - remainder) % 60
            num_pairs += remainder_count[complement]
            remainder_count[remainder] += 1 
        return num_pairs
        