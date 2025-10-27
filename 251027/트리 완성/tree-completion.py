# 251027 (13:18)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# cycle 없애기 
# edge마다 find(a)==find(b) 조건으로 제거 / 추가? 
arr=list(range(n+1))
cycle=0
def find(x):
    global arr 
    if arr[x]==x:
        return x 
    root=find(arr[x])
    arr[x]=root 
    return root 

def union(a,b):
    a_p,b_p=find(a),find(b)
    if a_p==b_p:
        return 
    elif a_p<b_p:
        arr[b_p]=a_p
    else:
        arr[a_p]=b_p 

for a,b in edges :
    if find(a)==find(b):
        cycle+=1 
        continue 
    union(a,b)

graph_set=set()
for i in range(1,n+1):
    graph_set.add(find(i))

print(cycle+len(graph_set)-1)

        
