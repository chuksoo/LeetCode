class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        return ''.join([x for x in list(s) if x not in vowels])
        