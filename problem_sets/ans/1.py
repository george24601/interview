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
'''

def previous_permutation(permutation):
    pass

'''
Idea 1: 
Assuming all distinct, then we just swap the smallest entry in order with the current one at the front, and recursivly call it 

When it is duplicate, we sort the array and check if we are swapping with the same value, so we need to keep the highest TWO values, in case there is a duplicate

Idea 2:
Start with sorted array, and keep calling next_perm(permutation), until it is all reversely sorted
'''



