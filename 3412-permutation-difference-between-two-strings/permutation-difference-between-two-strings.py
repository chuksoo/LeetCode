class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        counter_t = {ch: idx for idx, ch in enumerate(t)}
        per_diff = 0

        for i in range(len(s)):
            per_diff += abs(i - counter_t[s[i]])
        return per_diff
        