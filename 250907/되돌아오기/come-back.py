N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
cnt=0
dx,dy=[0,0,1,-1],[1,-1,0,0]
idx={'E':0, 'W':1,'S':2, 'N':3}

n_dx,n_dy=0,0
find_flag=False 
for i in range(N):
    n_dir=dir[i]
    n_dist=dist[i]

    for j in range(n_dist): # 1초당 1거리 
        n_dx,n_dy=n_dx+dx[idx[n_dir]], n_dy+dy[idx[n_dir]]
        cnt+=1 
        if n_dx==0 and n_dy==0:
            find_flag=True
            break
    if find_flag==True:
        break
        
if find_flag==False:
    print(-1)
else:
    print(cnt)

