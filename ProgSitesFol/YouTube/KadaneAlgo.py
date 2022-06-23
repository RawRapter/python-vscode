"""
Maximum Sum Subarray Array - Optimised Approach
"""

arr1 = [ 2, 3, 4, -10, 40, -70, 90 ]
def KadaneSubArray(x):
    n = len(x)
    currsum = 0
    maxsum = -999
    for i in range(0,n):
        currsum = currsum + x[i]
        if(currsum < 0):
            currsum = 0
        maxsum = max(maxsum,currsum)
    return maxsum
print(KadaneSubArray(arr1))