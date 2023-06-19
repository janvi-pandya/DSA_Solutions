#
# PROBLEM EXPLANATION
# Given an array of integers nums which is sorted in ascending order, and
# an integer target , write a function to search target in nums . If target
# exists, then return its index. Otherwise, return -1 .
# You must write an algorithm with 0(log n) runtime complexity.
#

#!/bin/python3

#
# Completed the 'binarySearch' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l starting index
#  2. INTEGER r ending index
#  3. INTEGER_ARRAY arr
#  4. INTEGER search searching element
# 

def binarySearch(l, r, arr, search):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == search:
            return mid
        elif arr[mid] < search:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().split()))
    search= int(input().strip())
    result = binarySearch(0, n-1, arr, search)
    print(result)
