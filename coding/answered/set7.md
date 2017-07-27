Problem A
-----------
how to find leaf node value from preorder sequence of BST without rebuilding the tree

```
pair<vector<char>, int> leaves(string s, int start, int nextStart){
	if(start == nextStart - 1)
		return make_pair(vector<int>{s[i]}, 1);
	else if(start == nextStart)
		return make_pair(vector<int>(), 0);

	leftResult = leaves(s, start + 1, nextStart)	
	rightResult = leaves(s, start + 1 + leftResult.second, nextStart)

	return make_pair(merge(leftResult.fist, rightResult.frist), leftResult.second + rightResult.second + 1)
}


```


Problem B
-------
write a function that randomly return a random Fibonacci number in range [min, max) 

```
vector<int> fibs; 

void precalc(){
fibs.push_back(1);
fibs.push_back(2);

	while(fibs[size - 1] <= int.Max - fibs[size -2]){
		fibs.pushback(fibs[size-1] + fibs[size -2])
	}
}

	
public int getRandom (int min, int max){
	int leftMost = bsearch(min)
	int nextStart = bsearch(max)

	int randI = random(nextStart - leftMost) + nextStart //-1 or not depends on random semantics
	return fibs[randI]
}

```


Problem C
---------
Find the Lexicographic next word of the input word from a list of words 
Example 
Words list 
[Cat, dog, cow, donkey, zebra, monkey], 
input 
duck 
output 
monkey 

Input 
dog 

output 
donkey 

Use trie to solve it 

public String findNextWord(List<String> words, String input){ 
}

```
vector<char> path;
parentRightChild = null
vector<char> parentPrefix

Node iterate(Node n, String input, int i){
	if(i == input.size()){
		return n;
	}

	for(child : n.children) {
		if(child.c == input[i]){
			
			if(c is not last){
				parentRightChild = next child
				parentPrefix = path
			}

			path.push_back(input[i])
			iterate(child, input, i+1)	
		}
	}
}

public String findNextWord(List<String> words, String input){ 
	endNode = iterate(root, input, 0)
	if(endNode.left != null){
		leftMostEnd(endNode.Left)
	}else if(endNode.right != null) {
		leftMostEnd(endNode.Right)
	}else if(parentRightChild != null){
		path = parentPrefix
		leftMostEnd(parentRightChild)
	}
	
	return toString(path)
}


```


Problem D
----------
Given a equation in the form of "3x+4y+2=-5y+2x+10", simplify the equation to be in form "y=Ax+B", and return A,B. Also allow parenthesis to be in the equation. Ex. "3y-4x+(3-(2x-3y))=10y", result is "y =0.75 - 1.5x"


```

map<char, int> parse(string s, int start, int nextStart){
	if(s[start] == nextStart)
		return map<char, int>

	if(s[start] == '(')){
		int end = findMatching(start)
		return plus(parse(start + 1, end), parse(end, nextStart))
	}

	int f = 1;
	if(s[start] == '-'){
		f= -1;
		start++;
	}

	int coef = 0;
	while(s[start] is digit){
		coef *= 10; 
		coef += s[start] - '0'
		start++;
	}

	get operand
	
	rest = parse(start,nextStart)
	add operand to the reset
	
	return rest
}

string simplify(string s){
	int i = s.find('=')
	map<char, int> lhs = parse(s.substr(i));
	map<char, int> rhs = parse(s.substr(i + 1));

	map<char, int> subtracted = substract(lhs, rhs)

	return construct(subtracted)
}
```


