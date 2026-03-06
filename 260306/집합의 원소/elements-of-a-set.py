# 260306 (20:18)

n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]
arr=list(range(n+1))

def union(a,b):
    par_a = find(a)
    par_b=find(b)
    arr[par_a]=par_b
def find(num):
    if arr[num]==num:
        return num
    root_node=find(arr[num])
    arr[num]=root_node
    return root_node

for num,a,b in query:
    if num==0:
        if find(a)!=find(b):
            union(a,b)
    elif num==1:
        if find(a)==find(b):
            print(1)
        else:
            print(0)
