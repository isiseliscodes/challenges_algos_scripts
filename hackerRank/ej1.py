 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
* separate positive, negative, zero
* print proportions in that order
'''
def percentage_to_decimal(count, length):
    percentage = ( count * 100 ) / length
    #print(percentage)
    return float("{:.6f}".format(percentage / 100))

def plusMinus(arr):
    pos = neg = zeroes = 0
    
    # Write your code here
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zeroes += 1
            
    print(percentage_to_decimal(pos, len(arr)))
    print(percentage_to_decimal(neg, len(arr)))
    print(percentage_to_decimal(zeroes, len(arr)))                 
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

