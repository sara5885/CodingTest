#251027 (15:02)
n, m = map(int, input().split())
type_arr = input().split()
edges = [tuple(map(int, input().split())) for _ in range(m)]
arr=list(range(n+1))
# kruskal- unionfind 
# weight sorting 
# 조건 : 다른 종류 
# n-1이 될때까지 
edges.sort(key=lambda x: x[-1])
edge_cnt=0
weight_sum=0
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
    else:
        arr[a_p]=b_p 

for i in range(m):
    if edge_cnt==n-1:
        break 
    a,b,w=edges[i]
    if type_arr[a-1]==type_arr[b-1]:
        continue 
    if find(a)==find(b):
        continue 
    union(a,b)
    weight_sum+=w 
    edge_cnt+=1 

if edge_cnt<n-1:
    print(-1)
else:
    print(weight_sum)