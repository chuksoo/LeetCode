class Solution:
    def removeStars(self, s: str) -> str:
        star_stack = []
        for char in s:
            if char != '*':
                star_stack.append(char)
            else:
                if len(star_stack) > 0:
                    star_stack.pop()

        result = ""
        start, end = 0, len(star_stack) - 1
        while start < end:
            star_stack[start], star_stack[end] = star_stack[end], star_stack[start]
            start += 1
            end -= 1

        while star_stack:
            result += star_stack.pop()
        return result




        