class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        new_lst = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if not new_lst[left].isalpha():
                left += 1
            elif not new_lst[right].isalpha():
                right -= 1
            else:
                new_lst[left], new_lst[right] = new_lst[right], new_lst[left]
                left += 1
                right -= 1
        return "".join(new_lst)

        