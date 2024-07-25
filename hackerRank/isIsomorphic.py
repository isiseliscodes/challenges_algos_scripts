def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    
    ordnum = 0
    isodict = {}
    last_ord = 0
    for i in range(len(s)):
        ordnum = ord(s[i]) - ord(t[i])
        if ordnum != last_ord and i== 0:
            return False
        else:
            last_ord = ordnum
        isodict[ordnum] += 1

    print(isodict)
    for key, value in isodict.items():
        if value != len(s):
            return False
    return True 