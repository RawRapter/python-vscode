"""
Question from GFG
Program for Program to Print Matrix in Z form

Given a square matrix of order n*n, we need to print elements of the matrix in Z form

Examples:
Input : mat[][] =  {1, 2, 3,
                    4, 5, 6,
                    7, 8, 9}
Output : 1 2 3 5 7 8 9

Input : mat[][] = {5, 19, 8, 7,
                   4, 1, 14, 8,
                   2, 20, 1, 9,
                   1, 2, 55, 4}
Output: 5 19 8 7 14 20 1 2 55 4
"""
arr = [[4, 5, 6, 8], 
        [1, 2, 3, 1], 
        [7, 8, 9, 4], 
        [1, 8, 7, 5]]

arr1 = [[4, 5, 6], 
        [1, 2, 3], 
        [7, 8, 9]]

arr2 = [[4, 5, 6, 8, 9], 
        [1, 2, 3, 1, 10], 
        [7, 8, 9, 4, 11], 
        [1, 8, 7, 5 ,12],
        [13, 14, 15, 16]]

def Z_matrix(n):
    j = 1
    print(len(n))
    for i in range(len(n)):
        print(n[0][i], end=" ")

    for i in range(len(n)-2,0,-1):
        print(n[j][i],end=" ")
        j += 1

    for i in range(0,len(n)):
        print(n[len(n)-1][i], end=" ")

Z_matrix(arr2)