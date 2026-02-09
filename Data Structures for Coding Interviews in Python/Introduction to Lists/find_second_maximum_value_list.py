"""
Given a list of integers, nums, find the second maximum value from the list.
"""

def find_second_maximum(nums):
    """
    Time complexity: O(n), where n is the number of elements in the list.
    Space complexity: O(1), as we are only using a constant amount of extra space.
    """
    if not nums:
      return None
     
    max_val = nums[0]
    second_max_val = -9999 
    for i in range(1, len(nums)):
      if nums[i] > max_val:
        max_val = nums[i]
        
    for i in range(len(nums)):
      if nums[i] > second_max_val and nums[i] != max_val:
        second_max_val = nums[i]
    return second_max_val

# Driver code
def main():
    inputs = [[9, 2, 3, 6],
            [1, 2],
            [-2, 2],
            [-4, -1, -9, 1, -7],
            [25, 50, 75, 100, 100]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\n\tSecond maximum value: ", find_second_maximum(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()