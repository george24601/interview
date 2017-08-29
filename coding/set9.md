Problem A
----------
How do you verify a search result list which changes consistently based on each search word and filters? 

For example, how do you make sure that the list is sorted based on price or rating or etc without any identical list to compare with? Since providing an identical list as Test Input for each word is not the best approach.


Problem B
----------
```
Print first pair of mis-matching leaves (first pair as in in-order) given two pre-order traversal arrays of BSTs. 

e.g.


For
                  5
              4      8
            2  4    6  9
            Pre-order Sequence as [5,4,2,4,8,6,9]
                &
                  5
              3     8
            2  4   7  9
            Pre-order Sequence2 as [5,3,2,4,8,7,9]
            Print “4, 3”.

What if they are binary tree instead of BST
```

Problem C
-----------
Define amazing number as: its value is less than or equal to its index. Given a circular array, find the starting position, such that the total number of amazing numbers in the array is maximized. 
Example 1: 0, 1, 2, 3 
Ouptut: 0. When starting point at position 0, all the elements in the array are equal to its index. So all the numbers are amazing number. 
Example 2: 1, 0 , 0 
Output: 1. When starting point at position 1, the array becomes 0, 0, 1. All the elements are amazing number. 
If there are multiple positions, return the smallest one. 

should get a solution with time complexity less than O(N^2)


Problem D
-----------

