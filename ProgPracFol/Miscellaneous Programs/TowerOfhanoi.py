""" Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 
1) Only one disk can be moved at a time. 
2) Each move consists of taking the upper disk from one of the stacks 
and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack. 
3) No disk may be placed on top of a smaller disk.
Note: Transferring the top n-1 disks from source rod to Auxiliary rod can again be thought of as a fresh problem
and can be solved in the same manner. """

def TowerOfHanoi(n: int, source, destination, auxilary):
    if n==1:
        print("Move Disk 1 from source ",source," to destination ",destination)
        return
    TowerOfHanoi(n-1,source,auxilary,destination)
    print("Move Disk",n,"from source ",source," to destination ",destination)
    TowerOfHanoi(n-1,auxilary,destination,source)

n = 4
TowerOfHanoi(n,"A","B","C")