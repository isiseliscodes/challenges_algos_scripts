
import math
import os
import random
import re
import sys

def ifFunction(n):
    if n % 2 == 0:
        return("Weird")

    elif n in range(2,6) or n > 20:
        return("Not Weird")
    
    elif n in range(6,21):
        return("Weird")
    


if __name__ == '__main__':
    n = 3
    

    result = ifFunction(n)
    print(result)