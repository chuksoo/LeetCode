class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_lst = [i.lower() for i in s if i.isalnum()]
        left = 0
        right = len(new_lst) - 1 
        print(new_lst)
        while left < right:
            if new_lst[left] != new_lst[right]:
                return False
            left += 1
            right -= 1
        return True
            
        