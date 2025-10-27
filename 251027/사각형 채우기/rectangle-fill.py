# 251027 (21:33)
n = int(input())
memo=[-1]*(n+1)
def square(n):
    if memo[n]!=-1:
        return memo[n]
    if n==1:
        memo[1]=1
        return memo[1]
    elif n==2:
        memo[2]=2
        return memo[2]
    # elif n==3:
    #     memo[3]=3
    #     return memo[3]
    memo[n]=square(n-1)+square(n-2)
    return memo[n]

print(square(n))
