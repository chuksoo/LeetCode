**Divide and Conquer**

Divide and conquer is an algorithmic paradigm in which the problem is *repeatedly* divided into subproblems until we reach a point where each problem is **similar and atomic** (i.e., can’t be further divided).

**Atomic problem**
Let’s solve a problem in which we have a list of uppercase and lowercase alphabets and the task is to convert it all into lowercase.

In this problem, we will start solving these atomic problems and combining (merging) the solutions. So, Divide and Conquer solutions have the following 3 steps:

**1. Divide**
First, break the problem at hand into smaller subproblems. This step can be achieved by dividing the list containing the alphabets into sublists until a single unit is left and no further division is possible.

**2. Conquer**
Solve the received *atomic* subproblems from step 1. Often, the problems are considered solved and passed onto the next step.

**3. Merge**
Repeatedly combine the solved subproblems to formulate a solution for the original problem.

**Advantages**
It can be **optimal for a general case solution** where the problem is easy to divide, and the subproblem at some level is easy to solve.
It makes **efficient use of memory cache** because, when the problem gets divided into subproblems, it becomes smaller enough to be easily solved in the cache itself.

**Disadvantages**
- It uses a **recursive approach** and the most common issue with recursion is that it is **slow**. Sometimes, it can be more complicated than a basic iterative approach, especially in cases with a large **n**. For example, adding multiple numbers using a simple loop is much simpler and efficient than dividing the numbers into two groups, adding these groups recursively, and then adding the sums of the two groups.

- Since the problem is solved using recursion, it may end up **duplicating some subproblems** and lead to **huge recursive stacks**, which consequently **consumes extra space**.