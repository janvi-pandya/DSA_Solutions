#
# PROBLEM EXPLANATION
# Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next number of days.
# Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. 
# Find what is the maximum profit you can obtain with an optimum trading strategy.
# 

#!/bin/python3

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    maximum_price=0
    maximum_profit=0
    for i in prices[::-1]:
        if i>maximum_price:
            maximum_price=i
        else:
            maximum_profit+=maximum_price-i
    return maximum_profit
        
    

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        print(str(result))
