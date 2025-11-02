#251102 (11:42)
import sys 
INT_MIN=-sys.maxsize
A = input()
B = input()
A=" "+A
B=" "+B
n=len(A)-1
m=len(B)-1

dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][1]=i 
for j in range(m+1):
    dp[1][j]=j 

for i in range(1,n+1):
    for j in range(1,m+1):
        if A[i]==B[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
print(dp[n][m])