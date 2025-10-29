# 251029 (18:39) 
from sortedcontainers import SortedSet
n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
s=SortedSet()

for x,y in points:
    s.add((x,y))

for x,y in queries:
    if s.bisect_left((x,y))==len(s):
        print(-1,-1)
    else:
        tmp_x,tmp_y=s[s.bisect_left((x,y))]
        print(tmp_x,tmp_y)