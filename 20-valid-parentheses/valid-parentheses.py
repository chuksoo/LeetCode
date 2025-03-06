class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # if char is an opening bracket, push it to stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                # if stack is empty, return False
                if not stack:
                    return False

                if (char == ')' and stack[-1] == '(') or \
                    (char == '}' and stack[-1] == '{') or \
                    (char == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
                
        