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