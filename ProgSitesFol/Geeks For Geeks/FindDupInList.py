class Solution:
    def duplicates(self, arr, n): 
        # code here
        arr1 = set()
        dup = set()
        for i in arr:
            if i in arr1:
                dup.add(i)
            else:
                arr1.add(i)
        dup = sorted(list(dup))
        if len(dup) == 0:
            return [-1]
        else:
            return dup
            

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
        """
        Time limit is exceeding by 2.66 second
        
        # code here
        arr1 = []
        dup = []
        for i in arr:
            if i not in arr1:
                arr1.append(i)
            elif i in dup:
                continue
            else:
                dup.append(i)
        dup.sort()
        if(len(dup)>0):
            return dup
        else:
            return [-1]
        """