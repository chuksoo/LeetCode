class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_string = ''
            i = 0
            while i < len(s):
                groupsum = 0
                for ch in s[i:i + k]:
                    groupsum += int(ch)
                next_string += str(groupsum)
                i += k
            s = next_string
        return s

        