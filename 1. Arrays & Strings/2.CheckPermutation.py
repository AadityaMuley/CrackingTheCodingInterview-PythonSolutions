# Given two strings,write a method to decide if one is a permutation of the other.

def func1(s1, s2):
    str1 = dict()
    str2 = dict()
    
    for i, c in enumerate(s1):
        if c not in str1:
            str1[c] = 1
        else:
            str1[c] += 1
    
    for i, c in enumerate(s2):
        if c not in str2:
            str2[c] = 1
        else:
            str2[c] += 1
    
    return str1 == str2

def func2(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            return False
    
    return True

S1 = "hello"
S2 = "leloh"
print(func1(S1, S2))
