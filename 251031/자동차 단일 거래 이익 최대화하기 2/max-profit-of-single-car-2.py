# 251031 (12:45)
n = int(input())
price = list(map(int, input().split()))

min_price=price[0]
max_profit=0

for i in range(1,n):
    if min_price>price[i]:
        min_price=price[i]
    else:
        profit=price[i]-min_price
        if profit>max_profit:
            max_profit=profit 

print(max_profit)