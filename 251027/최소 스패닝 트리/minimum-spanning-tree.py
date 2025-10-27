# 251027 (13:38)
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# mst 
edges.sort(key=lambda x : x[-1])
arr=list(range(n+1))
edge_cnt=0
weight_sum=0

def find(x):   
    global arr 
    if arr[x]==x:
        return x 
    root = find(arr[x])
    arr[x]=root 
    return root 

def union(a,b):
    global arr 
    a_p,b_p=find(a),find(b)
    if a_p==b_p:
        return 
    elif a_p<b_p:
        arr[b_p]=a_p
    else:
        arr[a_p]=b_p 

for a,b,w in edges:
    if edge_cnt==n+1:
        break
    if find(a)==find(b):
        continue 
    union(a,b)
    weight_sum+=w 
    edge_cnt+=1 

print(weight_sum)