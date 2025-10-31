# 251031 (15:47)
n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

arr=[0]*(200001)
min_idx=200001
max_idx=-1 
for s,e in intervals:
    arr[s]+=1
    arr[e]-=1 
    if s<min_idx:
        min_idx=s 
    if e>max_idx:
        max_idx=e 

ans=0
for i in range(min_idx,max_idx+1):
    cnt=sum(arr[:i])
    if cnt>ans:
        ans=cnt 
print(ans)