n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans=0
dx=[-1,-1,1,1]
dy=[1,-1,-1,1]
def get_score(i,j,h,w):
    # start idx : i,j
    score=0
    move_cnt=[h,w,h,w]
    cx,cy=i,j
    # 순서대로 이동 
    for dir in range(4): #
        len=move_cnt[dir]
        for _ in range(len): # h or w 길이만큼 
            nx,ny=cx+dx[dir], cy+dy[dir]
            if not (0<=nx<n and 0<=ny<n):
                return -1 
            score+=grid[nx][ny]
            cx,cy=nx,ny
    return score 

for i in range(n):
    for j in range(n):
        for h in range(1,n):
            for w in range(1,n):
                ans=max(ans,get_score(i,j,h,w))
print(ans)