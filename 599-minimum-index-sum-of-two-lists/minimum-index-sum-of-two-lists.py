class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        min_index = float('inf')
        list1_map = {val:i for i, val in enumerate(list1)}
        for j, val in enumerate(list2):
            if val in list1_map:
                index_sum = j + list1_map[val]
                if index_sum < min_index:
                    min_index = index_sum
                    result = [val]
                elif index_sum == min_index:
                    result.append(val)

        return result