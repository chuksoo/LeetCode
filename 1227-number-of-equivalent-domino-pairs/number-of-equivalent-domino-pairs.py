class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes_count = {}
        total_dominoes = 0
        for dominoe in dominoes:
            dominoe.sort()
            dominoe = tuple(dominoe)

            if dominoe in dominoes_count:
                total_dominoes += dominoes_count[dominoe]
                dominoes_count[dominoe] += 1
            else:
                dominoes_count[dominoe] = 1
        return total_dominoes




        