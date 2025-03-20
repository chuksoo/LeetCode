class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        sort_freq = Counter(s)

        result = []
        for item, val in sort_freq.most_common():
            result.append(item * val)
        return ''.join(result)


        