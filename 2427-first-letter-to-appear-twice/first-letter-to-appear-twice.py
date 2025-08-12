class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_map = {}
        for char in s:
            if char not in char_map:
                char_map[char] = 1
            else:
                return char

        