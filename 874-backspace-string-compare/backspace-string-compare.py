class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(strg):
            process_str = []
            for char in strg:
                if char != "#":
                    process_str.append(char)
                else:
                    if len(process_str) > 0:
                        process_str.pop()
            return process_str
        return process_string(s) == process_string(t)

        