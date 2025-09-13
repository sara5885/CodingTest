#250913 (11:27)
N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

max_cnt=0

arr=sorted(P)

# 모든 조합 
for i in range(N):
    total=B
    tmp_cnt=0
    # i의 선물을 반값 할인 받음 
    # 이 때 선물 가능 최대 명수 
    for j in range(N):
        if i==j:
            if total>=P[j]//2:
                total-=P[j]//2
                tmp_cnt+=1
            else:
                break
        else:
            if total>=P[j]:
                total-=P[j]
                tmp_cnt+=1
            else:
                break 
        
        
    max_cnt=max(max_cnt,tmp_cnt)
    
print(max_cnt)