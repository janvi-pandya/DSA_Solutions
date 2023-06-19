#
# PROBLEM EXPLANATION
# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it 
# reads the same forward and backward. Alphanumeric characters include letters and numbers
# 

#!/bin/python3

import string

#
# Completed the 'solve' function below.
#
# The function is expected to return a STRING "YES" or "NO".
# The function accepts 2 STRINGs s,t as parameter.
#

def solve(s):
    s=s.lower()
    atoz=string.ascii_lowercase
    alphanumeric=['0','1','2','3','4','5','6','7','8','9']
    for i in atoz:
        alphanumeric.append(i)
    for i in s:
        if i not in alphanumeric:
            s=s.replace(i,"")
    if s==s[::-1]:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(str(result))