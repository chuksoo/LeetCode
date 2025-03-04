class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ternary_base = []
        while n > 0:
            n, r = divmod(n, 3)
            ternary_base.append(r)
        return True if 2 not in ternary_base else False


        