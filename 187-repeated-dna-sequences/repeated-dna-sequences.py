class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # create a set to store unique sequence
        unique_sequence = set()
        # create a set to store repeated sequence
        repeated_sequence = set()
        # iterate through the DNA sequence
        for i in range(0, len(s) - 10 + 1):
            # extract substing of length k
            substring = s[i:i + 10]
            # if substring in unique sequence, add to repeated
            if substring in unique_sequence:
                repeated_sequence.add(substring)
            # else, add to unique
            else:
                unique_sequence.add(substring)
        # return repeated as a list
        return list(repeated_sequence)
        