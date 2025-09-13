n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

total_max_time=0
for i in range(n):
    arr=[0]*1001
    for j in range(n):
        if i==j:
            continue 
        for k in range(a[j],b[j]):
            arr[k]=1 
    total_time=sum(arr)
    total_max_time=max(total_max_time,total_time)

print(total_max_time)

