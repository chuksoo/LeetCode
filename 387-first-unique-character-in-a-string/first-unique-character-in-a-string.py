class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        char_dict = Counter(s)
        for i, char in enumerate(s):
            if char_dict[char] == 1:
                return i
        return -1

        