"""
You are given a string S. 
Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X, c) in the string.
"""
from itertools import groupby
S = input()
l = []
for k, v in groupby(S):
    t = (len(list(v)), int(k))
    l.append(t)
print(*l)
