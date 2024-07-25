#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        new_string = ""
        new_string = new_string.join(sorted(grid[i]))
        grid[i] = new_string


    for i in range(len(grid[0])):
        for j in range(len(grid)):
            for k in range(j+1, len(grid)):
                if grid[j][i] > grid[k][i]:
                    return "NO"
    return "YES"


print(gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]))
    