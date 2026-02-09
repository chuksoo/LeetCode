"""
Given a list, nums, and an integer, k, rotate the list to the right by k positions so that each 
rotation involves shifting the elements one position at a time.
"""

def rotate_list(nums, k):
    """
    Time complexity: O(n), where n is the number of elements in the list.
    Space complexity: O(1), as we are only using a constant amount of extra space.
    """
    k %= len(nums)
    return nums[-k:] + nums[:-k]

def main():
    inputs = [
        ([10, 20, 30, 40, 50]),  
        ([1, -2, 3, 4, 5]),  
        ([-1, 90, -90, 4, 6]),      
        ([3, 6, 9, -12]),          
        ([-100, -200, -300])         
    ]
    k= [3, 2, 6, 2, 1]
    
    for i in range(len(inputs)):
        print(i + 1, ".\tnums: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tRotated list: ", rotate_list(inputs[i], k[i]), sep="")
        print("-" * 70)

if __name__ == "__main__":
    main()