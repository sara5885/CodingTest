# 251027 (21:45)
n = int(input())
memo=[-1]*(n+1)
def square(n):
    if memo[n]!=-1:
        return memo[n]
    if n==1:
        memo[1]=2
        return memo[1]
    if n==2:
        memo[2]=7
        return memo[2]
    if n==3:
        memo[3]=22
        return memo[3]
    memo[n]=2*square(n-1)+3*square(n-2)+2*square(n-3)
    return memo[n]

print(square(n)%1000000007)