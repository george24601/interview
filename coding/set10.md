Problem A
------------
Given a set of numbers {x1, x2, x3, x4, ..., xN} (N>=3) a set of its pairwise sums is {x1+x2, x1+x3, x1+x4, x2+x3,x2+x4,x3+x4, ...,}. (That is s_k = x_i + x_j where i != j) 
Restore a set of numbers given a set of its pairwise sums. 
Note: you don't know given some k, to which i and j it refers, (i.e. input is given in undefined order) 

Example:


S = {1, 5, 10, 100} (n elements)
P = {6, 11, 101, 15, 105, 110} (n * (n - 1) / 2 elements)
Given P you have to restore S. 
Note here means that if you knew which element in P corresponded to which pair of indices in S, you could just solve a simple linear equation


x1+x2=a{k1} x2+x3 = a{k2}, ...., x{n-1} + x{n} = a{k{n-1}, x{n} + x1 = a{k{n}}


Problem B
-----------
Given a vector/list of doubly linked list pointers (a pointer is the directed linkage of two nodes), count how many independent blocks of linked lists there are for the pointers given.

Problem C
---------
As an input, you have points on a 2D graph. You aim to find a straight line that can fit as my points as possible. Return, the maximum number of points you can fit. # of points <= 2200


Problem D
--------
Find the length of longest arithmetic progression in array. 

For example, in the array {1, 6, 3, 5, 9, 7}, the longest arithmetic sequence is 1, 3, 5, and 7
