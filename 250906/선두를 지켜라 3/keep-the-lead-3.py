N, M = map(int, input().split())

dist_per_time1=[0]
dist_per_time2=[0]
honor_history=[] #바뀔때만 추가 

# Process A's movements
v = []
t = []
now_dist1=0
now_dist2=0
for _ in range(N):
    # vi : velocity, ti: hour
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)
    for i in range(ti):
        now_dist1+=vi 
        dist_per_time1.append(now_dist1)


# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)
    for i in range(ti):
        now_dist2+=vi 
        dist_per_time2.append(now_dist2)

cnt=0 
for i in range(len(dist_per_time1)):
    #현재 선두 확인 -> 이전 선두랑 다르면 honor에 선두 기록 + cnt+=1
    if dist_per_time1[i]>dist_per_time2[i]:
        now_lead='A'
    elif dist_per_time1[i]<dist_per_time2[i]:
        now_lead='B'
    elif dist_per_time1[i]==dist_per_time2[i]:
        now_lead='AB'
    
    # 기록 초기화 
    if len(honor_history)==0:
        honor_history.append(now_lead)
    # 기록 초기 X & 선두 바뀌었을 때 
    elif honor_history[-1]!=now_lead:
        honor_history.append(now_lead)
        cnt+=1

print(cnt)