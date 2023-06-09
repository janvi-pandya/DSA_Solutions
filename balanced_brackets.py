#
# PROBLEM EXPLANATION
# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().
#

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Completed the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack=[]
    opening=['{','[','(']
    clossing=['}',']',')']
    for i in s:
        if i in opening:
            stack.append(i)
        elif i in clossing:
            if len(stack)==0:
                return "NO"
            if opening.index(stack.pop())!= clossing.index(i):
                return "NO"
    if len(stack)==0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')
