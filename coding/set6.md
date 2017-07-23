Problem A
------------
Given a Binary tree (Not binary Search Tree ), find the inorder successor of a node.

inorder: left, mid, right

if current node has right child, then it will be left most leave of the right child
otherwise, it will be the first right child of its parent


class TreeNode{
    TreeNode left;
    TreeNode right;
     int val;
    public TreeNode(int val){
        this.val = val;
    }
}

public TreeNode inOrderSuccessor(TreeNode root, TreeNode n) {
}

Problem B
-----------
there is a bunch of tasks, each have different time to complete, task is independent, and then there are some workers, 
How to allocate tasks to these workers to minimize the total time to complete all the task. The tasks can be randomly picked from the task list. 
Example 
Task: 2,2,3,7, 1 
Worker: 2. 
Return 8, because the first worker can work on the first three tasks : 2 + 2 + 3 = 7, and the second worker can work on the last two tasks : 7 + 1 = 8, so the total time to finish all the task is 8. 
public int getMini(int[] tasks, int k)


Problem C
------------
Check if two given binary trees(expression trees with two characters 'a' and 'b' and obviously operators like +,-,*) are mathematically equivalent?


Problem D
----------
```
Find all the abbreviations of string:
eg
ABC
SOME Valid abbreviations are :
1BC
2C
3
A1C
AB1
A2
NOT VALID
11C(two numbers cannot occur continuously)
```
