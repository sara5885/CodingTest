# 250921 (03:07)
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
idx=len(coins)-1
coin_cnt=0
while k>0:
    if coins[idx]<k:
        coin_cnt+=k//coins[idx]
        k%=coins[idx]
    idx-=1 
print(coin_cnt)
