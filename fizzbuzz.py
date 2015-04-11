__author__ = 'azmi'

t = int(raw_input())
nums = map(int, raw_input().split())

for n in nums:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print 'FizzBuzz'
        elif i % 3 == 0:
            print 'Fizz'
        elif i % 5 == 0:
            print 'Buzz'
        else:
            print i
