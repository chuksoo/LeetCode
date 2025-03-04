class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digit = 0
        digit = ''.join(str(ord(char) - 96) for char in s)
        digit = int(digit)

        # Transformation
        while k > 0:
            digit = self.get_total_sum(digit)
            k -= 1
        return digit

    # def get_total_sum(self, val):
    #     total_sum = 0
    #     while val != 0:
    #         quotient, remainder = divmod(val, 10)
    #         total_sum += remainder
    #         val = quotient
    #     return total_sum

    def get_total_sum(self, val):
        return sum(map(int, str(val)))