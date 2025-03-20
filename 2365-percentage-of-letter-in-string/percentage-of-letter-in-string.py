class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        left = 0
        n = len(s)
        count = 0
        while left <= n - 1:
            if s[left] == letter:
                count += 1
            left += 1
        return floor(count / n * 100)

        