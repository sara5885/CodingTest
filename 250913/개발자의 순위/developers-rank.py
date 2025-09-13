# 250913 (23:18)
k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

cnt=0 
for i in range(1,n+1):
    for j in range(1,n+1): #개발자 combination
        if i==j:
            continue 
        track_cnt=0
        for track in arr:
            if track.index(i)<track.index(j):
                track_cnt+=1
        if track_cnt==k:
            cnt+=1

print(cnt)


