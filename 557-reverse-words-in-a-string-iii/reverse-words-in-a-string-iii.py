class Solution:
    def reverseWords(self, s: str) -> str:
        # Brute Force - Step 1
        # sentence = s.split(' ')
        # reversed_word = [item[::-1] for item in sentence]
        # return " ".join(reversed_word)
        
        # Method 2 - List comprehension
        return " ".join([item[::-1] for item in s.split(' ')])

        # Method 3 - Two Pointer
#         new_str = ''
#         for i, item in enumerate(s.split(' ')):

#             new_str += reverse_string(item.split())
#         return new_str



# def reverse_string(strg):
#     start = 0
#     end = len(strg) - 1
#     while start <= end:
#         strg[start], strg[end] = strg[end], strg[start]
#         start += 1
#         end -= 1

    

        