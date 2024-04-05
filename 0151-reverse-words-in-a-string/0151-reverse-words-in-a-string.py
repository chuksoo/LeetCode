class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        for val in s.split():
            lst.append(val)
        return " ".join(lst[::-1])
        