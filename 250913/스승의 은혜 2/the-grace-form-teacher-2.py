#250913 (11:27)
#  반값할인받을 i의 반값가격으로 arr에 저장해야함  
N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

max_cnt=0

# 모든 조합 
for i in range(N):
    total=B
    tmp_cnt=0
    arr=[]
    for j in P:
        arr.append(j)
    arr[i]=arr[i]//2
    arr.sort()
    for j in arr:
        if total<j:
            break
        else:
            total-=j
            tmp_cnt+=1
    max_cnt=max(max_cnt,tmp_cnt)
    
print(max_cnt)