#251027 (11:46)
# 왜 이 알고리즘은 union-find를 하는가 
import sys
sys.setrecursionlimit(100001)
n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

parent_arr=list(range(n+1))

def find(x):
    if parent_arr[x]==x:
        return x 
    root=find(parent_arr[x])
    parent_arr[x]=root 
    return root 

def union(a,b):
    a_p=find(a)
    b_p=find(b)
    if a_p<=b_p:
        parent_arr[b_p]=a_p
    else:
        parent_arr[a_p]=b_p
for a,b in edges:
    # union 
    union(a,b)

s=find(path[0])
check=True 
for node in path:
    if s!=find(node):
        check=False 
        break 

if check:
    print(1)
else:
    print(0)
