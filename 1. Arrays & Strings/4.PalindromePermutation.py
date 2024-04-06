# Given a string, write a function to check if it is a permutation of a palin­drome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

def func(s):
    s = s.replace(" ", "")
    s = s.lower()
    check = set()
    for c in s:
        if c not in check:
            check.add(c)
        else:
            check.remove(c)
    
    if len(s) % 2 == 0:
        return True if len(check) == 0 else False
    else:
        return True if len(check) == 1 else False

s = "Tact Coa"
print(func(s))
