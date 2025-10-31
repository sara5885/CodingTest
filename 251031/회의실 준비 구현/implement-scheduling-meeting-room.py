# 251031 (12:14)
n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x:x[1])
cnt=0
tmp_e=0
for s,e in meetings:
    if s>=tmp_e:
        cnt+=1
        tmp_e=e 
print(cnt)