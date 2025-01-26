class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [] # list to store the maximum values for each window
        queue = collections.deque() # deque to store indices of elements within the current window
        
        # Iterate over each element in the input array by its index
        for i in range(len(nums)):
            # Remove indices of elements that are out of the current window
            # If the index at the front of the deque is less than or equal to (i - k), remove it
            while queue and queue[0] <= i - k:
                queue.popleft()
            
            # Remove indices of elements from the back of the deque
            # These elements are smaller than or equal to the current element nums[i],
            # as they cannot be the maximum of the current or any future window
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            
            # Add the current index to the deque
            # It is a candidate for being the maximum of the current or future windows
            queue.append(i)
            
            # Once the first window of size k is fully processed (i >= k - 1),
            # the maximum value of the window is at the front of the deque
            if i >= k - 1:
                output.append(nums[queue[0]])

        # Return the list of maximum values for each sliding window
        return output


        