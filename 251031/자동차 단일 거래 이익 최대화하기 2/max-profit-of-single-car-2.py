# 251031 (12:45)
n = int(input())
price = list(map(int, input().split()))
arr=[]
for i in range(n-1):
    for j in range(i+1,n):
        if price[j]-price[i]>0:
            arr.append(price[j]-price[i])
if len(arr)==0:
    print(0)
else:
    arr.sort()
    print(arr[-1])
