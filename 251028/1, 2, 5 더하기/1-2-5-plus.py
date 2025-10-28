# 251028 (20:09)
n = int(input())

# Please write your code here.
A=[1,2,5]

# dp[i] : 정수 i를 A의 원소들로 나타낼 수 있는 방법의 수 
# dp[i]=dp[i-1]+dp[i-2]+dp[i-5]
# for j in range(3):
    # dp[i]+=dp[i-A[j]]

# min, max 가 아님 
dp=[0]*(n+1)
dp[0]=1


for i in range(1,n+1):
    for j in range(len(A)):
        if i>=A[j]:
            dp[i]+=dp[i-A[j]]%10007

print(dp[n])