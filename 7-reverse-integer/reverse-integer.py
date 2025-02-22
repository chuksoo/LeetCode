class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        
        rev_num = 0
        while x > 0:
            digit = x % 10
            x = x // 10
            rev_num = rev_num * 10 + digit

        if isNegative:
            rev_num = -rev_num

        if rev_num < (-2**31) or rev_num > (2**31 - 1):
            return 0

        return rev_num

        