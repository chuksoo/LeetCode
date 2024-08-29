"""
Given a list nums, find the first nonrepeating integer in it.
"""
def find_first_unique(nums):
    """
    Time complexity: O(n), where n is the number of elements in the list.
    Space complexity: O(n), where n is the number of elements in the list.
    """
    # base case
    if not nums:
      return None
    
    # create a dictionary to store the frequency of each number in the list
    dict = {}
    for item in nums:
      if item in dict:
        dict[item] += 1
      else:
        dict[item] = 1
        
    # iterate through the list again and find the first non-repeating number
    for val in nums:
      if val in dict and dict[val] == 1:
        return val
    
# Test Case
def main():
  input = [
    [],
    [11, -11, 22, 33, -33, 11],
    [5, 5, 6, 6, 7],
    [4],
    [1, 2, 3],
    [-9, -10, -10, -11, -11],
    [5, 5, 6, 6, 7, 8, 9, 9],
    [-9, 1, 8, -9, 20, 1, 8]
  ]

  for i in range(len(input)):
    print(i + 1, ".\tInput list: ",  input[i])
    print("\n\tFirst nonrepeating integer: ", find_first_unique(input[i]))
    print("-" * 100)


if __name__ == "__main__":
  main()