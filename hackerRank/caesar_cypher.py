#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def move_formula(char, k):
    ordnum = ord(char)
    k = k % 26 if (k > 26) else k
    if char.isupper():
        ordnum = ordnum + k if ordnum + k <= 90 else ordnum - 26 + k

    elif char.islower():
        ordnum = ordnum + k if ordnum +k <= 122 else ordnum - 26 + k
    
    return ordnum


def caesarCipher(s, k):
    # Write your code here
    new_string = ""
    for i in range(0,len(s)):
        if s[i].isalpha():
            new_ord = move_formula(s[i], k)
            new_string = new_string + chr(new_ord)
            # new_string = new_string + move_formula(s[i], k)
        else:
            new_string = new_string + s[i]    

    return new_string
            



s = "!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U"
#s = "abcdefghijklmnopqrstuvwxyz"
expected_output = "!w-bL`-yX!.G`mVKmFlX/MaCyyvSS!CSwts.!g/`He`eJk1DGZBa`eBLdyu`hZD`vV-jZDm.LCBSre..-!.!dmv!-E"

result = caesarCipher(s, 62)

if result == expected_output:
    print("PASS")
else:
    print("FAIL")
    print(result)
    print(expected_output)