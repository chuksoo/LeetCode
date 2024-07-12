class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_lst = s.strip().split()
        for i in word_lst:
            return len(word_lst[-1])
        