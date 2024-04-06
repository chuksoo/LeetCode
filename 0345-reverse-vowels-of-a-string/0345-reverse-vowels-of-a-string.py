class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_lst = [i for i in s]
        left = 0
        right = len(s_lst) - 1
        while left < right:
            if s_lst[left] in vowels and s_lst[right] in vowels:
                s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
                left += 1
                right -= 1
            elif s_lst[left] in vowels and s_lst[right] not in vowels:
                right -= 1
            elif s_lst[left] not in vowels and s_lst[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s_lst)
            
        
        