# 251028 (21:01)
n = int(input())
profit = list(map(int, input().split()))

# dp[i] : 길이가 i일 때 얻을 수 있는 최대 수익 
# dp[0]:0 

dp=[-1]*(n+1)
dp[0]=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j and dp[i-j]!=-1:
            dp[i]=max(dp[i], dp[i-j]+profit[j-1])

max_val=0
for val in dp:
    max_val=max(val,max_val)

print(max_val)