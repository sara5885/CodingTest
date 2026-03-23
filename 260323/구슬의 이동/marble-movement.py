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
        
        if td == 'R':
            tmp=(tc+tv)//(n-1)
            if tmp%2!=0:
                td='L'
                tc=(n-1)-((tc+tv)%(n-1))
            else:
                tc=(tc+tv)%(n-1)

        elif td=='L':
            # 핑퐁없이 그대로 tc에서 빼기 
            if tc>=tv:
                tc=tc-tv 
            # tv가 더 커서 핑퐁함 
            else:  
                tmp=(tc-tv)//(n-1)
                if tmp%2!=0:
                    td='R'
                tmp2=(tv-tc)%(n-1)
                if td=='R':
                    tc=tmp2
                else:
                    tc=(n-1)-tmp2
        elif td=='U':
            if tr>=tv:
                tr=tr-tv
            else:
                tmp=(tv-tr)//(n-1)
                if tmp%2!=0:
                    td='U'
                tmp2=(tv-tr)%(n-1)
                if td=='U':
                    tr=tmp2
                else:
                    tr=(n-1)-tmp2 
        elif td=='D':
            tmp=(tr+tv)//(n-1)
            if tmp%2!=0:
                td='U'
                tr=(n-1)-((tr+tv)%(n-1))
            else:
                tr=(tr+tv)%(n-1)

        new_grid[tr][tc].append((tv,ti,td))
        if len(new_grid[tr][tc])>=k:
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
    jewels=new_jewels 
    grid=new_grid

print(len(jewels))