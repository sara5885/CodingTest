# 250913 (11:19)
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

cnt=0
for i in range(n):
    # i번째 선분이 다른 모든 선분과 겹치지 않으면 cnt+=1
    tmp_cnt=0
    for j in range(n):
        if i==j:
            continue 
        # lines[i][0], lines[i][1] 
        if (lines[i][0]>lines[j][0] and lines[i][1]>lines[j][1]) or (lines[i][0]<lines[j][0] and lines[i][1]<lines[j][1]):
            tmp_cnt+=1
        else:
            break
    if tmp_cnt==n-1:
        cnt+=1

    
print(cnt)