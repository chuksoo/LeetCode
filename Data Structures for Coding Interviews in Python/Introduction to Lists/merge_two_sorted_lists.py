"""
Given two integer lists, nums1 and nums2, of size m and n, respectively, sorted in nondecreasing order. 
Merge nums1 and nums2 into a single list sorted in nondecreasing order.
"""

# def merge_lists(nums1, nums2):
#     """
#     Time complexity: O((n + m) log(n + m)), where n and m are the lengths of nums1 and nums2, respectively.
#     Space complexity: O((n + m) log(n + m)), as we are creating a new list to store the merged elements.
#     """
#     if not nums1:
#         return nums2
    
#     if not nums2:
#         return nums1
  
#     if not nums1 and not nums2:
#         return []
#     return sorted(nums1 + nums2)

def merge_lists(nums1, nums2):
    """
    Time complexity: O(m + n), where m and n are the lengths of nums1 and nums2, respectively.
    Space complexity: O(1), as we are modifying the input lists directly.
    """
    merged_lst = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged_lst.append(nums1[i])
            i += 1
        else:
            merged_lst.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged_lst.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged_lst.append(nums2[j])
        j += 1
    return merged_lst

# Test the function
def main():
    nums1 = [0, 0, 1, 2, 3]
    nums2 = [2, 5, 6]
    print(merge_lists(nums1, nums2))  # Output: [0, 0, 1, 2, 2, 3, 5, 6]

if __name__ == '__main__':
  main()