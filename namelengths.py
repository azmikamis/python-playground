__author__ = 'azmi'


t = int(raw_input())
for _ in range(t):
    totalstudents, studentspercamp = map(int, raw_input().split())
    totalcamps = totalstudents / studentspercamp
    d = {}
    for _ in range(totalstudents):
        n = len(raw_input())
        if n not in d.keys():
            d[n] = 1
        else:
            d[n] += 1
    if len(d) > totalcamps:
        print 'Not possible'
    elif sum([x/studentspercamp for x in d.values()]) != totalcamps:
        print 'Not possible'
    else:
        print 'Possible'