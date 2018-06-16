'''Parameter array is an array of integers The function should return an integer'''
def product_of_five(array):
    array.sort()
    global n
    ans = -1e9
    ans = max(ans, array[n - 5] * array[n - 4] * array[n - 1] * array[n - 2] * array[n - 3])
    ans = max(ans, array[0] * array[1] * array[n - 1] * array[n - 2] * array[n - 3])
    ans = max(ans, array[0] * array[2] * array[n - 1] * array[3] * array[4])
    return ans
