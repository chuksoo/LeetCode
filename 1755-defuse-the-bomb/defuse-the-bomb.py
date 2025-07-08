class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        # base case
        if k == 0:
            return [0] * n
        # extend the list
        extended = code + code
        result = [0] * n
        for i in range(0, n):
            if k > 0:
                result[i] = sum(extended[i+1:i+1+k])
            else:
                result[i] = sum(extended[i+n+k:i+n])
        return result

        
        