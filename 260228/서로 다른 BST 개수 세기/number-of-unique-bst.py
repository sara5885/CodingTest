n = int(input())

dp=[0]*(n+1)
dp[0]=1 
dp[1]=1
dp[2]=2

if n==1:
    print(1)
elif n==2: 
    print(2)
elif n==3:
    print(5)
else:
    for i in range(4,n+1):
        # dp[i]
        for j in range(i-1):
            k=i-j
            dp[i]+=dp[j]*dp[k]

    print(dp[n])
