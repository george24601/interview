Problem A
-----------
Data structure design, N horse races, there are 10 checkpoints, whenever a horse through a check point will produce a (horse number, check point number) message, then design a data structure and algorithm to update the messages and then get the top 3 horse efficiently.

Problem B
--------
Given n, return 1 ^ 2 ^ 3 ^ ... ^ n 
Where ^ is binary xor. 
Note: n is a 64-bit number, and 1<<63 is a valid n for this problem. 

Examples:


>>> reduce(lambda a,b:a^b, [1,2,3])
0
>>> reduce(lambda a,b:a^b, [1,2,3,4])
4
>>> reduce(lambda a,b:a^b, [1,2,3,4,5,6,7])
0
>>> reduce(lambda a,b:a^b, [1,2,3,4,5,6,7,8,9])
1

Problem C
----------
You are given a set of points on x axis (consumers) 
Also you are given a set of points on a plane (producer) 

For every consumer print the nearest producer. 
Wanted something better than O(n^2) time. 

Example: 
consumers: 1 5 7 
producers: (0, 3), (1,1), (3, 2), (8, 10), (9, 100) 

Answer: 
for 1 nearest producer is (1, 1), for 5 nearest is (3, 2), for 7 nearest is (3, 2)

Follow-up question: now both sets are sorted by x coordinate. Could you come up with a linear algorithm?

Problem D
----------
Given integer k and a subset S of set {0, 1, 2, ..., 2^k - 1} 
Return the count of pairs (a, b) where a and b are from S and (a < b) and (a & b == a) 
& here is bit-wise and. 
Do it faster than O((2^k)^2), assume k <= 16 

Example: 
0b111 0b101 
0b010 
Answer: 2 

0b110 
0b011 
0b101 
Answer: 0
