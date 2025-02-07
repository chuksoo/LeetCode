class Solution:
    def reverseWords(self, s: str) -> str:
        # Brute Force - Step 1
        # sentence = s.split(' ')
        # reversed_word = [item[::-1] for item in sentence]
        # return " ".join(reversed_word)
        
        # Method 2 - List comprehension
        # return " ".join([item[::-1] for item in s.split(' ')])

        # Method 3 - Two Pointer
        result = ''
        split_words = s.split()
        for word in split_words:
            reversed_str = reverse_string(word)
            result = result + reversed_str + " "
        result = result.strip()
        return result

def reverse_string(strg):
    char_list = list(strg)
    start = 0
    end = len(char_list) - 1
    while start <= end:
        char_list[start], char_list[end] = char_list[end], char_list[start]
        start += 1
        end -= 1
    return "".join(char_list)

    

        