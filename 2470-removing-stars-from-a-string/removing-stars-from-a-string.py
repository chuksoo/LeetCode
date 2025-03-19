class Solution:
    def removeStars(self, s: str) -> str:
        star_stack = []
        for char in s:
            if char != '*':
                star_stack.append(char)
            else:
                if len(star_stack) > 0:
                    star_stack.pop()
        return ''.join(star_stack)




        