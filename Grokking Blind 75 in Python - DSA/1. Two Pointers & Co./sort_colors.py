def sort_colors(colors):
    start, current, end = 0, 0, len(colors) - 1
    
    while current <= end:
        if colors[current] == 0:
            if colors[start] != 0:
                colors[start], colors[current] = colors[current], colors[start]
            
            current += 1
            start += 1

        elif colors[current] == 1:
            current += 1

        else:
            if colors[end] != 2:
                colors[current], colors[end] = colors[end], colors[current]

            end -= 1

# Driver code
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        colors=inputs[i]
        print(i + 1, ".\tcolors:", colors)
        sort_colors(colors)
        print("\n\tThe sorted array is:", colors)
        print("-" * 100)

if __name__ == "__main__":
    main()