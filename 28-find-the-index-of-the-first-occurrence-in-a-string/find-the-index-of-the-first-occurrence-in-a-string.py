class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        