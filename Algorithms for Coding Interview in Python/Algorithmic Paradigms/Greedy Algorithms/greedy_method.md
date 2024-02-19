**Greedy method**

Greedy is an **algorithmic paradigm** that builds up a solution, piece by piece. This means it chooses the next piece that offers the most obvious and immediate benefit. A Greedy algorithm, as the name implies, always makes the choice that seems to be the best at the time. It makes a *locally-optimal* choice in the hope that it will lead to a *globally optimal* solution.

The Greedy method can solve a problem that satisfies the below-mentioned properties:

1. *Greedy choice property*: A global optimum can be arrived at by selecting a local optimum.
2. *Optimal substructure*: An optimal solution to the complete problem contains an optimal solution to subproblems.
Greedy algorithms work by recursively constructing a set of pieces from the smallest possible constituent parts.

**Advantages**

The advantage of using a greedy algorithm is that solutions to smaller instances of the problem can be straightforward and easy to understand. Also, it works in some cases, especially where the **optimal solution of the subset is the solution for the superset** as well.

**Disadvantages**

The disadvantage of the greedy algorithm is that sometimes the most optimal **short-term solutions may lead to the worst possible solution to the whole problem!**