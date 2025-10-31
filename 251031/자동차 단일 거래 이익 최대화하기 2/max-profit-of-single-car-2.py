# 251031 (12:45)
n = int(input())
price = list(map(int, input().split()))

max_diff=0
for i in range(n-1):
    for j in range(i+1,n):
        if price[j]-price[i]>0:
            max_diff=max(max_diff,price[j]-price[i])
print(max_diff)