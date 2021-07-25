#Note: Please run seperately dont run this file
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