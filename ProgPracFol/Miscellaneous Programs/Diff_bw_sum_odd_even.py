"""
Question from GFG

Program for Difference between sums of odd and even digits

Given a long integer, we need to find if the difference between sum of odd digits and sum of even digits is 0 or not. The indexes start from zero (0 index is for leftmost digit).

Examples:

Input : 1212112
Output : Yes
Explanation:-
the odd position element is 2+2+1=5
the even position element is 1+1+1+2=5
the difference is 5-5=0.so print yes.

Input :12345
Output : No
Explanation:-
the odd position element is 1+3+5=9
the even position element is 2+4=6
the difference is 9-6=3 not  equal
to zero. So print no.
"""
#Above question is same as asking if the number is divisible by 11.
def diff_sum(n):
    if(n%11 == 0):
        return "Yes difference is 0"
    return "No difference is not 0"

print(diff_sum(1212112))