"""
This set is related to string python programs, question taken from GeeksOfGeeks
"""
#All Import
import re
#Strings Created:
a = 'anna'
b = 'anant'
c = 'bumbum'
str = "My Name is Anant Arun"

"""
1) Program to check if a string is palindrome or not
"""
#Method 1, using slicing
def PalindromeString(x):
    if type(x) != str:
        raise Exception("Please Provide String Only")
    if x == x[::-1]:
        return "String is Palindrome"
    else:
        return "String is not Palindrome"
print(PalindromeString(a))
#Time taken:  0.0009963512420654297

#Method 2, using recursion
def PalindromeString1(x):
    x = x.lower()
    length = len(x)
    if length < 2:
        return "Yes it is Palindrome"
    elif x[0] == x[length-1]:
        return PalindromeString1(x[1:length-1])
    else:
        return "Not a Palindrome"
print(PalindromeString1(a))
#Time taken:  0.0009579658508300781

#Method 3, using flag
def PalindromeString2(x):
    flag = 0
    k = -1
    for i in x:
        if i != x[k]:
            k -= 1
            flag = 1
            break
        k -= 1
    if flag == 0:
        return "String is Palindrome"
    else:
        return "String is not Palindrome"
print(PalindromeString2(a))
#Time taken:  0.0009965896606445312

#Method 4,using Iterative method
def PalindromeString3(x):
    length = len(x)
    for i in range(0,int(length/2)):
        if x[i] != x[length - i - 1]:
            return "String is not Palindrome"
    return "String is Palindrome"
print(PalindromeString3(a))
#Time taken:  0.0009963512420654297

"""
2) Basic program to check whether the string is Symmetrical
"""
#Method 1, using string slicing
def SymmetricalString(x):
    end = len(x)
    mid = int(len(x)/2)
    if x[0:mid] == x[mid:end]:
        return "String is Symmetrical"
    else:
        return "String is not Symmetrical"
print(SymmetricalString(c))
#Time taken:  0.0009968280792236328

#Method 2, using flag
def SymmetricalString1(x):
    end = len(x)
    mid = int(len(x)/2)
    start1,start2 =0,mid
    flag = 0
    while start1 < mid and start2 < end:
        if x[start1] == x[start2]:
            start1 += 1
            start2 += 1
        else:
            flag = 1
            break
    if flag == 0:
        return "String is Symmetrical"
    else:
        return "String is not Symmetrical"
print(SymmetricalString1(c))
#Time taken:  0.0009965896606445312

"""
3) Basic program to Reverse words in a given String in Python
"""
#Method 1, using regular expression
def ReverseWords(x):
    str1 = re.split('\s',x)
    str2 = ''
    for i in str1[:0:-1]:
        str2 = str2 + i + ' '
    str2 += str1[0]
    return str2
print(ReverseWords(str))
#Time taken:  0.000997781753540039

#Method 2, using normal split function of string
def ReverseWords1(x):
    str1 = x.split()[::-1]
    str2 = ''
    for i in str1[:-1:1]:
        str2 = str2 + i + ' '
    str2 += str1[-1]
    return str2
print(ReverseWords1(str))
#Time taken:  0.0009942054748535156

#Method 3, using split,reversed and join
def ReverseWords2(x):
    str1 = reversed(x.split())
    r = ' '.join(str1)
    return r
print(ReverseWords2(str))
#Time taken:  0.000997304916381836

"""
4) Basic Program to remove i’th character from string in Python
"""
#Method 1, using replace
print(str.replace('n',' ',1)) #First occurence of 'n' deleted

#Method 2, using regex
print(re.sub('n',' ',str,1)) #First occurence of 'n' deleted

#Method 3, using Naive method
n = 3 #4th position to be deleted
new_str = ''
for i in range(len(str)):
    if i !=n:
        new_str = new_str + str[i]
print(new_str)