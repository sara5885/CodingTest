# 260318 

N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# L(+1), R(-1)
idx=0

cx,cy = N//2, N//2 
# print(cx,cy)
ans=board[cx][cy]
dx,dy=[-1,0,1,0],[0,-1,0,1]
for dir in str:
    if dir == 'L':
        idx = (idx+1)%4
    elif dir=='R':
        idx = (idx+3)%4
    else:
        nx,ny=cx+dx[idx],cy+dy[idx]
        if 0<=nx<N and 0<=ny<N :
            # print(board[nx][ny])
            ans+=board[nx][ny]
            cx,cy=nx,ny 

    
print(ans)