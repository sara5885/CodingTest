n = int(input())
arr = list(map(int, input().split()))

n_sorted=True 
for i in range(n):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            tmp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=tmp 
            n_sorted=False 
    if n_sorted==True:
        break 

for i in arr:
    print(i,end=" ")