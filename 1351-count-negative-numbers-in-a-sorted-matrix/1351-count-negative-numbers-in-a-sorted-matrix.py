class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_num_list = []
        for lst in grid:
            for val in lst:
                if val < 0:
                    neg_num_list.append(val)
        return len(neg_num_list)
        