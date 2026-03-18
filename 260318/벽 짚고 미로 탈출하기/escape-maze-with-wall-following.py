# 260318

N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]
dx,dy = [0,-1,0,1],[1,0,-1,0]
idx=0
cx,cy = x,y 

cnt =0 
grid[x][y]=cnt

while True :
    cnt+=1
    if cnt>1 and (cx,cy)==(x,y): 
        cnt=-1
        break
    nx,ny = cx+dx[idx], cy+dy[idx]
    if not(1<=nx<=N and 1<=ny<=N) : 
        break # 탈출 조건 
    # step1 : 막혀있어 이동 불가능 
    if grid[nx][ny]=='#':
        # 이동은 안하고 방향만 조절 
        idx=(idx+1)%4 
        cnt-=1 
    else : # 이 방향으로 이동 가능 
        # step2 
        # case 1
        # if not(0<=nx<N and 0<=ny<N) : break # 탈출 조건 
        # 오른쪽 벽 => ㅅ상대적 
        if idx ==0 : wx,wy = nx+1,ny
        elif idx ==1 : wx,wy=nx,ny+1
        elif idx ==2 : wx,wy =nx-1,ny 
        else: wx,wy = nx,ny-1 
        # case 2 => out of range는 어떻게 하지 
        if 1<=wx<=N and 1<=wy<=N and grid[wx][wy]=='#':
            cx,cy = nx,ny 
            grid[cx][cy]=cnt
        else:
            cx,cy = nx,ny
            idx=(idx+3)%4
            grid[cx][cy]=cnt 
            nx,ny = cx+dx[idx], cy+dy[idx]
            cx,cy=nx,ny 
            cnt+=1
            grid[cx][cy]=cnt
    

    # 종료 조건 
print(cnt)
# for row in grid:
#     for col in row:
#         print(col,end=" ")
#     print()