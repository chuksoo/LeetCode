class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        whole_num = 0
        for digit in digits:
            whole_num = whole_num * 10 + digit
        whole_num += 1
        return [int(x) for x in str(whole_num)]

        