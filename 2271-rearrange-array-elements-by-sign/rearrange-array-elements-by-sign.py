class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        from collections import deque
        result = []
        pos_queue = deque()
        neg_queue = deque()
        for num in nums:
            if num > 0:
                pos_queue.append(num)
            else:
                neg_queue.append(num)

        while pos_queue and neg_queue:
            result.append(pos_queue.popleft())
            result.append(neg_queue.popleft())
        return result

        