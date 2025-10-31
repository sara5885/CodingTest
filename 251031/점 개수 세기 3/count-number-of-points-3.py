#251031 (14:42)
from sortedcontainers import SortedSet 
n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

nums=SortedSet(points)
mapper=dict()
cnt=1 
for num in nums:
    mapper[num]=cnt 
    cnt+=1 

for a,b in queries:
    na,nb=mapper[a],mapper[b]
    print(nb-na+1)