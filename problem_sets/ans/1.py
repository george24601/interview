'''
Analysis:
Start with a case discussion, and we found that the code between cases can be merged anyway, i.e., we relaxed complete search's scope, as long as the possible answer space remains.  
'''

def product_of_five(array):
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
