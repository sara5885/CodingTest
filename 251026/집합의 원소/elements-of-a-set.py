# 251026 (19:05)
n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

arr=list(range(n+1))

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
    if a_p<b_p:
        arr[b_p]=a_p 
    else:
        arr[a_p]=b_p


for num,a,b in query :
    if not num:#1 : union
        if find(a)!=find(b):
            union(a,b)
    else: # 0
        if find(a)==find(b):
            print(1)
        else:
            print(0)
