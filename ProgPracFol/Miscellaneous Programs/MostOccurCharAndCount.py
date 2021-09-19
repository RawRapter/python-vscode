"""
Program to find the most occurring character and its count

Given a string, write a python program to find the most occurrence character and its number of occurrences.

Examples:

Input : hello
Output : ('l', 2)

Input : geeksforgeeks
Output : ('e', 4)
"""

def GetMaxChar(x):
    d = {key:x.count(key) for key in x}
    return max(d,key=d.get)
print(GetMaxChar("geeksforgeeks"))

from collections import Counter
  
def find_most_occ_char(input):
  
    wc = Counter(input)
    s = max(wc.values())
    i = wc.values().index(s)    
    print(wc.items()[i])