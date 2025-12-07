# 251207 (14:32)
n = int(input())
l, m, r = [], [], []
grid=[[0 for _ in range(3)] for _ in range(n)]
dp=[[[0,-1] for _ in range(3)] for _ in range(n)]
for i in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)
    grid[i][0]=left
    grid[i][1]=mid
    grid[i][2]=right

for j in range(3):
    dp[0][j]=[grid[0][j],j]

for i in range(1,n):
    for j in range(3):
        # dp[i][j]
        for k in range(3):
            if j==k: continue 
            if i==n-1 and j==dp[i-1][k][1]: continue 
            if dp[i-1][k][0]+grid[i][j]>dp[i][j][0]:
                dp[i][j]=[dp[i-1][k][0]+grid[i][j],k]
            # dp[i][j]=max(dp[i-1][k]+grid[i][j],dp[i][j])

ans=0
for j in range(3):
    ans=max(ans, dp[n-1][j][0])
print(ans)

