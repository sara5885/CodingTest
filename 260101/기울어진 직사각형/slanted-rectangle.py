n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dir=0
dx=[-1,-1,1,1]
dy=[1,-1,-1,1]
ans=0

def get_score(i,j,h,w):
    len=[h,w,h,w]
    score=0
    cx,cy=i,j
    for dir in range(4): # direction을 막혔을 때 바뀌는게 아니고 해당 길이만큼 갔을 때 바꾸는 것 
        c_len=len[dir]
        for _ in range(c_len):
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
                score=get_score(i,j,h,w)
                ans=max(ans,score)


print(ans)  
