Problem A
------------
Given a Binary tree (Not binary Search Tree ), find the inorder successor of a node.

inorder: left, mid, right

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

Idea
------
If current node has right child, then it will be left most leave of the right child
otherwise, it will be its parent 

```
public TreeNode inOrderSuccessor(TreeNode root, TreeNode n) {

	if(root == n){
		return getLeftMost(root.right)
	}

	tryLeft = inOrderSuccessor(root.left == n ? root : root.left, n)
	if(tryLeft == null)
		return inOrderSuccessOr(root.right == n ? root : root.right, n)
}


public TreeNode findSuccessor(TreeNode parent, TreeNode n) {
	if(parent == null || n == null)
		return null
	if(n.right == null)
		return getLeftMost(parent)
	else
		return parent
}
```

Problem B
-----------
there is a bunch of tasks, each have different time to complete, task is independent, and then there are some workers, 
How to allocate tasks to these workers to minimize the total time to complete all the task. The tasks can be randomly picked from the task list. 
Example 
Task: 2,2,3,7, 1 
Worker: 2. 
Return 8, because the first worker can work on the first three tasks : 2 + 2 + 3 = 7, and the second worker can work on the last two tasks : 7 + 1 = 8, so the total time to finish all the task is 8. 
public int getMini(int[] tasks, int k)

Idea
--------
Very similar to Dijkstra's algorithm, sort times by reverse length, and increase the next available time

```
public int getMini(vector<int> tasks, int k) {
sort(tasks, tasks+n);
reverse(tasks.begin(), tasks.end())

int maxFinish= 0;
priority_queue<PII> finishT
LP(i, 0, k){
	finishT.insert(PII(i, 0))	
}

LP(i, 0, tasks.size()){
	PII nextAvailable = finisT.top()
	finishT.pop()

	int nextFinishTime =  -nextAvailable.first + tasks[i];
	maxFinish = max(maxFinish, nextFinishTime);
	finishT.push_back(PII(-nextFinishTime, nextAvailable.first));
}

return maxFinish;

}

```


Problem C
------------
Check if two given binary trees(expression trees with two characters 'a' and 'b' and obviously operators like +,-,*) are mathematically equivalent?

Idea
-------
What does matematically equivalent mean? Evaluates to the same value, or write out to the same formula?

If it is first, then it becomes a eval task, which is non-trivial given operators

If it means write out to the same formula, then that means translate the tree into formula in a layout neutral way, and the answer shoudl be same,i.e,when there is only +,-, justgiven an inorder traversal to see the final layout is the same 

When there is *, we need to keep track of the toplevel formula has + in it, if there is, then we need to add brackets



Problem D
----------
Given a large MxN matrix of 1s and 0s like this:


1 1 0 0 1 0 1
1 0 1 0 0 1 1
0 1 1 1 0 1 0
...
Calculate the number of 1s in a given subset PxQ matrix. In effect, write a function:


int ones(int startx, int starty, int len, int width);
Looking for something better than O(n^2).

Idea
-------
Another vague problem, very hard to do less than O(n^2) without pre-computation, which I belive is what the problem meant


