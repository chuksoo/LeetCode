**Linear Search**
This method requires us to go through all the possibilities to find a solution to the problem we want to solve. For instance, if we have a list of integers and we want to find the minimum, maximum, or a certain element in that list, the Brute Force approach requires us to go through all the elements to find that specific element.


- Example: linear search
Linear/Sequential Search is a method for finding a target value within a given list. It sequentially checks each element of the list for the target value until a match is found or all the elements have been searched. Linear Search runs in linear time (at its worst) and makes `n` comparisons (at most), where `n` is the length of the list.

Let’s assume that we are given the following list of unsorted integers.

```python
lst = [2, 4, 6, 3, 5, 7, 9, 1, 8]
```
Now, we can be asked to find a certain element in the list and return true if the element exists. To search the list using a brute force exhaustive search technique, we traverse the whole length of the list until the element is found.

That element exists at any particular index value. If we modify the above task, such that, if we want to find the index of the specified number and then extend it further that we don’t specify the number but find the index of the maximum or minimum value present in the list, the brute force approach will let you traverse the entire list. Here is what the code for this would look like - see find.py, maximum.py, minimum.py.

*Time complexity: O(n)* - We would have to do n comparisons in the worst case if the element we want to find is present on the last index of the array.

**Advantages**
The good thing about the Brute Force method is that, if a solution to our problem exists, we are guaranteed to find the solution this way. Once we have a way to go about solving the problem, we can focus on making the solution more efficient.

**Disadvantages**
Even though it might be the first solution that pops up into our heads, it is the most inefficient one. Also, there are no shortcuts and no performance improvements at this stage.