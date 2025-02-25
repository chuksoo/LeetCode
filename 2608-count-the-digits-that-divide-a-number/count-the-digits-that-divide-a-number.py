class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        new_num = num
        while new_num > 0:
            quotient, remainder = divmod(new_num, 10)
            if num % remainder == 0:
                count += 1
            new_num = quotient
        return count
        