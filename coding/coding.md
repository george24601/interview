### Coding

* i + 1 - len(suffix) = start index of suffix ends at i
* How to make a HashMap ordered without using the linked list? 
* How to find the single linked list's 1/3 point? Use the fast-slow pointer approach
* How to find the min 10 from the 100k numbers
* maximal continous sum from an int array, with both positive and negative numbers
* Given a function return 0,1 at P and 1-P, implement a function that return 0 and 1 with same probability
* 1B URL, each url LT 56B, dedup, memory 4G
* convert BST to a double linked list
* DAT vs trie?
* Use multi-thread to calc how many prime numbers betwenn 1 and 1 mil
* 3 threads to write into the same list 1,2,3, and you need to output 123123, the time is decided by the thread A

1. Write a livelock code example, i.e., dining philosopher problem
2. 1M promo code, how to ensure each user gets only one? click twice will get the same one?
3. 1M line file with purchased good IDs, how to find the top 100 good

2. Find the max and min number out of n numbers. Try to do that with LT 2n comparisions
  * divide and conquer with bands - how to calculate the complexity?
3. Design an implment a conneciton pool 
  * keep working q, idle q, and recycled q
  * Need to encapsulate the original connection
  * May need to create init connection
4. Implment a skip list,need to support insert, delete, find, and find_range
5. Implement a blocking queue with Java, e.g., include wait and notify
1. 5B strings, and ONE 4G RAM box, find the most repeatable strings.
2. Two 10G files, 10 m memory, put the duplicate into the third file 
1. Write an example of mutilpe people racing on the same track. Leave at the same time and record used times
6. Design: use generics to implement LRU. 
  * Can LinkedHashMap, removeEldestEntry() if you are on java (What is DLL type in java?).
* similarly, count how many 1 bits in an integer? how about how many 0 bits in an integer? What if you can use limited storage?

Consider an IM system, how do you design so that the offline party can receive and read the message the next time he is online ?
* What if the offline user(OU) has many friends?
* What if the OU got too many unread messages? 
* Suppose we do pagination, can we reduce the # of pagination ACKs?

6. Design and implement a service interface that round robins between 3 IPs, behind it. Need to consider concurrency case
