class Solution:
    def clearDigits(self, s: str) -> str:
        # If no digits, return original string
        if not any(c.isdigit() for c in s):
            return s
        
        # Convert to list for easier manipulation
        chars = list(s)
        i = 0
        
        while i < len(chars):
            if chars[i].isdigit():
                # Found a digit, now find closest non-digit to left
                left = i - 1
                while left >= 0 and chars[left].isdigit():
                    left -= 1
                    
                if left >= 0:  # Found a non-digit to left
                    # Remove both characters
                    chars.pop(i)  # Remove digit
                    chars.pop(left)  # Remove non-digit
                    # Reset i to handle shifted positions
                    i = left
                else:
                    # No non-digit found to left, just remove digit
                    chars.pop(i)
                    i = 0  # Reset to start since positions shifted
            else:
                i += 1
                
        return ''.join(chars)
