#251031 (14:42)
from sortedcontainers import SortedSet 
n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

nums=SortedSet()
for point in points:
    nums.add(point)

for a,b in queries:
    e=nums.bisect_right(b)
    s=nums.bisect_left(a)
    print(e-s)
