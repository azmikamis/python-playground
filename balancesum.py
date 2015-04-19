__author__ = 'azmi'


t = int(raw_input())
for _ in range(t):
    l = map(int, raw_input().split())[1:]
    res = 0
    if len(l) > 1:
        for i in range(len(l)-1):
            if sum(l[:i+1]) == sum(l[i+1:]):
                res = i+1
                break
    print res
