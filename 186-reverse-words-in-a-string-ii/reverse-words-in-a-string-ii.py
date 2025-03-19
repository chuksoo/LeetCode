class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse_word(s, 0, len(s) - 1)
        left = 0

        for i in range(0, len(s) - 1):
            if s[i] == " ":
                reverse_word(s, left, i - 1)
                left = i + 1
        # reverse the last word
        reverse_word(s, left, len(s) - 1)
        
def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] =  s[end], s[start]
        start += 1
        end -= 1




            
            


        