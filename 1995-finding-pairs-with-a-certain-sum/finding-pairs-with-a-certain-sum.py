class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_freq = {}
        for num in self.nums2:
            if num in self.nums2_freq:
                self.nums2_freq[num] += 1
            else:
                self.nums2_freq[num] = 1        

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2_freq[old_val] -= 1
        if self.nums2_freq[old_val] == 0:
            del self.nums2_freq[old_val]

        self.nums2[index] += val
        new_val = self.nums2[index]
        if new_val in self.nums2_freq:
            self.nums2_freq[new_val] += 1       
        else:
            self.nums2_freq[new_val] = 1 

    def count(self, tot: int) -> int:
        total_pairs = 0
        for num in self.nums1:
            required = tot - num
            if required in self.nums2_freq:
                total_pairs += self.nums2_freq[required]
        return total_pairs       


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)