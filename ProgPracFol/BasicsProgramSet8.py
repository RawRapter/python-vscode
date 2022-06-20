"""
This Set is related to all searching and sorting programs
"""
#Arrays (List)
arr1 = [ 2, 3, 4, 10, 40, 70, 90 ]
arr2 = [5,3,6,2,65,34,23,76,12,9]

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

"""
2) Linear Search
"""
#Method 1, iterating through each element
def LinearSearch(x,k):
    for i in x:
        if i == k:
            x = 1
        else:
            x = -1
    if x == 1:
        return "Element found"
    else:
        return "Element not found"
print(LinearSearch(arr2,12))
#Time taken:  0.0010023117065429688

#Method 2, simpler than above
def LinearSearch(x,k):
    for i in x:
        if i == k:
            return "Element Found"
    return "Element Not found"
print(LinearSearch(arr2,45))
#Time taken:  0.0009970664978027344

"""
3) Insertion Sort
"""
#Method 1, normal way
def InsertionSort(x):
    for i in range(1,len(x)):
        key = x[i]
        j = i-1
        while j > 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key
def TraversingIS(x):
    InsertionSort(x)
    for i in range(len(x)):
        print(x[i],end=" ")
TraversingIS(arr2)
#Time taken:  0.003993988037109375

"""
4) Quick Sort
"""
#Partition function
def QuickPartition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high): #Loop for partitiong element < pivot > element
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1] #replacing with the mid one
    return (i+1)

#Sorting function
def QuickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = QuickPartition(arr, low, high)
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)

#displaying function
def DisplayQS(x):
    n = len(x)
    QuickSort(x,0,n-1)
    for i in range(n):
        print(x[i],end=" ")
DisplayQS(arr2)
#Time taken:  0.0039958953857421875