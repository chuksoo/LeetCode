class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 0:
            if n == 1:
                return True

            n, r = divmod(n, 3)
            if r > 0:
                return False
        return True
            # elif r == 0 and n == 1:
            #     return True

        