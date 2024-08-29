"""
You’re given an integer array, nums. Return a resultant array product so that product[i] is equal to the product of all the elements of nums except nums[i].
Write an algorithm that runs in O (n) time without using the division operation.
"""

def product_except_self(nums):
    """
    Time complexity: O(n) where n is the number of element in the list
    Space complexity: O(1) because no extra space is used
    """
    # initialization
    n = len(nums)

    # Initialize result array with 1's
    product = [1] * n
    left_product, right_product = 1, 1
    left = 0
    right = len(nums) - 1

    while left < n and right > -1:
        # left calculation
        product[left] *= left_product
        left_product *= nums[left]
        left += 1

        # right calculation
        product[right] *= right_product
        right_product *= nums[right]
        right -= 1
    return product

def main():
    inputs = [
        [1, 2, 3, 4],   
        [5, -3, 1, 2],   
        [2, 2, 2, 0],      
        [0, 0, 0, 0],   
        [-1, -2, -4]   
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tList of products: ", product_except_self(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()