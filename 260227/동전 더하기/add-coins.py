n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
idx = n-1
ans=0
while k > 0 :
    ans+=k//coins[idx]
    k=k%coins[idx]
    idx -=1 
print(ans)