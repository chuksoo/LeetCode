class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # initialize empty string to store result        
        result = ''
        # iterate thru in 2k steps
        for i in range(0, len(s), 2*k):
            # get end index
            end = min(i + k, len(s))
            # reverse the substring from i to end and append to result
            reversed_substring = reverse_Substring(s, i, end)
            result += reversed_substring

            # Append the remaining chunk
            remaining_start = end
            remaining_end = min(i + 2*k, len(s))
            result += s[remaining_start:remaining_end]
        return result

def reverse_Substring(str_, start, end):
    char_list = list(str_[start:end])
    left = 0
    right = len(char_list) - 1
    while left <= right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return "".join(char_list)        