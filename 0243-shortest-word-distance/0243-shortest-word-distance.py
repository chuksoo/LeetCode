class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ptr1 = ptr2 = min_distance = float('inf')
        for index, item in enumerate(wordsDict):
            if word1 == word2 or wordsDict == []:
                return -1
            if item == word1:
                ptr1 = index
            elif item == word2:
                ptr2 = index
            min_distance = min(abs(ptr1 - ptr2), min_distance)
        return min_distance
                
        