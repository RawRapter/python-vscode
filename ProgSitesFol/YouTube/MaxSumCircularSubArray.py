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

def circSubAray(x):
    n = len(x)
    wrapsum=0
    nonwrapsum = KadaneSubArray(x)
    totalsum = 0
    for i in range(0,n):
        totalsum = totalsum + x[i]
        x[i] = -x[i]
    wrapsum = totalsum + KadaneSubArray(x)
    return max(wrapsum,nonwrapsum)

print(circSubAray(arr1))