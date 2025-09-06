n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx,dy=[1,0,-1,0],[0,-1,0,1]
x,y=0,0

# if dir=='E':
#     nx,ny=x+dx[0],y+dy[0]
# elif dir=='S':
#     nx,ny=x+dx[1],y+dy[1]
# elif dir=='W':
#     nx,ny=x+dx[2],y+dy[2]
# elif dir=='N':
#     nx,ny=x+dx[3],y+dy[3]

dir_idx={'E':0, 'S':1, 'W':2, 'N':3}


for i in range(n):
    idx=dir_idx[dir[i]]
    n=dist[i]
    x,y=x+n*dx[idx],y+n*dy[idx]
    # print(f"idx:{i}, (x,y):({x,y})")

print(x,y)