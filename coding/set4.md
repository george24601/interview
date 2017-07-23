Problem A
--------
Reverse a linked list with O(1) space

```
pair<Node, Node> rev(Node h) {

	if (h.next == null)
		return pair<Node, Node> (h, h)
	else{
		nh, nt := rev(h.Next)
		nt.Next = h
		h.Next = null
		return PNN(nh, h)
	}
}

```


Problem B
--------
print rows of a binary tree, terminating each row with a carriage return

```
depth[root] = 0

toExpand.insert(root)
lastVisit = null

while(toExpand.size()) {
	int curV = toExpand.top();
	toExpand.pop();

	if (lastVisit != null && depth[lastVisit] == depth[curV] - 1){
		cout << endl
	}
	lastVisit = curV;
	cout << curV;

	foreach neighbor in curVNeighbors
		if depth[neighbor] < 0 {
			depth[neighbor] = depth[curV] + 1
			toExpand.push_back(curV)
		}
}

```

Problem C
--------
Print all anagrams of a string

```

vector<string> prefix;
set<string> ans;
void anagram(
	map<int, int> nc){

	if(nc.count() == 0)
		ans.insert(prefix);
	return;

	for(key in nc){
		nc[key] --
		prefix.push_back(key)
		anagram(nc)
		prefix.pop_back()
		nc[key]++
	}

}


```

Problem D
-----------
suppose a row of parking lot with n spots, one of them is empty and n-1 spots are occupied with cars. Only one operation is allowed: move one car from its position to the empty spot. Given a initial order of cars and a final order, output steps needed to convert initial order to final oder with that operation.

Follow up: Minimize steps needed. 

ex: 

{1 2 3 -1 4 5} 
move car 1 to empty spot(denoted as -1) will make it {-1,2,3,1,4,5} 
push 1 to the output list because you move car 1 to the empty spot 

suppose you have a initial order {1 2 3 -1 4 5} and a final order {5,1,-1,3,2,4}, you need to transfer {1 2 3 -1 4 5} to {5,1,-1,3,2,4}, push each car moved into a output list.


```
map<int, int> vToI;
int a[N], target[N];

void swap(int fromV, toV){
//update vToI for both here
//update a for both new vToI here
}

void rearrange(int size){
if (size == 0)
	return

if (a[size -1] == target[size -1]){
}else{
	

swap(target[a[size-1]], -1)

swap(target[size - 1], -1)
	rearrange(size - 1)
}
}



```

