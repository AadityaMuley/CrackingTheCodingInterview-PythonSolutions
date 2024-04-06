# There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false

def func(s1, s2):
    diff = abs(len(s1) - len(s2))
    if diff > 1: 
        return False
    elif diff == 1:
        s1, s2 = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    
    i, j = 0, 0
    check = 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            check += 1
            if check > 1:
                return False
            
            if diff == 1:
                j += 1
                continue
        
        i += 1
        j += 1
    
    return True
        


s1 = "bake"
s2 = "pale"
print(func(s1, s2))
