"""
Regular Expression Programs
"""
import re
from collections import Counter

#Strings
a = "My11Name12Is12Anant11$93a11@"
b = "My11Name12Is11Anant93ab11"
c = "AnantArunKumarTiwari"
d = "anna"
e = "anant"
f = "My My Name is is is anant arun arun"
g = "a#f$b@gjdg*dg&"
h = "anant123"
i = "anant@"
j = "anantarunheroacademia"
url = "https://rawrapter.github.io/portfolio/"
email = "anant.arun92@gmail.com"
filenames = ["anant.html", "anant.xml", "anant.txt", "anant.jpg"]
password = "Anant_Zura007"

"""
1) Program to Check if String Contain Only Defined Characters using Regex
"""
#Method 1
def TxtSearch(x: str)->str:
    """
    Input: String
    Output String -> Valid/Invalid
    Checks the existence of specific string provided
    """
    if re.search("^[1234]+$",x):
        return "Valid String"
    else:
        return "Invalid String"
print(TxtSearch("1234"))
print(TxtSearch("567"))
#Time taken:  0.0009937286376953125

"""
2) Program to Count Uppercase, Lowercase, special character and numeric values using Regex
"""
#Method 1, using search
def RegCount(x: str):
    """
    Input: String
    Output: Integer
    Counts the number of Upper Case, Lower Case, Special and Numerical Characters.
    """
    c1,c2,c3,c4=0,0,0,0
    for i in x:
        if re.search("^[A-Z]+$",i):
            c1+=1
        elif re.search("^[a-z]+$",i):
            c2+=1
        elif re.search("^[1-9]+$",i):
            c4+=1
        elif re.search("^[!@#$%^&*]+$",i):
            c3+=1
    print("Number Of Upper Case: ",c1,"\nNumber of Lower Case: ",c2,"\nNumber of digits: ",c4,"\nnumber of special char: ",c3)
    return "Alldone"
print(RegCount(a))
#Time taken:  0.0009987354278564453

#Method 2,using findall and length
UpperCase = re.findall(r"[A-Z]",a)
LowerCase = re.findall(r"[a-z]",a)
Digit = re.findall(r"[1-9]",a)
Special = re.findall(r"[!@#$%^&*]",a)
print("Upper Case: ",len(UpperCase))
print("Lower Case: ",len(LowerCase))
print("Digit: ",len(Digit))
print("special: ",len(Special))
#Time taken:  0.000997304916381836

"""
3) Program to find the most occurring number in a string using Regex
"""
#Method 1
def CountNumber(x: str)->int:
    """
    Input: String
    Output: Integer
    returns the highest count number
    """
    c = re.findall(r"[1-9]+",x)
    max,maxele = 0,0
    d = Counter(c)
    #print(d)
    j = list(d.keys())
    #print(j)
    for i in j:
        if d[i] > max:
            max = d[i]
            maxele = int(i)
    return maxele
print(CountNumber(b))
#Time taken:  0.003999233245849609

"""
4) Program to extract maximum numeric value from a string
"""
#Method 1
def max_num(x: str)->int:
    """
    Input: String
    Output: Integer
    Finds the maximum integer in the string
    """
    c = re.findall(r"[1-9]+",x)
    maxele = 0
    for i in c:
        if int(i) > int(maxele):
            maxele = i
    return maxele
print(max_num(b))
#Time taken:  0.0039942264556884766

#Method2
def max_num1(x: str)->int:
    """
    Input: String
    Output: Integer
    Finds the maximum integer in the string
    """
    c = re.findall("\d+",x)
    n = map(int,c)
    return max(n)
print(max_num1(b))
#Time taken:  0.003995180130004883

"""
5) Program to put spaces between words starting with capital letters using Regex
"""
#1 Method
def space_between_words(x: str)->str:
    """
    Input/Output: String
    Takes a string and seperate the words where the letters are capital
    """
    c = re.findall("[A-Z][a-z]*",x)
    for i in range(len(c)):
        c[i]=c[i][0].lower()+c[i][1:]
    return ' '.join(c)
print(space_between_words(c))
#Time taken:  0.0010013580322265625

"""
6) Program to Check whether a string starts and ends with the same character or not
"""
#1 Method
def check_same_start_and_end(x: str)->str:
    """
    Input: String
    Output: String -> Valid/Invalid
    Checks if the string starts and ends with same character
    """
    regex = r"^[a-z]$|^([a-z]).*\1$"
    if(re.search(regex,x)):
        return "Valid"
    else:
        return "Invalid"
print(check_same_start_and_end(c))
#Time taken:  0.0009894371032714844

"""
7) Program in regex to find sequences of one upper case letter followed by lower case letters
"""
#Method 1
def uc_sequence(x: str)-> str:
    """
    Input: String
    Output: String
    Check if there is any word exists with first alphabet uppercase and else lower case.
    """
    c = re.findall("[A-Z][a-z]*",x)
    if c:
        return "Yes"
    else:
        return "No"
print(uc_sequence(d))
#Time taken:  0.00199127197265625

"""
8) Program to Remove duplicate words from Sentence
"""
#method 1
def remove_duplicate_words(x: str)->str:
    """
    Input: String
    Output: String
    Removes duplicates in string.
    """
    regex = r"\b(\w+)(?:\W+\1\b)+"
    return re.sub(regex, r"\1", x, flags=re.IGNORECASE)
print(remove_duplicate_words(f))
#Time taken:  0.0009930133819580078

"""
9) Program to Remove all characters except letters and numbers
"""
#1 method
def remove_non_characters(x: str)->str:
    """
    Input: String
    Output: String
    Removes everything that is not letters or numbers.
    """
    x = re.sub("[\W_]+","",x)
    return x
print(remove_non_characters(g))
#Time taken:  0.0019991397857666016

#Method 2 , non regex method using list comprehension
def remove_non_characters1(x: str)->str:
    """
    Input: String
    Output: String
    Removes everything that is not letters or numbers.
    """
    z = list([val for val in x if val.isalpha() or val.isnumeric()])
    return ''.join(z)
print(remove_non_characters1(g))
#Time taken:  0.0019943714141845703

#Method 3, non regex method instead of isaplha or isnumeric using isalnum()
def remove_non_characters2(x: str)->str:
    """
    Input: String
    Output: String
    Removes everything that is not letters or numbers.
    """
    z = list([val for val in x if val.isalnum()])
    return ''.join(z)
print(remove_non_characters2(g))
#Time taken:  0.000989675521850586

"""
10) Program to accept string ending with alphanumeric character
"""
#Method 1
def ending_alphanumeric(x: str)->str:
    """
    Input: String
    Output: String
    Gives Valid as answer when end of string is letter or a number
    """
    z = re.search("[A-Za-z0-9]$",x)
    return "Valid" if z else "Invalid"
print(ending_alphanumeric(h))
#Time taken:  0.0019960403442382812

"""
11) Program to accept string starting with vowel
"""
#Method 1
def start_vowel(x: str)->str:
    """
    Input: String
    Output: String
    Accepts string if it starts with vowel
    """
    z = re.search("^[aeiouAEIOU][A-Za-z-0-9]*",x)
    return "Valid" if z else "Invalid"
print(start_vowel(h))
#Time taken:  0.0009975433349609375

"""
12) Program to check if a string starts with a substring using regex
"""
#Method 1
def string_starts_substring(x: str,y: str)->str:
    """
    Input: String , Substring
    Output: String
    Checks if the substring is in the starting of the string
    """
    z = re.search("^{0}[A-Za-z-0-9]*".format(y),x)
    return "Valid" if z else "Invalid"
print(string_starts_substring(j,e))
#Time taken:  0.0019927024841308594

#Method 2
def string_starts_substring1(x: str,y: str)->str:
    """
    Input: String , Substring
    Output: String
    Checks if the substring is in the starting of the string
    """
    y = "^"+y
    z = re.search(y,x)
    return "Valid" if z else "Invalid"
print(string_starts_substring1(j,e))
#Time taken:  0.0009975433349609375

"""
13) Program to Check if an URL is valid or not using Regular Expression
"""
#From GOG
def isValidURL(str: str):
    """
    Input: String
    Output: Boolean
    Checks if the URL are valid or not
    """
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False
print(isValidURL(url))
#Time taken:  0.001008749008178711

"""
14) Program for Parsing and Processing URL
"""
#From GOG
def URL_parse(x: str):
    a = re.findall('(\w+)://',x)
    b = re.findall('://www.([\w\-\.]+)',x)
    return "Hostname: ",b,"\n Protocol: ",a
print(URL_parse(url))
#Time taken:  0.0009968280792236328

"""
15) Program to Check if email address valid or not
"""
def isValidemail(str: str):
    """
    Input: String
    Output: Boolean
    Checks if the Email are valid or not
    """
    regex = (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return "Valid Email"
    else:
        return "Invalid Email"
print(isValidemail(email))
#Time taken:  0.0009975433349609375

"""
16) Program to find files having a particular extension
"""
def file_extension(x: list):
    """
    Input: String
    Output: String
    This finds the given file extension from the list of files.
    """
    for file in x:
        # search given pattern in the line 
        match = re.search("\.xml$", file)
    
        # if match is found
        if match:
            return("The file ending with .xml is:",file)
print(file_extension(filenames))
#Time taken:  0.000997304916381836

"""
17) Program to check the validity of a Password
"""
#from GOG
def password_check(x: str):
    """
    Input: String
    Output: String
    Checks if the password passes all the conditions
    """
    flag = 0
    while(True):
        if(len(x)<8):
            flag = -1
            break
        elif not re.search("[a-z]",x):
            flag = -1
            break
        elif not re.search("[A-Z]",x):
            flag = -1
            break
        elif not re.search("[0-9]",x):
            flag = -1
            break
        elif not re.search("[_@$]",x):
            flag = -1
            break
        elif re.search("\s",x):
            flag = -1
            break
        else:
            return "Valid Password"
            break
    if flag == -1:
        return "Invalid Password"
print(password_check(password))
#Time taken:  0.0009927749633789062

"""
18) Program to Categorize Password as Strong or Weak using Regex in Python
"""
#From GOG
# Minimum 9 characters and maximum 20 characters.
# Cannot be a newline or a space
# There should not be three or more repeating characters in a row.
# The same string pattern(minimum of two character length) should not be repeating.
def password_categorize(x):
    #If password is newline or space
    if x == '\n' or x == " ":
        return "Password Cannot be a newline or space"
    if 9<=len(x)<=20:
        #if character repeated 3 times or more consecutively
        if re.search(r"(.)\1\1",x):
            return "Weak Password: Password cannot repeat three or more times in a row"
        #if substring is rereated
        if re.search(r"(..)(.*?)\1",x):
            return "Weak Password: Same pattern repeated in Password"
        else:
            return "Strong Password"
    else:
        return "Password length must be in 9-20 Characters"
print(password_categorize(password))
#Time taken:  0.0009965896606445312