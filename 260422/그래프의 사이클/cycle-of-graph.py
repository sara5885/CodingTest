n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
parent=list(range(n+1))
# 사이클이 생기는 시점 - union하려고 했는데 이미 조상이 같을 때
def find(node):
    if parent[node]==node:
        return node 
    par=find(parent[node])
    parent[node]=par 
    return par 

found=False 
for i in range(m):
    a,b=edges[i]
    A=find(a)
    B=find(b)
    if A==B:
        found=True 
        print(i+1)
        break
    else:
        if A<=B:
            parent[B]=A 
        else:
            parent[A]=B


if not found:
    print("happy")