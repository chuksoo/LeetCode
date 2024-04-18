
def factorial(n):
    print("factorial called with n = ", str(n))
    if n == 0 or n == 1:
        print("Ending condition met.")
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    n = 5
    print(factorial(n))