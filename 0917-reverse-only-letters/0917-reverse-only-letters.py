class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        num_lst = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if not num_lst[left].isalpha():
                left += 1
            elif not num_lst[right].isalpha():
                right -= 1
            else:
                num_lst[left], num_lst[right] = num_lst[right], num_lst[left]
                left += 1
                right -= 1
        return "".join(num_lst)
        
