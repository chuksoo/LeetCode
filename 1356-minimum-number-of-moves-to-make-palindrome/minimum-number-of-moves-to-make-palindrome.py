class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # convert string to list 
        chars = list(s)
        # counter for number of moves needed
        moves = 0
        # initialize two pointers for start and end of string
        left, right = 0, len(chars) - 1
        # keep track of original right position when finding matches
        end_index = right 
        # track position of single character (if any) that needs to be moved to center
        center_index = -1 
        while left < right:
            # if characters at ends match, move forward
            if chars[left] == chars[right]:
                left += 1 
                right -= 1 
                continue
            
            # store current right position before searching for match
            end_index = right
            
            # move right pointer left until we find matching character
            while chars[left] != chars[right]:
                right -= 1
                
            # if right pointer meets left pointer, we've found a character
            # that needs to be in the center of palindrome
            if right == left:
                center_index = left 
                left += 1 
                # reset right pointer to continue processing
                right = end_index 
                continue 
            
            while right != end_index:
                # swap characters
                chars[right], chars[right + 1] = chars[right + 1], chars[right]
                right += 1
                moves += 1 
            
            right -= 1 
            left += 1
        
        if center_index != -1:
            moves += abs(center_index - len(chars) // 2)
        
        return moves        