n, m = map(int, input().split())

loc_per_sec1=[]
loc_per_sec2=[]
now_loc=500000
loc_per_sec1.append(now_loc)
loc_per_sec2.append(now_loc)

# Process robot A's movements
t = []
d = []

for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)
    if direction=='L':
        for i in range(int(time)):
            now_loc-=1
            loc_per_sec1.append(now_loc)
    elif direction=='R':
        for i in range(int(time)):
            now_loc+=1
            loc_per_sec1.append(now_loc)

# Process robot B's movements
t_b = []
d_b = []
now_loc=500000
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)
    if direction=='L':
        for i in range(int(time)):
            now_loc-=1
            loc_per_sec2.append(now_loc)
    elif direction=='R':
        for i in range(int(time)):
            now_loc+=1
            loc_per_sec2.append(now_loc)
rev_cnt=0


for i in range(2,min(len(loc_per_sec1),len(loc_per_sec2))):
    if loc_per_sec1[i-1]!=loc_per_sec2[i-1] and loc_per_sec1[i]==loc_per_sec2[i]:
        rev_cnt+=1

# compute remain movement 
# if len(loc_per_sec1)>len(loc_per_sec2):
#     long_robot=loc_per_sec1
#     short_robot=loc_per_sec2
#     short_last=short_robot[-1]
#     # start idx : len(short_robot)
#     for i in range(len(short_robot),len(long_robot)):
#         if long_robot[i-1]!=short_last and long_robot[i]==short_last:
#             rev_cnt+=1

# elif len(loc_per_sec1)<len(loc_per_sec2):
#     long_robot=loc_per_sec2
#     short_robot=loc_per_sec1
#     short_last=short_robot[-1]
#     for i in range(len(short_robot),len(long_robot)):
#         if long_robot[i-1]!=short_last and long_robot[i]==short_last:
#             rev_cnt+=1
if len(loc_per_sec1)!=len(loc_per_sec2):
    if len(loc_per_sec1)>len(loc_per_sec2):
        long_robot=loc_per_sec1
        short_robot=loc_per_sec2
    else:
        long_robot=loc_per_sec2
        short_robot=loc_per_sec1
    short_last=short_robot[-1]
    for i in range(len(short_robot),len(long_robot)):
        if long_robot[i-1]!=short_last and long_robot[i]==short_last:
            rev_cnt+=1


print(rev_cnt)