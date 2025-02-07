class Solution:
    def reverseWords(self, s: str) -> str:
        # sentence = s.split(' ')
        # reversed_word = [item[::-1] for item in sentence]
        # return " ".join(reversed_word)
        
        return " ".join([item[::-1] for item in s.split(' ')])

    

        