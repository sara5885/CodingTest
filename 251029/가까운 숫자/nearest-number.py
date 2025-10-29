#251029 (18:56)
from sortedcontainers import SortedSet 
n = int(input())
queries = list(map(int, input().split()))

s=SortedSet([0])
for q in queries:
    s.add(q)
    min_dist=s[1]-s[0]
    for i in range(1,len(s)-1):
        min_dist=min(min_dist,s[i+1]-s[i])
    print(min_dist)

        