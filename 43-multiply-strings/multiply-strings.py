class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_val1 = int_val2 = 0
        for char1 in num1:
            int_val1 = int_val1 * 10 + (ord(char1) - ord('0'))
        for char2 in num2:
            int_val2 = int_val2 * 10 + (ord(char2) - ord('0'))
        return str(int_val1 * int_val2)


        