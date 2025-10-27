#251027 (15:11)
n, m = map(int, input().split())

horizontal = [list(map(int, input().split())) for _ in range(n)]
vertical = [list(map(int, input().split())) for _ in range(n - 1)]

edges=[]

#node : (i,j)
# for i in range(n):
#     for j in range(n-1):
#         edges.append(((i,j),(i,j+1),))

for i in range(len(horizontal)):
    # horizontal[i] : [20,5]
    for j in range(len(horizontal[i])):
        edges.append(((i,j),(i,j+1),horizontal[i][j]))

# print(vertical)
for i in range(len(vertical)):
    # vertial[i]: [1,4,1]
    for j in range(len(vertical[i])):
        edges.append(((i,j),(i+1,j),vertical[i][j]))

edges.sort(key=lambda x:x[-1])
# print(edges)

grid=[[None for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        grid[i][j]=(i,j)
edges_cnt=0
weight_sum=0

def find(x,y):
    if grid[x][y]==(x,y):
        return x,y 
    tmp_x,tmp_y=grid[x][y]
    root_x,root_y=find(tmp_x,tmp_y)
    grid[x][y]=(root_x,root_x)
    return root_x,root_y

def union(ax,ay,bx,by):
    ax_p,ay_p=find(ax,ay)
    bx_p,by_p=find(bx,by)
    if (ax_p,ay_p)==(bx_p,by_p):
        return 
    elif ax_p<bx_p or (ax_p==bx_p and ay_p<by_p):
        grid[bx_p][by_p]=(ax_p,ay_p)
    else:
        grid[ax_p][ay_p]=(bx_p,by_p)

for a,b,w in edges:
    if edges_cnt==n*m-1:
        # print(edges_cnt, n*m-1)
        break 
    a_x,a_y=find(a[0],a[1])
    b_x,b_y=find(b[0],b[1])
    if a_x==b_x and a_y==b_y:
        continue 
    # print("union:",a,b,w)
    union(a_x,a_y,b_x,b_y)
    edges_cnt+=1
    weight_sum+=w 
# for row in grid:
#     for col in row:
#         print(col,end=" ")
#     print()
print(weight_sum)