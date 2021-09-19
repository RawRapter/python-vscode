"""
Program for Print Number series without using any loop
Problem – Givens Two number N and K, our task is to subtract a number K from N until number(N) is greater than zero, once the N becomes negative or zero then we start adding K until that number become the original number(N).
Note : Not allow to use any loop.

Examples :

Input : N = 15 K = 5  
Output : 15 10 5 0 1 5 10 15

Explanation – We can do it using recursion idea is that we call the function again 
and again until N is greater than zero (in every function call we subtract N by K). 
Once the number becomes negative or zero we start adding K in every function call 
until the number becomes the original number. Here we use a single function for 
both addition and subtraction but to switch between addition or subtraction 
function we used a Boolean flag.
"""

def PrintNumber(N, Original, K, flag):

	print(N, end = " ")

	if (N <= 0):
		if(flag==0):
			flag = 1
		else:
			flag = 0
		
	# base condition for
	if (N == Original and (not(flag))):
		return
	
	# if flag is true
	
	if (flag == True):
		PrintNumber(N - K, Original, K, flag)
		return
	
	# second case (Addition )
	if (not(flag)):
		PrintNumber(N + K, Original, K, flag)
		return
	
N = 20
K = 6
PrintNumber(N, N, K, True)