"""
This Set is related to all searching and sorting programs
"""
#Arrays
arr1 = [ 2, 3, 4, 10, 40, 70, 90 ]


"""
1) Binary Search
"""
#Method 1, using recursion
def Bsearching(arr, first, last, x):
    if last >= first:
        mid = (last + first) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return Bsearching(arr, first, mid - 1, x) 
        else:
            return Bsearching(arr, mid + 1, last, x)
    else:
        return -1
def BinarySearch(k,j):
    result = Bsearching(k,0,len(k)-1,j)
    if result != -1:
        return "Element is Present"
    else:
        return "element not present"
print(BinarySearch(arr1,10))
#Time taken:  0.003993511199951172

#Method 2, iterating method
def Bsearching1(arr,x):
    first = 0
    mid = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] < x:
            first = mid + 1
        elif arr[mid] > x:
            last = mid - 1
        else:
            return mid
    return -1
def BinarySearch1(k,j):
    result = Bsearching1(k,j)
    if result != -1:
        return "Element is Present"
    else:
        return "element not present"
print(BinarySearch1(arr1,10))
#Time taken:  0.00399470329284668