class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import defaultdict
        count_word = defaultdict(int)

        for word in s1.split():
            count_word[word] += 1
        for word in s2.split():
            count_word[word] += 1
        return [word for word in count_word if count_word[word] == 1]

        