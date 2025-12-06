#251206 (12:37)
N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.
grid=[[0 for _ in range(N)] for _ in range(M+1)]
for c in range(N):
    grid[0][c]=-1 
# 불가능한 곳은 -1로 설정 
for c in range(N):
    if clothes[c][0]!=1:
        grid[1][c]=-1 




for i in range(1,M+1): #해당 날짜
    for j in range(N): #해당 옷 
        if not clothes[j][0]<=i<=clothes[j][1]:
            grid[i][j]=-1
            continue 
        max_value=0
        # dp 계산해야 하는 것들 
        for k in range(N):
            # grid값이 -1이면 pass 
            if grid[i-1][k]==-1:
                continue 
            tmp_value=grid[i-1][k]+abs(clothes[j][2]-clothes[k][2])
            max_value=max(max_value,tmp_value)
        grid[i][j]=max_value


# for i in range(M+1):
#     for j in range(N):
#         print(grid[i][j],end=" ")
#         # dp[i][j]=
#     print()

ans=0
for j in range(N):
    ans=max(ans,grid[M][j])
print(ans)
