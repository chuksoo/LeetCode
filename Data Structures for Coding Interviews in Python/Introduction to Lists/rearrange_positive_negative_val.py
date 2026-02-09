"""
Implement a function that rearranges elements in a list so that all negative elements 
appear to the left and all positive elements (including zero) appear to the right. 
It’s important to note that maintaining the original sorted order of the input list is not required for this task.
"""
def rearrange_positive_negative_val(lst):
    """
    Time complexity: O(n), where n is the length of the input list.
    Space complexity: O(n), where n is the size of the input.
    """
    pos_lst = []
    neg_lst = []
    for i in range(len(lst)):
      if lst[i] < 0:
        neg_lst.append(lst[i])
      else:
        pos_lst.append(lst[i])
    return neg_lst + pos_lst

# Test the function
def main():
    inputs = [[10, 4, 6, 23, 7],
              [-3, 20, -1, 8],
              [2, -5, -4, 43, 2],
              [-3, -10, -19, 21, -17],
              [25, 50, 75, 100, 400]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tResult: ", rearrange_positive_negative_val(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()