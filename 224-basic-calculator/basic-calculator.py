class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        number = 0

        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            if c in '+-':
                result += number * sign
                sign = -1 if c == '-' else 1
                number = 0
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += number * sign
                pop_sign = stack.pop()
                result *= pop_sign

                pop_val = stack.pop()
                result += pop_val
                number = 0
                
        return result + number * sign

        