class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""

    def is_palindrome(self, word: List[str]) -> bool:
        if not word:
            return False
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        