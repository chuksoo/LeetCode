class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 0:
            if n == 1:
                return True

            n, r = divmod(n, 4)
            if r > 0:
                return False
        