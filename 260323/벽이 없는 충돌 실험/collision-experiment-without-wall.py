# 260323 (22:04)
import sys 
INT_MAX=sys.maxsize
T = int(input())
dir={'U':(0,1),'D':(0,-1), 'L':(-1,0),'R':(1,0)}
for _ in range(T):
    N = int(input())
    # x, y, w, d = [], [], [], []
    jewels=[[] for _ in range(N)] #[x,y,index,power,direction]
    grid=[[-1 for _ in range(4001)] for _ in range(4001)] # 4001로 해도 됨. 어차피 그 이상이면 out of index

    for i in range(N):
        xi, yi, wi, di = input().split()
        # x.append(2*int(xi)+2000)
        # y.append(2*int(yi)+2000)
        # w.append(int(wi))
        # d.append(di)
        jewels[i]=[2*int(xi)+2000, 2*int(yi)+2000, i, int(wi), di]

    # x[],y[],w[],d[]는 idx에 의해 
    # 이동 -> 충돌 (초마다 업데이트)
    final_collision=-1
    for i in range(1,4001): #(-1000~1000)*2 
        #1. 구슬 이동 
        #2. 충돌 확인 
        # (X)=> 모든 구슬 이동 => 모든 구슬 충돌 x 
        # (O)=> 모든 구슬에 대해 : 이동&충돌확인 
        # ** 구슬은 어떻게 관리할 것인가? => 매번 새로운 구슬 list?
        # ** new_jewels를 만드는게 나을까 아니면 원래 jewels의 값을 update 하는게 나을까
        new_jewels=[]*N
        for cx,cy,cidx,cw,cdir in jewels:
            if (cx,cy)==(INT_MAX,INT_MAX): #이미 사라진 구슬 
                continue 
            dx,dy = dir[cdir]
            nx,ny = cx+dx, cy+dy 
            # 1. 이동한 다음위치가 범위밖이면 skip
            if not (0<=nx<4001 and 0<=ny<4001): 
                continue 
            # 2. 이동한 다음위치에 다음 구슬이 있으면 
            if grid[nx][ny]!=-1:
                final_collision=i
                # print("collision!!!")
                
                ox,oy,oidx,ow,odir=jewels[grid[nx][ny]] # 우선순위 : cw, cidx vs 
                # print(nx,ny, "idx1:", cidx,"idx2:",oidx)
                # 2-1. 우선순위가 더 높으면 : update : grid[nx][ny] / 원래 new_jewels에 있는 구슬 제거 
                if cw>ow or (cw==ow and cidx>oidx):
                    # new_jewels에 원래 있는 값 => 꼭 제거해야하나? 
                    grid[nx][ny]=cidx
                    jewels[cidx]=[nx,ny,cidx,cw,cdir]
                    jewels[oidx]=[INT_MAX,INT_MAX,oidx,ow,odir]
                # 2-2. 우선순위가 더 낮으면 : skip / new_jewels에 update X 
                else:
                    jewels[cidx]=[INT_MAX,INT_MAX,cidx,cw,cdir]
                # print("disapperad!!!")
                # print(nx,ny, "winner:",grid[nx][ny])
                
            else:
                grid[nx][ny]=cidx
                jewels[cidx]=[nx,ny,cidx,cw,cdir]

    print(final_collision)
    

