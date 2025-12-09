# 251208 (13:16)
from collections import deque 

N = int(input())

value=N
cnt =0
q=deque()
q.append(value)
parent=[-1]*1000001
parent[N]=N

while q:
    tmp=q.popleft()
    if tmp==1: 
        break 
    # 1 : tmp-=1
    # 2 : tmp+=1
    # 3 : if tmp%2==0 : tmp=tmp//2 
    # 4 : if tmp%3==0: tmp=tmp//3 
    if tmp-1 >=1 and parent[tmp - 1] == -1:
        q.append(tmp-1)
        parent[tmp-1]=tmp
    if tmp+1<=1000000 and parent[tmp + 1] == -1:
        q.append(tmp+1)
        parent[tmp+1]=tmp 
    if tmp%2==0 and parent[tmp//2] == -1:
        q.append(tmp//2)
        parent[tmp//2]=tmp 
    if tmp%3==0 and parent[tmp//3] == -1:
        q.append(tmp//3)
        parent[tmp//3]=tmp 
    

v=1
cnt=0
while parent[v]!=v:
    cnt+=1 
    v=parent[v]
print(cnt)