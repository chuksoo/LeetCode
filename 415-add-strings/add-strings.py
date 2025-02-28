class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry > 0:
            digit1 = num1[i] if i >= 0 else '0'
            digit2 = num2[j] if j >= 0 else '0'

            # convert character to integer
            int_digit1 = ord(digit1) - ord('0')
            int_digit2 = ord(digit2) - ord('0')

            # compute sum with carry
            total_sum = int_digit1 + int_digit2 + carry
            carry = total_sum // 10
            last_digit = total_sum % 10

            result.append(str(last_digit))
            i -= 1
            j -= 1
        return ''.join(result[::-1])


        