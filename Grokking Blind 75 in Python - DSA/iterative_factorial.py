
def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1 
        print("Current value of n is ", str(n))
    print("Ending condition met.")
    return result

if __name__ == '__main__':
    n = 5
    print(factorial(n))

