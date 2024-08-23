<h3>Time Complexity for list operations</h3>

| **Methods** | **Description** | **Operations** | **Time Complexity** |
|-----------|------------------------------------------------------------------------------|------------------------------------------------------|---|
| append()  | Adds an element at the end of the list                                       | lst = [1, 3, 5, 'seven']                             |  O(1)  |
|           |                                                                              | lst.append(9) # list.append(val) returns [1, 3, 5, 'seven', 9]       | |
| insert()  | Adds an element at the specified position                                    | lst.insert(0, 2) # list.insert(index, val) returns [2, 1, 3, 5, 'seven', 9]  | O(n)  |
| remove()  | Removes the first item with the specified value                              | lst.remove('seven') # list.remove(val) returns [2, 1, 3, 5, 9]        | O(n)  |
| pop()     | Removes the element at the specified position                                | lst.pop(0) # list.pop(index) returns [1, 3, 5, 9]                    | O(n) for arbitrary index, O(1) for last element  |
| clear()   | Removes all the elements from the list                                       |   | O(n)  |
| copy()    | Returns a copy of the list                                                   |   | O(n)  |
| count()   | Returns the number of elements with the specified value                      |   | O(n) |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list | lst.extend([7, 6, 5]) # returns [1, 3, 5, 9, 7, 6, 5]  | O(k)  |
| index()   | Returns the index of the first element with the specified value              |   | O(n)  |
| reverse() | Reverses the order of the list                                               | lst.reverse() # returns [5, 6, 7, 9, 5, 3, 1]  | O(n)  |
| sort()    | Sorts the list                                                               |   | O(n log n)  |
