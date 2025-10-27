#251027 (12:41)
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 2)]

# 1. edge에 대한 모두 union
# 2. 두 graph에 대해 parent 구해서 union 두 parent 값 출력 

arr=list(range(n+1))
def find(x):
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
        _=find(b_p)
    else:
        arr[a_p]=b_p
        _=find(a_p)
for a,b in edges:
    union(a,b)


parent=set()
for i in range(1,n+1):
    parent.add(find(i))

x,y=parent
print(min(x,y),max(x,y))