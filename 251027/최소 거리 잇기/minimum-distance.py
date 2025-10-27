#251027 (16:00)
import math 
n, m = map(int, input().split())

x = [-1]
y = [-1]
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
arr=list(range(n+1))
edges = [tuple(map(int, input().split())) for _ in range(m)]

# i-th node : x[i],y[i]
# print(edges)
# print(x)
# print(y)
edges_cnt=len(edges)
dist_sum=0
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

def dist(a,b):
    ax,ay=float(x[a]),float(y[a])
    bx,by=float(x[b]),float(y[b])
    return math.sqrt((ax-bx)**2+(ay-by)**2)

for a,b in edges:
    a_p,b_p=find(a),find(b)
    if a_p==b_p:
        continue 
    union(a,b)
    # edges_cnt+=1 
    # dist_sum+=dist(a,b)

# connecting 
add_edges=[]
for i in range(1,len(x)-1):
    for j in range(i+1,len(x)):
        if (i,j) not in edges:
            add_edges.append((i,j,dist(i,j)))
add_edges.sort(key=lambda x : x[-1])

# print(add_edges)

for a,b,d in add_edges:
    if edges_cnt==n-1:
        break 
    if find(a)==find(b):
        continue 
    union(a,b)
    dist_sum+=d 
    edges_cnt+=1

print(f"{dist_sum:.2f}")


