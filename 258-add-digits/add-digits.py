class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum_num = 0
            while num > 0:
                num, remainder = divmod(num, 10)
                sum_num += remainder
            num = sum_num
        return num
      
                

        