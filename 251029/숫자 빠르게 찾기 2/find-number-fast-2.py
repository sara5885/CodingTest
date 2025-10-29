# 251029 (18:28)
from sortedcontainers import SortedSet 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

s=SortedSet(arr)

for q in queries:
    if s.bisect_left(q)==len(s):
        print(-1)
    else:
        print(s[s.bisect_left(q)])
    

