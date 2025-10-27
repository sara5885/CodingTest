#251027 (13:44) 
n, m = map(int, input().split())
a, b = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
from_v, to_v, satisfaction = zip(*edges)

edge_cnt=0
arr=list(range(n+1))
edges.sort(key=lambda x :-x[-1])
satis=[]

def find(x):
    global arr 
    if arr[x]==x:
        return x 
    root=find(arr[x])
    arr[x]=root 
    return root 

def union(a,b):
    global arr 
    a_p,b_p=find(a),find(b)
    if a_p==b_p:
        return 
    elif a_p<b_p:
        arr[b_p]=a_p
    else :
        arr[a_p]=b_p 

for i in range(m):
    s,e,w=edges[i]
    if edge_cnt==n+1:
        break
    if find(s)==find(e):
        break
    union(s,e)
    print(s,e, find(s),find(e))
    print(arr)
    edge_cnt+=1 
    satis.append(w)

print(edges)
print(satis)
satis.sort()
print(satis[0])