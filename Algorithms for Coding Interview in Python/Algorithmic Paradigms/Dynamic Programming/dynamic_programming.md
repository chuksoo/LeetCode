**What is dynamic programming?**
Dynamic programming algorithms solve problems by combining results of subproblems— just like divide and conquer algorithms.

**Characteristics**
1. **Overlapping Subproblems**: the subproblems of a given problem are not independent. In other words, two subproblems share a problem.

2. **Optimal Substructure Property**: the overall optimal solution of the problem can be constructed from the optimal solutions of its subproblems.

**Dynamic programming patterns**
There are two approaches which come in handy when a problem is to be solved using dynamic programming:

*Memoization (top-down)*
The memoized version of a problem is similar to the regular recursive version, except that it looks for the answer of a subproblem in a lookup table before computing its solution.

*Tabulation (bottom-up)*
Tabulation is the opposite of the top-down approach and it avoids recursion. In this approach, we solve the problem ``bottom-up''. This is typically done by filling up a lookup table and computing the solution to the top/original problem based on the results in the table.

**Advantages**
- Being a recursive programming technique, it **reduces the lines of code**.
- It **speeds up the processing**, as we use the answer of a previously-calculated subproblem to get the next one.

**Disadvantages**
- It takes a **lot of memory to store the calculated result of every subproblem** without ensuring if the stored value will be utilized or not, which leads to unnecessary memory utilization.
- There is **no general form** for problems solved by dynamic programming, i.e., every problem has to be solved in its own way.