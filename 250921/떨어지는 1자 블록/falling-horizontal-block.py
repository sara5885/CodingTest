# 250921 (23:35) 
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
for i in range(k-1,k+m-1):
    grid[0][i]=1

row_idx=0
while True :
    # 더이상 내려갈 곳 없으면 break
    if row_idx==n-1: #######여기 오류 
        break
    check_flag=True 
    for i in range(k-1,k+m-1):
        # grid[0][1] -> grid[1][1]
        # grid[0][2]-> grid[1][2] 
        if grid[row_idx+1][i]!=0:
            check_flag=False 
            break 
    if check_flag==True:
        row_idx+=1
        for i in range(k-1,k+m-1):
            grid[row_idx-1][i]=0
            grid[row_idx][i]=1 
    else:
        break

for row in grid:
    print(*row)