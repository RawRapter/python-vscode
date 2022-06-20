"""
This Set has Pattern Programs
"""

"""
1) G pattern
"""
#From GFG
def Pattern(line):
    pat=""
    for i in range(0,line):   
        for j in range(0,line):    
            if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
                i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2)
                and j > line-5 and j < line-1) or (j == line-2 and
                i != 0 and i != line-1 and i >=((line-1)/2))): 
                pat=pat+"*"  
            else:     
                pat=pat+" "  
        pat=pat+"\n"  
    return pat
line = 7
print(Pattern(line))
#Time taken:  0.0039958953857421875

"""
2) Inverted Star pattern
"""
#Method 1 using loops
def InvertedStar(x):
    for i in range(x):
        for j in range(i):
            print(" ",end="")
        for j in range(i,x):
            print("*",end="")
        print("")
line = 5
print(InvertedStar(line))
#Time taken:  0.003993988037109375

#Method 2, lesser code
n = 5
for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')
#Time taken:  0.003996372222900391

"""
3) Double sided stair case patten
"""
def pattern(n):
	for i in range(1,n+1):
		k =i + 1 if(i % 2 != 0) else i
		for g in range(k,n):
			if g>=k:
				print(end=" ")
		for j in range(0,k):
			if j == k - 1:
				print(" * ")
			else:
				print(" * ", end = " ")

n = 10
pattern(n)
#Time taken:  0.047942161560058594