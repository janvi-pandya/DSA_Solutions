#
# PROBLEM EXPLANATION
# Given two strings s and t , return true if t is an anagram of s , and
# false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.
# 

#!/bin/python3

#
# Completed the 'isAnagram' function below.
#
# The function is expected to return a STRING "Anagram" or "Not Anagram".
# The function accepts 2 STRINGs s,t as parameter.
#

def isAnagram(s,t):
    if set(s)==set(t):
        return "Anagram"
    else:
        return "Not Anagram"

if __name__ == '__main__':
    s,t = input().split()
    result = isAnagram(s,t)

    print(result + '\n')