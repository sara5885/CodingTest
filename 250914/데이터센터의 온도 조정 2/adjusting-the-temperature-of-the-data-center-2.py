N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

max_work=0

for i in range(0,1001):
    tmp_work=0
    for j in range(len(ranges)):
        temp_a,temp_b=ranges[j]
        if i<temp_a:
            tmp_work+=C
        elif i>=temp_a and i<temp_b:
            tmp_work+=G
        else:
            tmp_work+=H 
    max_work=max(tmp_work,max_work)

print(max_work)
