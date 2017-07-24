Problem A
--------
Given a decimal number, write a function that returns its negabinary (i.e. negative 2-base) representation as a string.

assert solution(-15) ==	'110001'
assert solution(2) == '110'
assert solution(13) == '11101'



Problem B
---------
```
Given a binary tree, return all the longest path between any two nodes in a tree. This path may or may not pass through the root. 
Example: 
Given a binary tree


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
          1
         / \
        2   3
       / \     
      4   5  
Return [4,2,1,3] and [5,2,1,3].

Public List<List<Integer>> getLongestPath(TreeNode root) {
        
    }
```


Problem C
----------
Generate a random 4-digit even number : the adjacent 2 digits must be different. 
public int getNumber(){ 
}



Problem D
---------
Having a home-defined linked list with the following structure, where the next will point to the next node in the list and the random will point to a random node in the list (not null). 
Create a copy of the structure (the data field in each node is not unique for different nodes): 

	```
	Example: 
	Having the list: 
	1 -> 2 -> 3 -> X 
	With random pointers to: 
	1: 3 
	2: 2 
	3: 1 

	Create the list: 
	1' -> 2' -> 3' -> X 
	1': 3' 
	2': 2' 
	3': 1' 

	class Node { 
		int data; 
		Node next; 
		Node random; 
	}
```
