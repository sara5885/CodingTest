n, q = map(int, input().split())
dest = [int(input()) for _ in range(q)]

# graph 만들기
graph=[[] for  _ in range(n+1)]
visited=[0]*(n+1)
c_node=1
while True:
    if 2*c_node<=n: 
        graph[c_node].append(2*c_node)
    else: break
    if 2*c_node+1<=n:
        graph[c_node].append(2*c_node+1)
    else:
        break
    c_node+=1 

# print(c)

for d in dest:
    tmp=d 
    path=[]
    while tmp>0:
        path.append(tmp)
        tmp=tmp//2 
    path.reverse()
    tmp_ans=0
    # print(path)
    for p in path:
        # print("visited[p]:",visited[p])
        if visited[p]: 
            tmp_ans=p
            # print("tmp_ans:",tmp_ans)
            break
    if tmp_ans==0:
        visited[d]=1 # ****

    print(tmp_ans)
