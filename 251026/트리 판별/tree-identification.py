# 251026 (12:33)
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph=[[] for _ in range(10001)]
#누군가의 자식으로 이미 선정된 node 
child=set()
tree_flag=True 

for a,b in edges:
    if b in child:
        tree_flag=False 
        break
    graph[a].append(b)
    child.add(b)

if tree_flag:
    print(1)
else:
    print(0)