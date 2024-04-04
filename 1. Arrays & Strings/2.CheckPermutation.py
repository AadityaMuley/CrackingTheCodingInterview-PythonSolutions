# Given two strings,write a method to decide if one is a permutation of the other.

def func1(s1, s2):
    str1 = dict()
    str2 = dict()
    
    for i in range(len(s1)):
        if s1[i] not in str1:
            str1[s1[i]] = 1
        else:
            str1[s1[i]] += 1
        if s2[i] not in str2:
            str2[s2[i]] = 1
        else:
            str2[s2[i]] += 1
    
    return str1 == str2

def func2(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    
    return True

s1 = "hello"
s2 = "leloh"
print(func1(s1, s2))