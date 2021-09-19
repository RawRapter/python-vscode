"""
GFG
Check whether a number has consecutive 0’s in the given base or not

Given a decimal number N, the task is to check if a number has consecutive zeroes or not after converting the number to its K-based notation.

Examples: 

Input: N = 4, K = 2 
Output: No 
4 in base 2 is 100, As there are consecutive 2 thus the answer is No.

Input: N = 15, K = 8 
Output: Yes 
15 in base 8 is 17, As there are no consecutive 0 so the answer is Yes. 
"""

def hasConsecutiveZeroes(N, K):
	z = toK(N, K)
	if (check(z)):
		print("Yes")
	else:
		print("No")

# Function to convert N into base K
def toK(N, K):

	# Weight of each digit
	w = 1
	s = 0
	while (N != 0):
		r = N % K
		N = N//K
		s = r * w + s
		w *= 10
	return s

# Function to check for consecutive 0
def check(N):

	# Flag to check if there are consecutive
	# zero or not
	fl = False
	while (N != 0):
		r = N % 10
		N = N//10

		# If there are two consecutive zero
		# then returning False
		if (fl == True and r == 0):
			return False
		if (r > 0):
			fl = False
			continue
		fl = True
	return True

# Driver code
N, K = 15, 8
hasConsecutiveZeroes(N, K)
