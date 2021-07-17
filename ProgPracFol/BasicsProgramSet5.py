"""
This set is related to string python programs, question taken from GeeksOfGeeks
"""
#All Import
from itertools import count
from operator import index
import re
from collections import Counter
#Strings Created:
a = 'anna'
b = 'anant'
c = 'bumbum'
str = "My Name is Anant Arun"
stra = "Anant arun is doing masters"
strb = "My_Name_is_Anant_Arun"
strc = "0011101001"
strd = "Anant is doing btech anant has joined PEC pec is a good college"
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

"""
13) Basic program to Least Frequent Character in String
"""
#Method 1, using dictionary comprehension and min()
def LessFrequentCharacter(x):
    l =  {key:x.count(key) for key in list(x)}
    return min(l,key=l.get)
print(LessFrequentCharacter(b))
#Time taken:  0.000997304916381836

#Method 2, using naive method for loops
def LessFrequentCharacter1(x):
    l = {}
    for i in x:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    return min(l,key=l.get)
print(LessFrequentCharacter1(b))
#Time taken:  0.0009980201721191406

#Method 3, using counter
def LessFrequentCharacter2(x):
    l = Counter(x)
    return min(l,key=l.get)
print(LessFrequentCharacter2(b))
#Time taken:  0.001001119613647461

"""
14) Basic program to Most Frequent Character in String
"""
#Method 1, using dictionary comprehension and min()
def MostFrequentCharacter(x):
    l =  {key:x.count(key) for key in list(x)}
    return max(l,key=l.get)
print(MostFrequentCharacter(b))
#Time taken:  0.0010006427764892578

#Method 2, using naive method for loops
def MostFrequentCharacter1(x):
    l = {}
    for i in x:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    return max(l,key=l.get)
print(MostFrequentCharacter1(b))
#Time taken:  0.000997781753540039

#Method 3, using counter
def MostFrequentCharacter2(x):
    l = Counter(x)
    return max(l,key=l.get)
print(MostFrequentCharacter2(b))
#Time taken:  0.0009953975677490234

"""
15) Basic program to Program to check if a string contains any special character
"""
#Method 1, regular expression and compile() is used
def StringSpecialCharCheck(x):
    spec = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    if spec.search(x) == None:
        return "No Special Character string is accepted"
    else:
        return "String is rejected"
print(StringSpecialCharCheck(a))
#Time taken:  0.0010004043579101562

#Method 2,Naive Method -  Using loops, if method
def StringSpecialCharCheck1(x):
    k = True
    j = "[@_!#$%^&*()<>?/\|}{~:]"
    for i in x:
        if i in j:
            k = False
            break
    if k == True:
        return "No Special Character string is accepted"
    else:
        return "String is rejected"
print(StringSpecialCharCheck1(a))
#Time taken:  0.0010044574737548828

"""
16) Basic Program to Find words which are greater than given length k
"""
#Method 1, Using List comprehension , split()
def StringLengthCheck(x):
    k = 4 #Length limit set
    return [i for i in x.split() if len(i) > 4]
print(StringLengthCheck(str))
#Time taken:  0.000990152359008789

#Method 2 , Naive method
def StringLengthCheck1(x):
    k = input("Give the length limit: ")
    str1 = []
    splits = x.split()
    for i in splits:
        if len(i) > k:
            str1.append(i)
    return str1
print(StringLengthCheck1(str))
#Time taken:  0.001986265182495117 (putting k constant)


"""
17) Basic program for removing i-th character from a string
"""
#Method 1, using list funtions, x is string and k is index to be deleted
def removeCharInStr(x,k):
    z = ''
    splt = list(x)
    splt.pop(k-1)
    for i in splt:
        z += i
    return z
print(removeCharInStr(b,2))
#Time taken:  0.0009942054748535156

#Method 2, using string slicing
def removeCharInStr1(x,k):
    a = x[:k]
    b = x[k+1:]
    return a + b
print(removeCharInStr1(b,2))
#Time taken:  0.0009970664978027344

#Method 3, using string replace [It is not working properly]
def removeCharInStr2(x,k):
    for i in range(len(x)):
        if i == k-1:
            x = x.replace(x[i],"",1)
    return x
print(removeCharInStr2(b,3))
#Time taken:  0.0009968280792236328

"""
18) Basic program to split and join a string to get '-' instad of space
"""
#Method 1
def StringSplitJoin2(x):
    listx = x.split(' ')
    print("After Split-> ",listx)
    strx = '-'.join(listx)
    print("After Join: ",end=" ")
    return strx
print(StringSplitJoin2(str))
#Time taken:  0.002007722854614258

#Method 2, instead of splitting and joing directly using string replace
def StringSplitJoin(x):
    x = x.replace(" ","-")
    return x
print(StringSplitJoin(str))
#Time taken:  0.0039975643157958984

#Method 3, using regex
def StringSplitJoin1(x):
    x = re.sub("\s","-",x)
    return x
print(StringSplitJoin1(str))
#Time taken:  0.003983259201049805

"""
19) Basic Program to Check if a given string is binary string or not
"""
#Method 1 , splitting string and converting to set
def BinaryStringCheck(x):
    x = set(list(x))
    if ('0' in x) and ('1' in x) and (len(x) == 2):
        return "Yes it is binary"
    else:
        return "It is not binary"
print(BinaryStringCheck(strc))
#Time taken:  0.0009982585906982422

#Method 2, iterating through characters
def BinaryStringCheck1(x):
    t = "01"
    count = 0
    for i in x:
        if i not in t:
            count = 1
            break
        else:
            pass
    if count == 1:
        return "Yes it is binary"
    else:
        return "It is not binary"
print(BinaryStringCheck1(strc))
#Time taken:  0.0009984970092773438

"""
20) Basic program to find uncommon words from two Strings
"""
#Method 1, using loops and list
def UncommonWords(x,y):
    xlist = x.split()
    ylist = y.split()
    z = []
    for i in xlist:
        if i not in ylist:
            z.append(i)
    for i in ylist:
        if i not in xlist:
            z.append(i)
    return z
print(UncommonWords(str,stra))
#Time taken:  0.0009970664978027344

#Method 2, using symmetric difference
def UncommonWords1(x,y):
    xlist = x.split()
    ylist = y.split()
    k=set(xlist).symmetric_difference(set(ylist))
    return k
print(UncommonWords1(str,stra))
#Time taken:  0.0009989738464355469

"""
21) Basic Program to Replace duplicate Occurrence in String
"""
#Method 1, using enumerate,split,join
def ReplaceDuplicate(x):
    split1 = x.split()
    replace_dict = {'anant':'he','PEC':'it'}
    newr = set()
    for idx,ele in enumerate(split1):
        if ele in newr:
            split1[idx] = replace_dict[ele]
        else:
            newr.add(ele)
    newr = ' '.join(split1)
    return newr
print(ReplaceDuplicate(strd))
#Time taken:  0.003998756408691406

#Method 2, using list comprehension , index() , dictionary
def ReplaceDuplicate1(x):
    split1 = x.split()
    replace_dict = {'anant':'he','PEC':'it'}
    result = ' '.join([replace_dict.get(val) if val in replace_dict.keys() and split1.index(val) != idx
    else val for idx,val in enumerate(split1)])
    return result
print(ReplaceDuplicate1(strd))
#Time taken:  0.0009970664978027344