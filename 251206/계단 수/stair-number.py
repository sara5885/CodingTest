
n = int(input())

# Please write your code here.
dp=[[0 for _ in range(10)] for _ in range(n)]
for i in range(10):
    if i==0:
        dp[0][i]=0
    else:
        dp[0][i]=1 
# for i in range(10):
#     print(dp[0][i],end=" ")
# print()

for i in range(1,n):
    for j in range(10):
        if j==0:
            dp[i][j]=dp[i-1][j+1]
        elif j==9:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=dp[i-1][j-1] + dp[i-1][j+1]


# for i in range(n):
#     for j in range(10):
#         print(dp[i][j],end=" ")
#     print()
ans=0
for j in range(10):
    ans+=dp[n-1][j]
print(ans%(10**9 + 7))