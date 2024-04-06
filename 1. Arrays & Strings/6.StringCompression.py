#Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2blc5a3. 
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).


def compress(s):
    ans = ""
    curr = s[0]
    freq = 0

    for i, c in enumerate(s):
        freq += 1
        if i + 1 == len(s) or c != s[i+1]:
            ans += c + str(freq)
            freq = 0

    return ans


S = input()
print(compress(S))
