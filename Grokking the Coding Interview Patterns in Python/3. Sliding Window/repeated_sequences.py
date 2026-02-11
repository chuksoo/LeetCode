"""
A DNA sequence consists of nucleotides represented by the letters ‘A’, ‘C’, ‘G’, and ‘T’ only. For example, “ACGAATTCCG” is a valid DNA sequence.

Given a string, s, that represents a DNA sequence, return all the 10-letter-long sequences (continuous substrings of exactly 10 characters) 
that appear more than once in s. You can return the output in any order.
"""
def find_repeated_sequences(dna, k):
    seen, repeated = set(), set()
    for i in range(len(dna) - k + 1):
        substring = dna[i:i+k]
        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)
    return list(repeated)

# Example usage:
def main():
    test_cases = [
        "AAAAACCCCC",
        "ACGTACGTAC",
        "GGGGGGGGGG",
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    ]

    for i, s in enumerate(test_cases):
        print(f'{i+1}.\tInput: "{s}"')
        print(f"\n\tEncoded Output: {find_repeated_sequences(s, 10)}")
        print("-" * 100)

if __name__ == "__main__":
    main()


