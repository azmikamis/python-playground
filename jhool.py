__author__ = 'azmi'

t = int(raw_input())
for _ in range(t):
    s = raw_input()
    totallen = str(len(s))
    i, j, k = s.split('.')
    jhoollen = str(len(''.join([c for c in j if c not in 'aeiou']) + '.' + k))
    print '{0}/{1}'.format(jhoollen, totallen)