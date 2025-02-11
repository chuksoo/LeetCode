class Solution:
    def reverseWords(self, s: str) -> str:
        # Brute force 
        # lst_sentence = s[::-1].split()
        # reversed_list = [string[::-1] for string in lst_sentence]
        # return " ".join(reversed_list)

        char_lst = list(s)
        n = len(char_lst)
        # reverse entire sentence 
        reverse_words_lst(char_lst, 0, n - 1)

        # reverse each word in place
        left = 0
        right = 0
        while right < len(char_lst):
            if char_lst[right] == ' ':
                reverse_words_lst(char_lst, left, right - 1)
                left = right + 1 
            right = right + 1
        reverse_words_lst(char_lst, left, right - 1)
        
        cleaned_sentence = []
        i = 0
        while i < n:
            while i < n and char_lst[i] == ' ':
                i += 1 
            if i >= n:
                break 
            
            while i < n and char_lst[i] != ' ':
                cleaned_sentence.append(char_lst[i])
                i += 1 
            while i < n and char_lst[i] == ' ':
                i += 1 
            if i < n: 
                cleaned_sentence.append(' ')
            
        return ''.join(cleaned_sentence)        

def reverse_words_lst(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

        