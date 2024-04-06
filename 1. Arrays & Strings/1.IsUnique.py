"""1.1 Is Unique"""
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def is_unique_1(s):
    """Function using sorting"""
    s = ''.join(sorted(s))
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

def is_unique_2(s):
    """Function using set"""
    check = set()
    for i in s:
        if i in check:
            return False
        else:
            check.add(i)
    return True

S = "asdfghjkl"
print(is_unique_1(S))
