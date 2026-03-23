#260323 (16:26)
T = int(input())

dir={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}

def can_collide(j1, j2):
    x1,y1,w1,d1,i1 = j1
    x2,y2,w2,d2,i2 = j2
    if d1 == d2:
        return False
    dx1,dy1 = dir[d1]
    dx2,dy2 = dir[d2]
    return (x2-x1)*(dx1-dx2) + (y2-y1)*(dy1-dy2) > 0

for _ in range(T):
    N = int(input())
    x, y, w, d = [], [], [], []
    jewels=[]
    for i in range(N):
        xi, yi, wi, di = input().split()
        x.append(2*int(xi))
        y.append(2*int(yi))
        w.append(int(wi))
        d.append(di)
        jewels.append([2*int(xi),2*int(yi),int(wi),di,i])

    cnt=0
    last_collision=-1
    while True:
        # 종료조건
        if not any(can_collide(j1,j2) for i,j1 in enumerate(jewels) for j2 in jewels[i+1:]):
            break

        cnt+=1
        new_jewels=[]
        while jewels:
            cx,cy,cw,cd,ci = jewels.pop()
            dx,dy=dir[cd]
            nx,ny=cx+dx,cy+dy 
            new_jewels.append([nx,ny,cw,cd,ci])
        
        collision={}
        collision_pos=set()
        for i in range(len(new_jewels)):
            for j in range(i+1,len(new_jewels)):
                ix,iy,iw,id,ii=new_jewels[i]
                jx,jy,jw,jd,ji=new_jewels[j]
                if (ix,iy)==(jx,jy):
                    if (ix,iy) not in collision:
                        collision[(ix,iy)]=set()
                    collision[(ix,iy)].add((iw,ii,id))
                    collision[(ix,iy)].add((jw,ji,jd))
                    collision_pos.add((ix,iy))

        if collision:
            last_collision=cnt

        surv_list=[]
        for pos, marbles in collision.items():
            cx,cy=pos
            cw,ci,cd=max(marbles, key=lambda x:(x[0],x[1]))
            surv_list.append([cx,cy,cw,cd,ci])

        jewels=[]
        for cx,cy,cw,cd,ci in new_jewels:
            if (cx,cy) in collision_pos:
                if [cx,cy,cw,cd,ci] in surv_list:
                    jewels.append([cx,cy,cw,cd,ci])
            else:
                jewels.append([cx,cy,cw,cd,ci])

    print(last_collision)