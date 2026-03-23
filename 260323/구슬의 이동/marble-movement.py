# 260323 (13:28)

from collections import deque
n, m, T, k = map(int, input().split())

# jewels=[deque() for _ in range(m)]
jewels=[]
r, c, d, v = [], [], [], []
grid=[[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri)-1)
    c.append(int(ci)-1)
    d.append(di)
    v.append(int(vi))
    jewels.append([int(ri)-1,int(ci)-1,int(vi),i,di])
    grid[int(ri)-1][int(ci)-1].append((int(vi),i,di)) 


# 1초에 v만큼 움직임
# 방향바꿀 때 시간 소요 x

# 위치 겹쳤을 때 -> k개 이상이면 
    #우선순위로 밑에 구슬삭제 : 우선순위(속도, 번호)

# t마다 새로운 grid로 update
dir={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
opp={'R':'L','L':'R','U':'D','D':'U'}
for t in range(T):
    
    # print("[",t,"s]")
    # new_grid에 모든 구슬의 위치 업데이트
    # 구슬 list로 하나씩 update
    new_jewels=[]
    new_grid=[[[] for _ in range(n)] for _ in range(n)]
    need_to_remove=set() #(r,c)
    while jewels:
        jewel=jewels.pop()
        tr,tc,tv,ti,td = jewel
        cx,cy = tr,tc 
        for _ in range(tv):
            dx,dy = dir[td]
            nx,ny=cx+dx, cy+dy 
            if 0<=nx<n and 0<=ny<n :
                cx,cy=nx,ny 
            else:
                nx,ny=cx-dx, cy-dy 
                td=opp[td]
                cx,cy=nx,ny 
        tr,tc=cx,cy 
        new_grid[tr][tc].append((tv,ti,td))
        if len(new_grid[tr][tc])>k:
            need_to_remove.add((tr,tc))
        new_jewels.append([tr,tc,tv,ti,td])
       
    # print(new_jewels)
    # for row in new_grid:
    #     for col in row:
    #         print(col,end=" ")
    #     print()
    
    # print("before removing (jewels)")
    # print(new_jewels)
    # 겹치는 구슬들 있으면 -> 조건에 따라 제거 (need_to_remove)
    for cx,cy in need_to_remove:
        # cx,cy에 해당하는 구슬들
        tmp=new_grid[cx][cy]
        tmp.sort(key=lambda x:(-x[0],-x[1]))
        new_tmp=tmp[:k]
        removed_tmp=tmp[k:]
        new_grid[cx][cy]=new_tmp
        #tv,ti,td=new_grid[tr][tc]
        for cv,ci,cd in removed_tmp:
            new_jewels.remove([cx,cy,cv,ci,cd])
    
    # print("after removing")
    # print(new_jewels)
    # for row in new_grid:
    #     for col in row:
    #         print(col,end=" ")
    #     print()
    # print()
    need_to_remove=set()
    jewels=new_jewels 
    grid=new_grid

print(len(jewels))