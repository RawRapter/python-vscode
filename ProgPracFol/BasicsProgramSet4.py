"""
This Set is related to Matrix Programs in Python, Questions from geeks of Geeks
"""
L1 = [[2 ,1, 1],
 [5, 5, 5],
 [3, 3, 8]]
from math import sqrt
import numpy as np
from numpy.core.fromnumeric import transpose
"""
1) Basic program to add two Matrices
"""
#Method 1, Using numpy
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix3 = matrix1 + matrix2
print("First matrix: \n",matrix1)
print("Second Matrix: \n",matrix2)
print("Matrix1 + Matrix2: \n",matrix3)
#Time taken:  0.005991697311401367

#Method 2. Using Loop
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix3 = np.zeros((3,3))
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
print(matrix3)
#Time taken:  0.0031545162200927734

#Method 3, Using list comprehension
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix3 = [matrix1[i][j] + matrix2[i][j] for i in range(len(matrix1)) for j in range(len(matrix2))]
print(np.reshape(matrix3,(3,3)))
#Time taken:  0.0009968280792236328

#Method 4, using zip() and sum
# matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
# matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
# matrix3 = [map(sum,zip(*t)) for t in zip(matrix1,matrix2)]
# print(matrix3)

"""
2) Basic program to multiply two matrices
"""
#Method 1, Using numpy
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix3 = matrix1 * matrix2
print("First matrix: \n",matrix1)
print("Second Matrix: \n",matrix2)
print("Matrix1 * Matrix2: \n",matrix3)
#Time taken:  0.005980491638183594

#Method 2. Using Loop
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix3 = np.zeros((3,3))
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        matrix3[i][j] = matrix1[i][j] * matrix2[i][j]
print(matrix3)
#Time taken:  0.0049860477447509766

#Method 3, Using list comprehension
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix3 = [matrix1[i][j] * matrix2[i][j] for i in range(len(matrix1)) for j in range(len(matrix2))]
print(np.reshape(matrix3,(3,3)))
#Time taken:  0.0042514801025390625

"""
3) Basic program for Matrix Product
"""
#Method 1, same thing has been done in BasicsProgramSet2 Program 8 for Lists in different ways
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
print(matrix1)
result = np.prod(matrix1)
print(result)
#Time taken:  0.003002643585205078

#Method 2, try with list comprehension and function
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
def MatrixProd(x):
    ans = 1
    for i in x:
        ans *= i
    return ans
result = MatrixProd([i for j in matrix1 for i in j])
print(result)
#Time taken:  0.005983591079711914
#Note: for both the programs product can be zero if matrix randomly chooses 0 as any elements, don't get confused

"""
4) Adding and Subtracting Matrices in Python
"""
#Method 1, This can be done same as Program 1 of this Set, for other ways look for Program 1
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix3 = matrix1 + matrix2
matrix4 = matrix1 - matrix2
print("First matrix: \n",matrix1)
print("Second Matrix: \n",matrix2)
print("Matrix1 + Matrix2: \n",matrix3)
print("Matrix1 - Matrix2: \n",matrix4)
#Time taken:  0.00698089599609375

#Method 2, using add() and subtract() of numpy
matrix1 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix2 = np.random.randint(9, size=(3,3)) #Matrix can be given directly too I have created randomly
matrix3 = np.add(matrix1,matrix2)
matrix4 = np.subtract(matrix1,matrix2)
print(matrix3)
print(matrix4)
#Time taken:  0.002694845199584961

"""
5) Basic Transpose a matrix in Single line in Python
"""
#Method 1 , using transpose from numpy
transpose1 = transpose(L1)
print(transpose1)
#Time taken:  0.003000020980834961

#Method 2, list comprehension
transpose2 = [[L1[i][j] for i in range(len(L1))] for j in range(len(L1[0]))]
for i in transpose2:
    print(i)
#Time taken:  0.0030078887939453125

#Method 3, Using Zip
transpose3 = zip(*L1)
for i in transpose3:
    print(i)
#Time taken:  0.0019838809967041016

"""
6) Basic Matrix creation of n*n
"""
n = int(input("Enter value of N(Must be perfefct square): "))
matrix1 = [list(range(1 + n*i, 1+n*(i+1))) for i in range(n)]
print(matrix1)
#Time taken:  0.6289224624633789