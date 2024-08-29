"""
Given a list of integers, lst, find the minimum value from the list.
"""
def find_minimum(lst):
    """
    Time complexity: O(n), where n is the number of elements in the list.
    Space complexity: O(1), as we are only using a constant amount of extra space.
    """
    # base case:
    if not lst:
        return -1
    
    min_value = lst[0]
    # iterate through the list and update min_value
    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
    return min_value

# Driver code
def main():

    inputs = [
        [],
        [9],
        [-1, -5, -10, -2, -4],
        [4, 3, 2, 1],
        [2, 3, 3, -1, -1],
        [100, 50, 75, 25, 400]
            
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tMinimum element: ", find_minimum(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()