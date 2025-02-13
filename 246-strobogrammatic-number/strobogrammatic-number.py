class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # create dictionary mapping
        number_dict = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

        # initialize two pointer
        left, right = 0, len(num) - 1

        # compare digit pointed by pointers
        while left <= right:
            # check if num[left] in dict, if not return False
            # retrieve the expected rotated value of nums[left] - if it doesn't match nums[right], return False
            if num[left] not in number_dict or num[right] != number_dict[num[left]]:
                return False
            # increment left, decrement right
            left += 1
            right -= 1
        # after all iteration, return True
        return True
        