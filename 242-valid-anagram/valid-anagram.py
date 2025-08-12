class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        if len(s) != len(t):
            return False

        s_freq = Counter(s)
        t_freq = Counter(t)
        return s_freq == t_freq

        

        