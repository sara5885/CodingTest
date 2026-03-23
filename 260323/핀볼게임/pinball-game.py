#260320 
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dir={'U':0, 'D':1, 'L':2, 'R':3}
# 상(0),하(1),좌(2),우(3)
dic_dx,dic_dy=[-1,1,0,0],[0,0,-1,1]
# 종료조건 : out of range

def escape(sx,sy, idx):
    # sx,sy : 출발지점 , d: 출발 방향 
    cnt=0
    cx,cy = sx,sy
    
    # if grid[cx][cy]==1:
    #     idx=3-idx
    # elif grid[cx][cy]==2:
    #     idx=idx^2
    # visited.add((cx,cy,idx))
    while True:
        cnt+=1
        dx,dy = dic_dx[idx], dic_dy[idx]
        nx,ny = cx+dx,cy+dy 
        if not (0<=nx<n and 0<=ny<n):
            break 
        
        if grid[nx][ny]==1: 
            idx=3-idx 
        elif grid[nx][ny]==2:
            idx=idx^2 
        
        cx,cy = nx,ny   
    return cnt 
mx,my,mdir =0,0,0
ans =0 
for i in range(n): # 0,1,2,3,4
    tmp= escape (i,-1, dir['R'])
    if tmp>ans : 
        ans=tmp
        mx,my,mdir = i,-1,'R'
    tmp = escape (i,n,dir['L'])
    if tmp>ans : 
        ans=tmp
        mx,my,mdir = i,n,'L'
    tmp= escape(-1,i, dir['D'])
    if tmp>ans : 
        ans=tmp
        mx,my,mdir = -1,i,'D'
    tmp= escape(n,i, dir['U'])
    if tmp>ans : 
        ans=tmp
        mx,my,mdir = n,i,'U'

print(ans)
# print(mx,my,mdir)
