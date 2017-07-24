Problem A
--------
Given a positive integer n, find the no of integers less than equal to n, whose binary representation doesn't contain consecutive 1s.
eg:
I/P : 4
O/P: 4 (0,1,2,4 Valid)


Idea
-------
If a number has consecutive 1s, then it is either 

1. number of consecutive 1s, with last bits 0

2. (last bit 1 case) number of consecutive 1s, with last bits 01

3. (last bit 1 case) any number, with last bits 11 

Note that by master theorem, this solution is only slightly better than linear. Because similar to the tree traversal case, even though the combination steps is minimal, the relative large # of subproblems cancels the reduction in problem size

Solution
---------

```
int c11(int n){
	if (n < 3) 
		return 0
	int ans  = c11(n/2);

	if (n % 4) == 3 {
		ans += c11(n/4)
	}else{
		ans += c11(n/4 - 1)
	}


	if (n % 4) > 2 {
		ans += c11(n/4)
	}else{
		ans += c11(n/4 - 1)
	}

	return ans;
}
```



Problem B
--------
Giving a method intToEnglish that receives an int as a parameter, how do you return its representation in english words. The number can be of any size but no more than around 2 billion since the parameter is an int 2ˆ32

Idea
--------
1. need to get rid of billion, million, thousand suffix 
2. need to get rid of hundred number
3. need to get rid of tens number


```
string ltle2(int n) {
	string ans = ""
	
	if (n / 10) {
		//return the value based on n % 10
	}

	ans += //return value based on n % 10
}


string lt1e3 (int n) {
	string ans = "";
	if (n / 100){
		ans += lt1e2(n% 100)
		ans += "Hundred"
	}

	ans += lt1e2(n / 100)
}

string intToEnglish(int n){

if (n == 0) {
return "Zero"
}

int vs[3] = [1e9,1e6, 1e3, 1] 
int ns[3] = .....

string ans = "";
	LP(i, 0, 3) {
		if (n / vs[i]) {
			ans += lt1e3(n %vs[i])
			ans += ns[i]
			n %=  vs[i]
		}
	}
}

```


Problem C
--------
```
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You can begin the journey with an empty tank at one of the gas stations.
Return ALL the starting gas station's index where you can travel around the circuit once
public List<Integer> canCompleteCircuit(int[] gas, int[] cost) {
}
```

Idea
---------
Need prefix sum of roads and stations for sure. At each station, it is easy to calculate what is the cost and gain so far, and we will break early if cost > gain. O(n^2)

To get run time to O(n), we need to break our cycle into 2 parts =>  from current to end + from 0 to curret,  and answer question for each gas station i

```
1. what is the minimum amount of gas at station 0 we need to reach gas station i?

2. what is the minimum amount of gas at station i we need to reach gas station 0? Part 2 can be calculated by reversing all indices, and run the procedure we need to calculate the question above

```
Then we iterate through all stations, and it is feasible if gas[i] >=q2[i] && gas[i] + netcost to go from i to 0 >= q1[i]

I have to admit, coming up with O(n) solution and code it in less than 35 mins would be really challenging in a real interview!



Problem D
--------
```
Given a task sequence tasks such as ABBABBC, and an integer k, which is the cool down time between two same tasks. Assume the execution for each individual task is 1 unit.
rearrange the task sequence such that the execution time is minimal.
Example:
S = AAABBBCCC, K = 3
Result: ABCABCABC (all 'A's are 3 distance apart, similarly with B's and C's), thus return 9
S = AAABC, K=2
Result: ABCA_ _A, thus return 7
S = AAADBBCC, K = 2:
Result: ABCABCDA, thus return 8
public int rearrangeTasks(String tasks, int cooldown){
}
```

Idea
--------
Brute force: generate all permutations, and calculate cost in each case

Greedy Idea: 
For the next entry, we take one with minimal (cost, -numberOfEntries). However, cost = max(0, cooldown - i - lastUsed), this means we will have to iterate through all task types and calculate which one to use. The answer we get is the optimal soltuion that triggers costs in a lexically greatest way

We can also try filling tasks in a radix way, but handling gaps proves to be tricky 


