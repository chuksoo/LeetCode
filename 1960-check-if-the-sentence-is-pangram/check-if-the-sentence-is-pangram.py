class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        new_str = ''
        for i in sentence:
            if i.isalpha():
                new_str += i
        return len(set(new_str)) == 26
        
        