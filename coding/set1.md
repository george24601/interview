Problem A
--------
```
Remove any number containing 9, writing a number that returns nth number =
newNumber(1) = 1
newNumber(8) = 8
newNumber(9) = 10
```

Idea
------
suppose we know that given n, we know number of ints <= n s.t. these ints doesn't have 9

Then the target number t is t - num9(t) = n

Not that t - num9(t) is not decreasing, so we can bsearch on t, and return the min t that satisfies the equation, note that being the min t also guarantees that t can not have any 9. Otherwise, t - num9(t) will be same as previous t 

To calculate num9(t), we do induction on digits, i.e.,  

```
1. previous has no 9, but last digit gives

2. previous has 9
```


Code
----
```
int num9(int t){
	if(t < 9)
		return 0;
	else if(t == 9)
		return 1;
	else{
		int prev = t / 10;

		int lastD = t % 10;

		int prevHas9 = num9(prev - 1) * 10 + has9(prev) ? lastD : 0;

		int prevHasNo9 = prev - 1 - num9(prev - 1) + has9(prev) ? 0 : lastD == 9;  
		return prevHas9 + prevHasNo9;
	}
}

int bsearch(int l, int h, int n){
	if(l == h)
		return l;
	int mid = (l + h) / 2;
	int fv = mid - num9(mid);

	if(fv >= n){
		return bsearch(l, mid);
	}else if (fv < n){
		return bearch(mid + 1, h);
	} 
}

int newNumber(int n)
	return bsearch(1, 2 * n, n);
```

Problem B
---------
```
Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.
Try to do it in one pass
example
[4, 2, 0, 5, 2, 0, 1] return: 0, 2
[1, 2, 3, 0, 0, 1, 3, 6, 6,6] return 0, 1, 3, 6
```

Idea
-------
since it O(n) and const memory space, most likely comparion or set based solution won't work. We will have to use a radix-sort like approach


Code
----------

```
public vector<int> findRepeat(vector<int> nums){
	vector<int> ans;
	LP(i, 0,nums.size()){

		while(nums[i] != i){
			int curNum = nums[i];
			int toSwap = nums[curNum];
			
			if(curNum == toSwap){
				ans.push_back(curNum)
				break;
			}else{
				swap(i, curNum);
			}

		}
	}

	return ans;
}
```

It is on because each index got swapped in at most once, i.e., the whole swap happens at most n times


Problem C
-------------
Find the median of unsorted array
Have to do better than O(nlogn) time.
e.g.
Given [2, 6, 1] return 2
Given [2, 6, 1, 4] return 3 which is sum of the two elements in middle over 2


Idea
-------
use the linear random selection algorithm


Code
-------

int median(vector<int> a){

	int firstM = find(a, 0, a.size(), a.size()/2 + 1);

	if(a.size() % 2){
		int secondM = find(a, 0, a.size(), a.size()/2 + 2);
		return (firstM + secondM) / 2;
	}else{
		return firstM;
	}
}

int find(int si, int ei, int rank){

	if(si == ei)
		return si;

	int pivot = randmon(si, ei)
	swap(si, pivot)

	int bandEnd = si + 1;

	LPE(i, si + 1, ei) {
		if(a[i] <= a[pivot]){
			swap(bandEnd, i);
			bandEnd++;
		}
	}

	int bandLen = bandEnd - si;

	if(bandLen <= rank)
		return find(si, bandEnd - 1, rank);
	else
		return find(bandEnd, ei, rank - bandLen);
}
		


Problem D
--------
A "derangement" of a sequence is a permutation where no element appears in its original position. For example ECABD is a derangement of ABCDE, given a string, may contain duplicate char, please out put all the derangement
public List<char[]> getDerangement(char[]){}


Idea
-----
Sure we can brute force to generate all permutations and then filter, but it will be too slow, so we will have to filter it early. i.e., we should generate the number index by index

set<string> solve(){
	vector<int> cnt(26);
	set<string> toReturn;
	//add each char to the cnt map
	derangement("", 0, cnt, toReturn);

	return toReturn;
}

void derangement(string prefix, int i, vector<int> cnt, vector<string> toReturn){

	if(i == s.length())
	{
		toReturn.insert(prefix);
		return;
	}

	for(int i in [0, 26))
		if(cnt[i]){
			char nextC = 'a' + i;
			if(s[i] == nextC){

			}else{
				cnt[i] --;
				prefix.push_back(nextC);
				derangement(prefix, i + 1, cnt);
				prefix.pop();
				cnt[i]++;
			}
		}

} 
