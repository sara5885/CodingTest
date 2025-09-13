# 250913 (23:43) ()

N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]
max_cnt=0
for i in range(N):
    new_P=P
    new_P[i]=new_P[i]//2 
    total_price=[0]*N
    for a in range(len(new_P)):
        total_price[a]=new_P[a]+S[a] 
    total_price.sort()
    total_budget=B
    idx=0
    cnt=0
    while True:
        if total_budget<total_price[idx]:
            break
        total_budget-=total_price[idx]
        idx+=1
        cnt+=1
    max_cnt=max(max_cnt,cnt)
        
print(max_cnt)
    