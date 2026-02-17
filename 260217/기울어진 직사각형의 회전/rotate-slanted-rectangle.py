# 260217 (14:52)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# dir : 회전 방향 (1시계/0반시계)
# r,c : starting point
r, c, m1, m2, m3, m4, dir = map(int, input().split())
r-=1
c-=1
# new_grid : 나머지는 다 그대로. 움직여진 값들만 수정 
# if dir: #tlrP 
#     dx,dy=[-1,-1,1,1],[-1,1,1,-1]
# else:
#     dx,dy=[-1,-1,1,1],[1,-1,-1,1]

dx,dy=[-1,-1,1,1],[1,-1,-1,1]
cr,cc=r,c 
m=[m1,m2,m3,m4]
tmp_value1=grid[cr][cc]
tmp_value2=0 
for idx in range(4): # 각 다이아몬드 방향별 (총 4개)
    # c_dx,c_dy=dx[idx],dy[idx] 
    for len_cnt in range(m[idx]): # 한 변의 길이
        
        nr,nc=cr+dx[idx], cc+dy[idx] #그다음 step 
        # print("현재 위치:",nr,nc)
        # 오류나면 여기에 out of index debugging 해보기
        if dir: # 시계방향 => cc,cr=nc,nr 
            grid[cr][cc]=grid[nr][nc]
        else: # 반시계방향 => nc,nr=cc,cr 
            tmp_value2=grid[nr][nc]
            grid[nr][nc]=tmp_value1
            tmp_value1=tmp_value2
        
        cr,cc=nr,nc
        # print("현재 위치:",cr,cc)


if dir:
    # print("마지막위치:",cr,cc)
    # print("tmp_value:",tmp_value1)
    grid[cr-1][cc-1]=tmp_value1
else:
    grid[r][c]=grid[nr][nc]


for row in grid:
    for col in row:
        print(col,end=" ")
    print()
    