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
Suppose you have a 2-D grid. Each point is either land or water. 
There is also a start point and a goal.
There are also keys that open up doors. Each key corresponds to one door. 
Implement a function that returns the shortest path from the start to the 
goal using land tiles, keys and open doors.

Data Representation
The board will be passed as an array of chars.

A board can have the following tiles.
0 = Water 
1 = Land
2 = Start
3 = Goal

uppercase = door
lowercase = key
Example Maps (keys at each step are not required)
`No doors`
char[][] board1 = {{'0', '2', '1', '1', '1'},
				   {'0', '1', '0', '0', '1'},
				   {'0', '1', '0', '0', '3'},
				   {'0', '1', '0', '0', '1'},
				   {'0', '1', '1', '1', '1'}};
path : [0,1]->[0,2]->[0,3]->[0,4]->[1,4]->[2,4]

`One door`
char[][] board2 = {{'0', '2', '1', '1', '1'},
				   {'0', '1', 'a', '0', 'A'},
				   {'0', '1', '0', '0', '3'},
				   {'0', '1', '0', '0', '1'},
				   {'0', '1', '1', '1', '1'}};
path : [0,1]->[0,2]->[1,2]->[0,2]->[0,3]->[0,4]->[1,4]->[2,4]
public List<int[]> solve(char[][] board) {

