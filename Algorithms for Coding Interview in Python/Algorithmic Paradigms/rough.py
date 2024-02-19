def max_element(lst):
    max_index = -1
    max_val = 99999
    for i in range(len(lst)):
        if max_val > lst[i]:
            max_val = lst[i]
            max_index = i
    return max_val, max_index


if __name__ == '__main__':

    nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]
    print("The lowest value is ", max_element(nums)[0], "located at", max_element(nums)[1])