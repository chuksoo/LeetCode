class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_num = 0
        product_num = 1
        while n > 0:
            n, remainder = divmod(n, 10)
            sum_num += remainder
            product_num *= remainder
        return product_num - sum_num
        