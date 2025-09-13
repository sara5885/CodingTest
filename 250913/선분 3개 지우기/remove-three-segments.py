# 250913 (23:35)
n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

not_meet_cnt=0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            # check meeting 
            check_comb=True 
            arr=[0]*101
            for idx in range(n):
                if idx==i or idx==j or idx==k:
                    continue 
                for tmp_idx in range(l[idx],r[idx]+1):
                    arr[tmp_idx]+=1
                    if arr[tmp_idx]>=2:
                        check_comb=False
                        break
            if check_comb==True:
                not_meet_cnt+=1
print(not_meet_cnt)

                