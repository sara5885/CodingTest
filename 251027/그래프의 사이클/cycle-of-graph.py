#251027 (13:11)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
arr=list(range(n+1))
cnt=0
cycle_flag=False 

def find(x):
    global arr 
    if arr[x]==x:
        return x 
    root=find(arr[x])
    arr[x]=root 
    return root 

def union(a,b):
    global arr 
    a_p=find(a)
    b_p=find(b)
    if a_p==b_p:
        return 
    elif a_p<b_p:
        arr[b_p]=a_p
    else:
        arr[a_p]=b_p

for a,b in edges:
    cnt+=1
    if find(a)==find(b):
        cycle_flag=True 
        break 
    union(a,b)

if cycle_flag:
    print(cnt)
else:
    print("happy")
