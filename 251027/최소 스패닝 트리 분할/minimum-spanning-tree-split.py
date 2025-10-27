# 251027 (17:27)
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 그래프분할
# - root node가 2개가 되는 경우 
# if len(root)>1: #분할됨 
roots=set()
arr=list(range(n+1))
edges.sort(key=lambda x:x[-1])
edges_cnt=0
weight_sum=0
def find(x):
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

weight_list=[]
for a,b,w in edges:
    if edges_cnt==n-1:
        break
    if find(a)==find(b):
        continue 
    union(a,b)
    edges_cnt+=1
    weight_sum+=w 
    weight_list.append(w)

weight_list.sort()
weight_sum-=weight_list[-1]
print(weight_sum)


