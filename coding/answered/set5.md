Problem A
--------
Given a decimal number, write a function that returns its negabinary (i.e. negative 2-base) representation as a string.

assert solution(-15) ==	'110001'
assert solution(2) == '110'
assert solution(13) == '11101'

Idea
-----------
-2^0 = 1
-2^1 = -2
-2^2 = 4
-2^3 = -8

so if the number is odd, the last digit is 1, with the number reversed, because all signs will be reversed

```
vector<int> solution(n){
	if (n == 0)
		return vector<int>(); 	
	else if(n == -1)
		return vector<int> (1, 1)
	else{
		vector<int> ans;
		if(n % 2) {
			ans = solution((-n-1)/2)
			ans.push_back(1)
		}else{
			ans = solution(-n/2)
			ans.push_back(0)
		} 

		return ans;
	}
}

string solution(n) {
	vector<int> ans = solution(n)
	
	if (n == 0) {
		return "0";
	}else{
		//translate from int to char here
	}
}
```


Problem B
---------
```
Given a binary tree, return ALL the longest path between any two nodes in a tree. This path may or may not pass through the root. 
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

Idea
-------
Implementation is messy because the requirement to keep track of ALL paths

```
int getLongestPath(TreeNode root) {
	ld =	allDepthNodes(root.left)
	rd = allDepthNodes(root.right)
	leftLongest = getLongestPath(root.left)
	rightLongest = getLongestPath(root.right)

	ll = max(ld + rd, leftLongest, rightLongest)
	return ll
}

Note that to caluclae path, we need to find all possible combinations betwenn left and right branchs
```




Problem C
----------
Generate a random 4-digit even number : the adjacent 2 digits must be different. 
```
public int getNumber(){ 

	int ans = 0;
	ans += randomEven();
	int lastDigit = ans;

	base = 1
	LP(i, 0, 3){
		base *= 10;
		newDigit = randomBlack(lastDigit)
		ans += newDigit * base;
		lastDigit = newDigit
	}
}
```


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

Idea
--------
A brute force recursion will not work, because the Node may contain cycles => generally not a good idea to handle with recursion, so we have to solve it in steps

```
Node copy(Node from){
map<Node, Node> fromTo;

	Node curNode = from
	while(curNode != null) {
	Node cp = curNode()
	fromTo[from] = to;
	}

	Node curNode = from
	while(curNode != null) {
	fromTo[from].next = fromTo[curNode.next];
	fromTo[from].random = fromTo[curNode.random];
	}

	return fromTo[from];
}

```
