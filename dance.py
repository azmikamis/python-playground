__author__ = 'azmi'

t = int(raw_input())
for _ in range(t):
    m, n = map(int, raw_input().split())
    boysheights = sorted(map(int, raw_input().split()))
    girlsheights = sorted(map(int, raw_input().split()))

    possible = True
    for a, b in zip(boysheights, girlsheights):
        if b > a:
            possible = False
            break

    print 'YES' if possible else 'NO'