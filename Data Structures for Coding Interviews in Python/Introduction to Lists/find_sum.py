"""Given a list of integers, nums, and an integer target, k, find two numbers in the list that sum up to the target k.

There is exactly one solution for each input, and each element of the list can only be used once in the solution. 
The order of the returned elements does not matter.
"""


def find_sum(nums, k):
    """
    Time complexity: O(n log n) where n is the number of element in the list and sorting of the list takes O(n log n).
    Space complexity: O(1) because no extra space is used
    """
    result = []
    # base condition: if list is empty, return empty list
    if not nums:
       return result
    
    # sort input list
    nums.sort()
    
    # initialize two-pointer 
    left = 0
    right = len(nums) - 1
    
    # iterate until the pointer meets
    while left <= right:
      
      # calculate sum of current pair
      two_sums = nums[left] + nums[right]

      # if sum is equal to k, add pair to result and break the loop
      if two_sums == k:
        result.append(nums[left])
        result.append(nums[right])
        return result
      
      # if sum is less than k, move left pointer to the right
      elif two_sums < k:
        left += 1
    
      # if sum is greater than k, move right pointer to the left
      else:
        right -= 1
    
# Driver code
def main():
    inputs = [[1, 2, 3, 4],
            [1, 2],
            [2, 2],
            [-4, -1, -9, 1, -7],
            [25, 50, 75, 100, 400]]

    k = [5, 3, 4, -3, 425]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tResult: ", find_sum(inputs[i], k[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()