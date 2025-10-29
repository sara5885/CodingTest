#251029 (18:46)
from sortedcontainers import SortedSet 
n, m = map(int, input().split())
queries = list(map(int, input().split()))

s=SortedSet(range(1,m+1))
for q in queries:
    s.remove(q)
    print(s[-1])