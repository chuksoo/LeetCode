class Solution:
    def reverseWords(self, s: str) -> str:
        # lst = []
        # for val in s.split():
        #     lst.append(val)
        # return " ".join(lst[::-1])
    
        return " ".join([val for val in s.split()[::-1]])
        #return " ".join(s.split()[::-1])
        