# 251026 (12:33)
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph=[[] for _ in range(10001)]
#누군가의 자식으로 이미 선정된 node 
child=set()
tree_flag=True 
node=[]
root_cand=[]
for a,b in edges:
    if a not in child and a not in root_cand:
        root_cand.append(a)
    if b in child:
        tree_flag=False 
        break
    if b in root_cand:
        root_cand.remove(b)
    graph[a].append(b)
    child.add(b)
    node.append(a)
    node.append(b)

# print(root_cand)
if len(root_cand)!=1:
    tree_flag=False 

if tree_flag:
    print(1)
else:
    print(0)