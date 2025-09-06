n, m = map(int, input().split())

dist_per_hour1=[0]
dist_per_hour2=[0]

# Process A's movements
v = []
t = []
dist1=0
dist2=0
# 1 2 (시속 1km로 2시간)
# 4 1 (시속 4km로 1시간) 
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)
    for i in range(ti):
        dist1+=vi
        dist_per_hour1.append(dist1)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)
    for i in range(ti):
        dist2+=vi
        dist_per_hour2.append(dist2)


rev_cnt=0
leader=''


for i in range(1,len(dist_per_hour1)):
    if dist_per_hour1[i]>dist_per_hour2[i]:
        tmp_leader='A'
    elif dist_per_hour1[i]<dist_per_hour2[i]:
        tmp_leader='B'
    else :
        continue
    if tmp_leader!=leader:
        if leader!='':
            rev_cnt+=1
        leader=tmp_leader

print(rev_cnt)