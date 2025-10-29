# 251029 (11:45)
n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

for s,e in segments:
    cnt=0
    for p in points:
        if s<=p<=e:
            cnt+=1 
    print(cnt)