class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_len, max_word = 0, -inf
        for word in sentences:
            word_len = len(word.split())
            if word_len > max_word:
                max_word = word_len
        return max_word
        