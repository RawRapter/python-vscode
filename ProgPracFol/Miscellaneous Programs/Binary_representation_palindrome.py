"""
Given an integer ‘n’, write a Python function that returns true if binary representation of x is palindrome else return false.

Input : n = 9
Output : True
Binary representation of n=9 is 1001 which 
is palindrome as well.

"""
#convert to binary if dont want to use bin(num)
def convert_to_binary(n):
    ans = 0
    p = 1
    while(n>0):
        last_bit = n&1
        ans += p*last_bit

        p*=10
        n=n>>1
    #print(ans)
    return ans

def palindrome(n):
    n = str(n)
    n1 = n[::-1]
    if(n1 == n):
        return "Binary Representation is palindrome"
    else:
        return "Not Palindrome"

# Driver program
if __name__ == "__main__":
    num = 9
    x = convert_to_binary(num)
    y = palindrome(x)
    print(y)

"""
Another way:

def binaryPallindrome(num):

	# convert number into binary
	binary = bin(num)

	binary = binary[2:]

	return binary == binary[-1::-1]

# Driver program
if __name__ == "__main__":
	num = 9
	print binaryPallindrome(num)


"""