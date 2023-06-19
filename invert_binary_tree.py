#
# PROBLEM EXPLANATION
# Given the root of a binary tree, invert the tree, and return its root
# 

#!/bin/python3

def printInOrder(root):
    stack = [1]
    result = []
    while stack :
        i = stack.pop()
        if i > 0 :
            if root[i][1] > 0 : 
                stack.append(root[i][1])
            stack.append(-i)
            if root[i][0] > 0 : 
                stack.append(root[i][0])
        else :
            result.append(-i)
    return result

#
# Completed the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
def swapNodes(indexes, queries):
    indexes=[None] + indexes
    output=[]
    for q in queries:
        toVisit, depth = [1], 1
        while toVisit :
            if depth % q == 0 :
                for i in toVisit :
                    indexes[i] = (indexes[i][1], indexes[i][0])
            toVisit_ = []
            for i in toVisit :
                if indexes[i][0] > 0 :
                    toVisit_.append(indexes[i][0])
                if indexes[i][1] > 0 :
                    toVisit_.append(indexes[i][1])
            toVisit = toVisit_
            depth += 1
        output.append(printInOrder(indexes))
    return output    

if __name__ == '__main__':
    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print('\n'.join([' '.join(map(str, x)) for x in result]))