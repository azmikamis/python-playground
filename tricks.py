import random

__author__ = 'azmi'

import collections
import itertools
import heapq

# Named tuples
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1.0, y=2.0)
print p, p.x, p.y

# Double ended queue
q = collections.deque()
q.append(0)
q.append(1)
q.appendleft(-1)
print q
q.pop()
q.popleft()
print q
q.extend([1, 2, 3, 4, 5])
q.rotate(3)
print q
q.rotate(-3)
print q

# Default dictionaries
m = collections.defaultdict(int)
print m['a']
m = collections.defaultdict(str)
print m['a']
m = collections.defaultdict(lambda: 'default')
print m['a']
m = collections.defaultdict(itertools.count().next)
print m['a'], m['b']

# heapq
a = [random.randint(0, 100) for __ in xrange(100)]
print heapq.nsmallest(5, a)
print heapq.nlargest(5, a)
