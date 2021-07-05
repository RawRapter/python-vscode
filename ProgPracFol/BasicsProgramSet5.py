"""
This set is related to string python programs, question taken from GeeksOfGeeks
"""
#All Import
from itertools import count
import re
from collections import Counter
#Strings Created:
a = 'anna'
b = 'anant'
c = 'bumbum'
str = "My Name is Anant Arun"
stra = "My My Name Name Name is is is is Anant Anant Arun"
strb = "My_Name_is_Anant_Arun"

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

"""
5) Basic program to Check if a Substring is Present in a Given String
"""
#Method 1, using in operator
if "Anant" in str:
    print("It exists")
else:
    print("No not present")
#Time taken:  0.0009982585906982422

#Method 2, using regex
xe = re.search("Anant",str)
if xe:
    print("yes exists")
else:
    print("Doesnt exist")
#Time taken:  0.0009989738464355469

#Method 3, using find
if (str.find("Anant")) == -1:
    print("Not Exists")
else:
    print("Exists")
#Time taken:  0.0019922256469726562

"""
6) Basic program for Words Frequency in String Shorthands
"""
#Method 1, using regex & dictionary comprehension
def wordcount(x):
    res = re.split('\s',x)
    return {key:x.count(key) for key in res}
print(wordcount(stra))
#Time taken:  0.002000093460083008

#Method 2, using string split instead of regex
def wordcount1(x):
    return {key:x.count(key) for key in x.split()}
print(wordcount1(stra))
#Time taken:  0.0009968280792236328

#Method 3, using counter
def wordcount2(x):
    return Counter(x.split())
print(wordcount2(stra))
#Time taken:  0.001996278762817383

"""
7) Basic program to Convert Snake case to Pascal case
"""
#Method 1, using regex
def PascalCase(x):
    return re.sub('_','',x)
print(PascalCase(strb))
#Time taken:  0.000997781753540039

#Method 2, using replace()
def PascalCase1(x):
    return x.replace('_','')
print(PascalCase1(strb))
#Time taken:  0.0009965896606445312

"""
8) Basic Program to Find length of a string in python
"""
#Method 1, using len()
print(len(strb))
#Time taken:  0.0009980201721191406

#Method 2, iterating over it through for loop
c = 0
for i in strb:
    c += 1
print(c)
#Time taken:  0.0009899139404296875

#Method 3, iterating over it through while loop
c = 0
while(c <= len(strb)):
    c +=1
print(c)
#Time taken:  0.0010058879852294922

#method 4, while loop and string slice
c = 0
while str[c:]:
    c +=1
print(c)
#Time taken:  0.0009963512420654297

"""
9)Basic program to print even length words in a string
"""
#Method 1, iterative method
def EvenLengthWords(x):
    l = x.split()
    for i in l:
        if len(i)%2 == 0:
            print(i)
print(EvenLengthWords(str))
#Time taken:  0.0009968280792236328

#Method 2, using lise comprehension
def EvenLengthWords1(x):
    return [i for i in x.split() if len(i)%2 == 0]
print(EvenLengthWords(str))
#Time taken:  0.0010204315185546875

"""
10) Basic program to accept the strings which contains all vowels
"""
VowelSet = {'a','e','i','o','u'}
#Method 1, Normal Approach - comparing set
def VowelCheck(x):
    set2 = set({})
    for i in x:
        if i in VowelSet:
            set2.add(i)
    if VowelSet == set2:
        return "String Accepted, all vowels there"
    else:
        return "String not accepted all vowel not there"
print(VowelCheck(str))
#Time taken:  0.0020024776458740234

#Method 2, using intersection, set and len
def VowelCheck1(x):
    if len(set(x.lower()).intersection("aeiou")) >= 5:
        return "String Accepted, all vowels there"
    else:
        return "String not accepted all vowel not there"
print(VowelCheck1(str))
#Time taken:  0.0009982585906982422

"""
11) Basic Program to Count the Number of matching characters in a pair of string
"""
#Method 1, using 2 loops comparing each data then adding it in set then finding it's length
def CountMatchCharacter(x,y):
    matchset = set({})
    for i in x:
        for j in y:
            if i == j:
                matchset.add(i)
    return len(matchset)
print("No. of matches: ",CountMatchCharacter(a,b))
#Time taken:  0.00099945068359375

#Method 2, converting string to set and using & operation
def CountMatchCharacter1(x,y):
    setx = set(x)
    sety = set(y)
    setmatch = setx & sety
    return len(setmatch)
print("No. of matches: ",CountMatchCharacter1(a,b))
#Time taken:  0.0009961128234863281

#Method 3, using regular expression, this will count duplicates
def CountMatchCharacter2(x,y):
    c = 0
    for i in x:
        if re.search(i,y):
            c += 1
    return c
print("No. of matches: ",CountMatchCharacter2(a,b))

"""
12) Basic program to Remove all duplicates from a given string in Python
"""
#Method 1, coonverting to set and join
def RemoveStringDuplicates(x):
    return "".join(set(x))
print(RemoveStringDuplicates(str))

#Method 2, removing duplicates and getting result in order using for loop and empty string
def RemoveStringDuplicates1(x):
    t = ""
    for i in x:
        if i in t:
            pass
        else:
            t += i
    return t
print(RemoveStringDuplicates1(str))
#Time taken:  0.0009965896606445312