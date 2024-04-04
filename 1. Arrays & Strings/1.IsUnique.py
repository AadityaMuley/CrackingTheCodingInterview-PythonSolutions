# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def func1(s):
    s = ''.join(sorted(s))
    
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    
    return True

def func2(s):
    check = set()
    
    for i in s:
        if i in check:
            return False
        else:
            check.add(i)
    
    return True

s = "asdfghjkl"
print(func1(s))