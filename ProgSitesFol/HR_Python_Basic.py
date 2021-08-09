#Note: Please run seperately dont run this file
import textwrap
"""
Question 1: Given the names and grades for each student in a class of N students, store them in a nested list
and print the name(s) of any student(s) having the second lowest grade.
"""
python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] #this is example to input
#Method 1
if __name__ == '__main__':
    python_students =[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score])
    list2 = sorted(python_students,key = lambda x:x[1])
    list2.pop(0)
    Minlist = min(list2,key = lambda x:x[1])
    list2 = sorted(list2)
    for i in range(len(list2)):
        if list2[i][1] == Minlist[1]:
            print(list2[i][0])

#Method 2
if __name__ == '__main__':
    python_students =[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score])
    sortedlst = sorted(list(set(x[1] for x in python_students)))
    secondlow = sortedlst[1]
    finallisr = []
    for i in python_students:
        if secondlow == i[1]:
            finallisr.append(i[0])
    for i in sorted(finallisr):
        print(i)

"""
Question 2: Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = 0
    count = 0
    for i in student_marks[query_name]:
        result += i
        count += 1
    result1 = result/count
    print('%.2f'%result1)

"""
Question 3: Basic List program having multiple commands
"""
if __name__ == '__main__':
    N = int(input())
    #All the commands in dictionary
    commands = {
        "insert": lambda a,b,c: a.insert(b,c),
        "print": lambda a : print(a),
        "remove": lambda a,b:a.remove(b),
        "append": lambda a,b:a.append(b),
        "sort": lambda a:a.sort(),
        "pop": lambda a:a.pop(),
        "reverse": lambda a:a.reverse()
    }
    output=[] #empty list
    for i in range(N):
        a = input() #Commands input
        splita = a.split(" ") #spliting commands
        #compand text part
        command = splita[0]
        try:#commands with 3 input
            commands[command](output,int(splita[1]),int(splita[2]))
        except IndexError:
            try:#commands with 2 inputs
                commands[command](output,int(splita[1]))
            except IndexError: #commands with 1 input
                commands[command](output)

"""
Question 4: Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits,
lowercase and uppercase characters.
"""
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

"""
Question 5: task is to wrap the string into a paragraph of given width.
"""
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    return "\n".join(word_list)

"""
Question 6: Floor mat design
"""
n,m = map(int,input().split())
#Abovepart
for i in range(1,((n-1)//2)+1):
    print(((2*i-1)*".|.").center(m,'-'))
#Middlepart
print("WELCOME".center(m,'-'))
#belowpart
for i in range(((n-1)//2),0,-1):
    print(((2*i-1)*".|.").center(m,'-'))

"""
Question 6: String formatting
"""
def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1,number+1):
        d = str(i)
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
        print(d.rjust(w),o.rjust(w),h.rjust(w),b.rjust(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

"""
Question 7: Alphabet Rangoli
"""
def print_rangoli(size):
    # All characters
    characters="abcdefghijklmnopqrstuvwxyz"
    #creating list of characters
    data = [characters[i] for i in range(n)]
    #creating index
    item = list(range(n))
    #getting desired patter like 32123
    item = item[:-1]+item[::-1]
    for i in item:
        #getting alphabets
        temp = data[-(i+1):]
        #getting desired pattern alphabet
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


"""
Question 8: Counter in collections, number of shoes , all size of shoes given sum the amount.
"""
from collections import Counter
int(input())
sizes = list(map(int,input().split()))
money = 0
stocks = Counter(sizes)
for i in range(int(input())):
    o,p = list(map(int,input().split()))
    if stocks[o]:
        money += p
        stocks[o] -= 1
print(money)


"""
Question 9: DefaultDictionary in collections , two group check index of B group element in A, if doesnt exist then return -1
"""
from collections import defaultdict
b1,b2 = list(map(int,input().split()))
d = defaultdict(list)
for i in range(b1):
    d[input()].append(i+1)
for i in range(b2):
    print(*d[input()] or [-1])

"""
Question 10: NamedTuple in collections, ID marks clas names of student stored get the average marks
"""
from collections import namedtuple
n = int(input())
Score = namedtuple("Score",input().split())
scores = [Score(*input().split()).MARKS for i in range(n)]
print(round((sum(map(int,scores))/n),2))

"""
Question 11: Ordered Dictionary in Collections, supermarket sales
"""
from collections import OrderedDict
n = int(input())
ordered_dictionary = OrderedDict({})
for i in range(n):
    x = input().split(' ')
    y = int(x[-1])
    x.pop()
    x1 = ' '.join(x)
    if x1 in ordered_dictionary:
        ordered_dictionary[x1] += y
    else:
        ordered_dictionary[x1] = y
for i,j in ordered_dictionary.items():
    print(i,j)

"""
Question 12: Set operations
"""
n = int(input())
s = set(map(int, input().split()))
noc = int(input())
commands = {
    "pop" : lambda a:a.pop(),
    "remove" : lambda a,b:a.remove(b),
    "discard" : lambda a,b : a.discard(b)
}
for i in range(noc):
    z = input()
    z1 = z.split()
    command = z1[0]
    try:
        commands[command](s,int(z1[1]))
    except IndexError:
        commands[command](s)
print(sum(s))

"""
13) Polar coordinates of complex number using cmath
"""
import cmath
z = complex(input())
for i in cmath.polar(z):
    print(i)

"""
14) Weekday in caps of specific date
"""
import datetime as dt
import calendar
n = input()
weekday = dt.datetime.strptime(n,"%m %d %Y").weekday()
print((calendar.day_name[weekday]).upper())

"""
15) Exception Program
"""
n = int(input())
for i in range(n):
    n1,n2 = input().split()
    try:
        print(int(n1)//int(n2))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as v:
        print("Error Code:",v)

"""
16) Set Symmetric Difference
"""
x = input()
y = map(int,input().split())
x1 = input()
y1 = map(int,input().split())
z = set(y)
z1 = set(y1)
z2 = z.symmetric_difference(z1)
z2 = list(z2)
z2.sort()
for i in z2:
    print(i)

"""
17) itertools combination
"""
from itertools import combinations
x,y = input().split()
x = list(x)
x.sort()
for i in range(1,int(y)+1):
    z = list(combinations(x,i))
    for j in z:
        print(''.join(j))