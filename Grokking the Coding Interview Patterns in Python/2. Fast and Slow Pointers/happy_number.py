"""
Write an algorithm to determine if a number `n` is a happy number. We use the following process to check if a given number is a happy number:
- Starting with the given number `n`, replace the number with the sum of the squares of its digits.
- Repeat the process until:
    + The number equals 1 which will depict that the given number `n` is a happy number.
    + The number enters a cycle, which will depict that the given number `n` is not a happy number.
Return TRUE if `n` is a happy number, and FALSE if not.
"""
def isHappy(n):
    def sum_of_squared_digits(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum
    slow = n
    fast = sum_of_squared_digits(n)
    while fast != 1 and slow != fast:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
    if (fast == 1):
        return True
    return False

# Example usage:
def main():
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(i+1, ".", "\tInput Number:", inputs[i], sep="")
        result = isHappy(inputs[i])
        print("\tIs Happy Number:", result)
        print("-" * 100)


if __name__ == '__main__':
    main()