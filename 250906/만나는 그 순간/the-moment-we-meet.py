n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
location_per_sec1=[]
location_per_sec2=[]
location_per_sec1.append(500000)
location_per_sec2.append(500000)
now_loc=500000
for i in range(n):
    tmp_d=d[i] #direction
    tmp_t=t[i] #time 
    if d[i]=='L': 
        for j in range(tmp_t):
            location_per_sec1.append(now_loc-1)
            now_loc-=1
    elif d[i]=='R':
        for j in range(tmp_t):
            location_per_sec1.append(now_loc+1)
            now_loc+=1
now_loc=500000
for i in range(m):
    tmp_d=d2[i] #direction
    tmp_t=t2[i] #time 
    if d2[i]=='L': 
        for j in range(tmp_t):
            location_per_sec2.append(now_loc-1)
            now_loc-=1
    elif d2[i]=='R':
        for j in range(tmp_t):
            location_per_sec2.append(now_loc+1)
            now_loc+=1
#print(location_per_sec1)
#print(location_per_sec2)
ans=-1
for i in range(1, min(len(location_per_sec1),len(location_per_sec2))):
    if location_per_sec1[i]==location_per_sec2[i]:
        ans=i
        break
    
print(ans)