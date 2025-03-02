class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merge_dict = {item[0]:item[1] for item in nums1}
        for item in nums2:
            if item[0] in merge_dict:
                merge_dict[item[0]] += item[1]
            else:
                merge_dict[item[0]] = item[1]

        return sorted([[k, v] for k, v in merge_dict.items()])
