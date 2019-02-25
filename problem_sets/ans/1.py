'''
Analysis:
Start with a case discussion, and we found that the code between cases can be merged anyway, i.e., we relaxed complete search's scope, as long as the possible answer space remains.  

By the same logic, we can search at a bigger space where we know for sure the solution exists for the ease of implementation 
'''

def product_of_five_v1(array):
    array.sort()
    n = len(array)
    ans = -1e9
    ans = max(
        ans, array[n - 5] * array[n - 4] * array[n - 1] * array[n - 2] *
        array[n - 3])
    ans = max(ans,
              array[0] * array[1] * array[n - 1] * array[n - 2] * array[n - 3])
    ans = max(ans, array[0] * array[2] * array[n - 1] * array[3] * array[4])
    return ans


def product_of_five(array):
    array.sort()
    n = len(array)
    ans = -1e9

    for j in range(0, 6):
        temp = 1
        for i in range(0, j):
            temp *= array[i]
        for i in range(n - 5 + j, n):
            temp *= array[i]
        ans = max(ans, temp)
    return ans

'''
If no previous exists, all entries are ordered. Therefore, we start from from the tail and find the first OOO entry, 
and then from the tail again to find the first entry < the OOO one, and then reverse the whole subarray after the OOO entry

TODO: clean up with mulitple assignments
'''

def previous_permutation(permutation):
    global n
    firstOdd = -1
    for i in range(n -1, 0, -1):
        if permutation[i-1] > permutation[i]:
            firstOdd = i

    if firstOdd < 0:
        return permutation;

    for i in range(firstOdd, n):
        if(permutation[i-1] > permutation[i]):
            temp = permutation[i -1]
            permutation[i -1] = permutation[i];
            permutation[i] = temp
        else:
            break;

    return permutation;

'''
Idea 1: 
Assuming all distinct, then we just swap the smallest entry in order with the current one at the front, and recursivly call it 

When it is duplicate, we sort the array and check if we are swapping with the same value, so we need to keep the highest TWO values, in case there is a duplicate

Idea 2:
Start with sorted array, and keep calling next_perm(permutation), until it is all reversely sorted

TODO: clean up with multiple assignments
'''

def next_permutation(permutation):
    global n
    firstI= -1
    firstV = -1
    for i in range(n -1, 0, -1):
        if permutation[i-1] < permutation[i]:
            firstI = i - 1
            firstV = permutation[firstI];
            break;

    if firstI < 0:
        return False;

    newI = -1;
    newV = -1;
    for i in range(firstI + 1, n):
        if(permutation[i] > firstV):
            newI = i 
            newV = permutation[i]
        else:
            break;

    permutation[newI] = firstV;
    permutation[firstI] = newV;
    permutation[firstI + 1:] = sorted(permutation[firstI + 1:])
    print(' '.join(map(str, permutation)))

    return True;

def print_permutations(array):
    global n;
    array.sort(key=None, reverse=False)
    print(' '.join(map(str, array)))
    while True:
        good = next_permutation(array)
        if not good:
            break


