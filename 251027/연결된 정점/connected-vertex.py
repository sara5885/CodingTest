#251027 (12:12)
n, m = map(int, input().split())

operations = []
for _ in range(m):
    op, *nums = input().split()
    if op == "x":
        a, b = map(int, nums)
        operations.append((op, a, b))
    else:
        a = int(nums[0])
        operations.append((op, a))

arr=list(range(n+1))
size=[1]*(n+1)
graph=[[] for _ in range(n+1)]
def find(x):
    global arr 
    if arr[x]==x:
        return x 
    root=find(arr[x])
    arr[x]=root 
    return root 

def union(x,y):
    global arr 
    a_p=find(a)
    b_p=find(b)
    if a_p==b_p:
        return

    elif a_p<b_p:
        arr[b_p]=a_p 
        size[a_p]+=size[b_p]
        # _=find(b)
    else:
        arr[a_p]=b_p 
        size[b_p]+=size[a_p]
        # _=find(a)

for i in range(m):
    if len(operations[i])==2:
        _,a=operations[i]
        a_p=find(a)
        print(size[a_p])
    else:
        _,a,b=operations[i]
        union(a,b)
