#
# PROBLEM EXPLANATION
# Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.
# Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
#

#!/bin/python3

#
# Completed the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==m:
                return [(i+1),(j+1)]
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(' '.join(map(str, result)))
