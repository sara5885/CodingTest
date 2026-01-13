# 260106 (21:07)
# 260112 (12:06)

n = int(input())
parent = list(map(int, input().split()))
k = int(input())
visited=[0]*(n)
removed_node=[0]*(n)

graph=[[] for _ in range(n)]
for i in range(n):
    p_num=parent[i]
    graph[p_num].append(i)
# for i in graph:
#     print(i)
removed_node[k]=1 

def count_leaf(node):
    if node is None:
        return 0 
    if removed_node[node]:
        return 0
    if not graph[node]: #empty 
        return 1 
    else:
        cnt=0
        for child in graph[node]:
            cnt+=count_leaf(child)
        return cnt 


ans=count_leaf(0)
print(ans)
