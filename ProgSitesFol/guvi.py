#First
i1 = str(input())
for i in i1:
    print(i, end=" ")

#Second
i1 = "anant"
for i in range(0,len(i1)):
    if i == len(i1) - 1:
        print(i1[i],end="")
    else:
        print(i1[i], end=" ")
for i in range(0,3):
    x = input()
    print(x)

#Third
tuples = [
    (-2.3391885553668246e-10, 8.473071450645254e-10),
    (-2.91634014818891e-10, 8.913956007163883e-10), 
    (-3.470135547671147e-10, 9.186162538099684e-10), 
    (-3.9905561869610444e-10, 8.425016542750256e-10), 
    (-4.4700997526371524e-10, 8.681513230068634e-10), 
    (-4.903967399792693e-10, 9.204845678073805e-10),
]
result = sum(t[0] for t in tuples)
print(result)

#Fourth
a,b = input().split()

if a > b:
    print(b)
else:
    print(a)

#Fifth
a = 'abc'
result = 0
for x in range(0,len(a)):
    result += ord(a[x])
print(result)

#Sixth
list1 = [1,2,3,4,5]
mapped_list = list(map(lambda x: 5*x, list1))
print(mapped_list)