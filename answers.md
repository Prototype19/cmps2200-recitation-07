# CMPS 2200 Recitation 10## Answers

**Name:** Daron Lebareidam

Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

$W(n) \in O(n+m)$ 

As shown in lectures.

- **4)**

In the worse case, and in all other cases, the number of time that the reachable function will be called is one as the number of times its called is not dependent on the size of the input graph.

- **5)**

$W(n) \in O(2n+m)$

Because the work of the reachable function is $O(n+m)$ and the work of geting all of the keys of the dictionary and turning said list into a set is $O(n)$ so the sum of these two works, since run sequenitally after each other, is $O(2n+m)$

- **7)**

Yes it would change, instead of being $O(n+m)$, the work of the reachable function would be $O(rn)$ where r is the number of nodes reachable from the root nodes and n is the total number of nodes in the graph. The the reachable function would always have to look reach each reachable node r times and for each of these nodes look at n nodes. So the worse case work for this implementation could be $O(n^2)$, or when r=n. Therefore using adjacency matrices will change the reachable function alot.
