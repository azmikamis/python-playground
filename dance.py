__author__ = 'azmi'


def checkpossibility(bh, gh):
    if len(gh) < len(bh):
        return False

    if bh[0] <= gh[0]:
        return False

    for a, b in zip(bh, gh):
        if b > a:
            return False

    return True

t = int(raw_input())
for _ in range(t):
    m, n = map(int, raw_input().split())
    boysheights = sorted(map(int, raw_input().split()))
    girlsheights = sorted(map(int, raw_input().split()))

    possible = checkpossibility(boysheights, girlsheights)

    print 'YES' if possible else 'NO'