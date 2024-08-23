def remove_even(lst):
    new_lst = []
    # Replace this placeholder return statement with your code
    if not lst:
      return new_lst
      
    for val in lst:
      if val % 2 != 0:
        new_lst.append(val)
    return new_lst

def main():

    inputs = [
            [3, 2, 41, 3, 34],
            [-5, -4, -3, -2, -1],
            [-1, 2, 3, -4, -10],
            [1, 2, 3, 7],
            [2, 4, 6, 8, 10],
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tFinal list: ", remove_even(inputs[i]), sep="")
        print("-" * 40)


if __name__ == "__main__":
    main()