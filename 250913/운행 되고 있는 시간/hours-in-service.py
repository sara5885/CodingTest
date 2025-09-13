n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

total_max_time=0

for i in range(n):
    total_time=0
    for j in range(n):
        if i==j: 
            continue 
        total_time+=b[j]-b[i]
    total_max_time=max(total_max_time,total_time)

print(total_max_time)
        