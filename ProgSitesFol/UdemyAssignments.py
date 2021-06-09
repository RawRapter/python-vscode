#Question 1
"""
Take a integer as a input from the user in the format 'Enter a value:' .Check whether the number is even number or odd number
and print it as 'Even' or 'Odd' necessarily.
If the number is odd then add the number with the ten's place of the given number and print the result as 'Result is : ' followed by value
If the number is even then add the number with the one's place of the given number and print the result as 'Result is : ' followed by value

Constraints:
0 <= number <= 99

Example:
Input 1 :
Enter a value : 29
Output1:
Odd
Result is : 49

Explanation: 29 + ten's place of the given number(20) =29+20 =49
Input 2 :
Enter a value : 28
Output2:
Even
Result is : 36
Explanation: 28 + one's place of the given number(8)=28+8 =36
"""
x = int(input("Enter a Value: "))
if x%2 == 0:
    print("Even")
    y = x % 10
    x += y
    print("Result is: ",x)
else:
    print("Odd")
    z = x//10
    z =  z*10
    x += z
    print("Result is: ",x)