Problem A
--------
Given an array of integers, return true if there're 3 numbers adding up to zero (repetitions are allowed)
{10, -2, -1, 3} -> true
{10, -2, 1} -> true -2 + 1 +1 =0

Idea
------
Standard read and then update pattern problem

```
Set<int> twoSums 

LP(i, 0, n){
	if(twoSums.count(a[i])) 
		return true
	else
		LP(j, 0, i)
			twoSums.insert(a[i] + a[j])
}

return false
```


Problem B
-------
You're given an array of integers(eg [3,4,7,1,2,9,8]) Find the index of values that satisfy A+B = C + D, where A,B,C & D are integers values in the array.

Eg: Given [3,4,7,1,2,9,8] array
The following
3+7 = 1+ 9 satisfies A+B=C+D
so print (0,2,3,5)

Idea
-------
Simliar to the problem above. Try all O(n^2) combinations, put it ina map<int, PII>. Note that we need to keep track of only one pair, because 
```
1. we will terminate early

2. For all feasible combinations, we just look for the one with lexigraphically minimal (A, B). Our solution will not miss, because if there exists solution with A + B = S, then 
we know there must exist solution with lexigraphically minimal (A, B) as a solution, s.t., A+ B = S. 

3.Because if there is multiple values of A and B in the array, we can just swap indexes to move the index of A and B forward.

4. Otherwise, we know there are multiple non-intersecting pairs that satisfies A + B = S.  We can obviously pick the first S sum pair we meet
```  


Problem C
-------
Given an undirected graph and a node, modify the graph into a directed graph such that, any path leads to one particular node.

Idea
-------
DFS variant. 

Test cases
-----
```
1. 2 node path
2. 3 node simple path
3. 3 node cycle

```

```
void dfs(v, from){
	if (visited[v])
		return
	else
		visited[v] = true

	LP(i, 0, g[v].size()){
		int u = g[v][i]
		dfs(u, v)
	}

	removeDir(v, from)
}
```

Problem D
--------
Input: A string equation that contains numbers, '+' and '*'
Output: Result as int.

For example:
Input: 3*5+8 (as String)
Output: 23 (as int)

```
int nextI;

int solve(string s){
	int sumSoFar = 0;
	int lastNum = parseInt()
	
	while (nextI < s.size()){
		char op = parseOp
		
		n = parseInt()
		
		if(op == '+'){
			sumSoFar += lastNum
			lastNum = n;
		}else{
			lastNum *= n
		}
	}

	return sumSoFar + lastNum
}
```


