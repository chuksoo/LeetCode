class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_lst = list(s)

        for i, val in enumerate(s_lst):
            if len(stack) > 0 and stack[-1][0] == '(' and val == ')':
                stack.pop()
            elif val == '(' or val == ')':
                stack.append([val, i])
        
        for lst in stack:
            s_lst[lst[1]] = ''
        return ''.join(s_lst)
        