
def isSubstring(s1, s2):

    # Only compare the characters
    for i, _ in enumerate(s1):
        if i + len(s2) < len(s1) and s2 == s1[i:i+len(s2)]:
            return True

    return False
    
# if s2 a consecutive substring of s1
print(isSubstring('abccde', 'bcc')) #True
print(isSubstring('abccde', 'abd')) #False