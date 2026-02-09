"""
Given a string, s, return TRUE if it is a palindrome; otherwise, return FALSE. A phrase is considered a palindrome if it reads the same 
backward as forward after converting all uppercase letters to lowercase and removing any characters that are not letters or numbers. 
Only alphanumeric characters (letters and digits) are taken into account.
"""
def is_palindrome(s):
  if not s:
    return False

  s = s.lower()
  s = ''.join(char for char in s if char.isalnum())

  start = 0
  end = len(s) - 1
  while start < end:
    if s[start] != s[end]:
      return False
    start = start + 1
    end = end - 1
  return True

# Test code
def main():
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("Is it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()