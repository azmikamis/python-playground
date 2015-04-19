__author__ = 'azmi'

letters = {}
res = ""
s = list(raw_input().replace(" ", ""))
for c in s:
    if c not in letters.keys():
        letters[c] = 1
    else:
        letters[c] += 1
for c in s:
    if letters[c] == 1:
        res = c
        break
print res