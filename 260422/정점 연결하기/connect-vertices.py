import sys
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 2)]

parent=list(range(n+1))
# 조건에 만족하는 간선이 많다면, 가장 앞선 순서쌍 
def find(node):
    if parent[node]==node:
        return node
    par=find(parent[node])
    parent[node]=par
    return par 

def union(a,b):
    A=find(a)
    B=find(b)
    if A<=B: #B를 A에 결속 
        parent[B]=A 
    else : 
        parent[A]=B 

for a,b in edges:
    union(a,b)

ans=set()
for i in range(1,n+1):
    ans.add(find(i))

if len(ans)!=2:
    print("error")
else:
    print(min(ans), max(ans))