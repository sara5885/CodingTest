n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
bombs=[]
ans=0
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            bombs.append((i,j))
bomb_type_arr=[0]*len(bombs)
# Please write your code here.
def count_bomb():
    global bomb_type_arr,ans
    bombed=[[0 for _ in range(n)] for _ in range(n) ]
    for i in range(len(bombs)):
        x,y=bombs[i]
        bomb_type=bomb_type_arr[i]
        bombed[x][y]=1 
        if bomb_type==1:
            for dx,dy in ((-2,0),(-1,0),(1,0),(2,0)):
                nx,ny=x+dx,y+dy 
                if 0<=nx<n and 0<=ny<n :
                    bombed[nx][ny]=1 

        elif bomb_type==2:
            for dx,dy in ((0,-1),(-1,0),(1,0),(0,1)):
                nx,ny=x+dx,y+dy 
                if 0<=nx<n and 0<=ny<n :
                    bombed[nx][ny]=1 
        elif bomb_type==3:
            for dx,dy in ((-1,-1),(-1,1),(1,-1),(1,1)):
                nx,ny=x+dx,y+dy 
                if 0<=nx<n and 0<=ny<n :
                    bombed[nx][ny]=1 

    cnt =0
    for row in bombed:
        cnt+=sum(row)
    ans=max(cnt,ans)

def solve(k):
    if k==len(bombs):
        count_bomb()
        return 
    for i in range(1,4): # bomb type 은 1~3
        bomb_type_arr[k]=i #k번째 bomb의 bomb type 
        solve(k+1)
    

solve(0)
print(ans)