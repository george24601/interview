Problem A
-----------
For a string chemical formula like “C6H2(NO2)3CH3”, and output a map with key as element and value as its count. 
element can have two chars, for example Fe2(SO4)3 
public HashMap<Character, Integer> getCount(String chemicals){ 
}

Problem B
-----------
```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
Find if a given binary tree has duplicate sub trees. 
followup: 
Find all duplicate subtrees in a binary tree


For example,

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, return [ [2,4], [4] ].
````

Problem C
----------
Given a Calendar class (there are three fields, year, month, day) and a number of N, 
Implement a function that returns the calendar after N days, 
For example, if the input is {2017, 3,20} and 12, then the return is {2017,4, 1}


Problem D
-----------
/** 
Given many coins of 3 different face values, print the combination sums of the coins up to 1000. Must be printed in order. 

eg: coins(10, 15, 55) 
print: 
10 
15 
20 
25 
30 
. 
. 
. 
1000 
*/




