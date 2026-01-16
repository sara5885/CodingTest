# 251026 (15:32)
from collections import deque
n, k = map(int, input().split())
sequence = list(map(int, input().split()))
root=-1 
k_idx=-1 
graph=[[] for _ in range(1000001)] 
leaf=deque()
# child=[[] for _ in range(n+1)]
c_node=-1
parent=-1 
depth=[]
root=sequence[0]
idx=0
depth.append([])
depth[idx].append(root)
leaf.append(root)
for i in range(1,n):
    if sequence[i]-1!=sequence[i-1]:
        idx+=1 
        depth.append([])
        c_node=leaf.popleft()
        graph[c_node].append(sequence[i])
    else:
        graph[c_node].append(sequence[i])
        # parent[sequence[i]]=c_node
    depth[idx].append(sequence[i])
    if sequence[i]==k : 
        parent=c_node
        k_idx=idx 
    leaf.append(sequence[i])
        # 1. 연속된 수 (+1)라서 얘네는 자식 됨? 
        # 2. 연속된 수가 아니다 sequence[i]+1!=sequence[i+1]
            # 

# 정답 
# p=parent[node]
# print(k, k_idx, depth[k_idx])
# print(len(depth[k_idx])-1) # : node의 부모의 graph list의 갯수 (본인 제외)
# for i in depth:
#     print(i)

# 그냥 dfs 할까
ans=0
visited=set()
def dfs(node,target,len):
    global ans 
    for i in graph[node]:
        if i in visited:
            continue 
        visited.add(i)
        dfs(i,target,len+1)
     