class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for lst in accounts:
            sum_wealth = sum(lst)
            if sum_wealth > maxWealth:
                maxWealth = sum_wealth
        return maxWealth
        