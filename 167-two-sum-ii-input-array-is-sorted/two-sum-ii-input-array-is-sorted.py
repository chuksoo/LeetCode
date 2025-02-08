class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return numbers

        # initialize two pointer at start and end of list
        start = 0
        end = len(numbers) - 1
        # initialize empty list
        result = []
        # iterate through and check if number at both end add up to target
        while start <= end:
            # if they do append [start, end] indexes
            two_sums = numbers[start] + numbers[end]
            if two_sums == target:
                result.append(start + 1)
                result.append(end + 1)
                return result
            # if their sum is smaller than target, increase left pointer by 1
            elif two_sums < target:
                start += 1
            # else decrement right pointer by 1
            else:
                end -= 1

        