class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        new_set = set(sentence)
        return True if len(new_set) == 26 else False
        