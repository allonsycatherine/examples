"""
Your initial happiness is 0. For each  integer in the array, 
if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness. 
Otherwise, your happiness does not change.
 Output your final happiness at the end.
"""

n, m = input().split()
arr1 = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happy = 0
for i in arr1:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
print(happy)
