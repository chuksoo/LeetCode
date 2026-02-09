"""
You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:
- Choose array nums1 or nums2 to traverse (from index-0).
- Traverse the current array from left to right.
- If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
The score is defined as the sum of unique values in a valid path.

Return the maximum score you can obtain of all possible valid paths. Since the answer may be too large, return it modulo 10^9 + 7.
"""
def maxSum(nums1, nums2):
    # initialize two pointer and running sums
    i = j = 0
    sum1 = sum2 = 0
    # initialize result array
    result = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sum1 += nums1[i]
            i += 1
        elif nums2[j] < nums1[i]:
            sum2 += nums2[j]
            j += 1
        else: # nums1[i] == nums2[j]:
            max_sums = max(sum1, sum2)
            max_sums += nums1[i]
            result += max_sums
            sum1 = sum2 = 0
            i += 1
            j += 1 
    # handle remaining element in nums1 or nums2
    while i < len(nums1):
        sum1 += nums1[i]
        i += 1

    while j < len(nums2):
        sum2 += nums2[j]   
        j += 1

    # add final segment
    max_sums = max(sum1, sum2)
    result += max_sums

    return result % (10**9 + 7)

# Test code
def main(): 
    test_cases = [
        {
            "nums1": [2,4,5,8,10],
            "nums2": [4,6,8,9]
        },
        {
            "nums1": [1,3,5,7,9],
            "nums2": [3,5,100]
        },
        {
            "nums1": [1,2,3,4,5],
            "nums2": [6,7,8,9,10]
        }
    ]
    for i in range(len(test_cases)):
        nums1 = test_cases[i]["nums1"]
        nums2 = test_cases[i]["nums2"]
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input list is ", nums1, " and ", nums2, ".", sep='')
        print("The maximum sum is.....", maxSum(nums1, nums2))
        print("-" * 100)
 

if __name__ == "__main__":
    main()