# #260323 (16:26)
# T = int(input())

# dir={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}


# for _ in range(T):
#     N = int(input())
#     x, y, w, d = [], [], [], []
#     jewels=[]
#     for i in range(N):
#         xi, yi, wi, di = input().split()
#         x.append(2*int(xi))
#         y.append(2*int(yi))
#         w.append(int(wi))
#         d.append(di)
#         jewels.append([2*int(xi),2*int(yi),int(wi),di,i])

#     cnt=0
#     last_collision=-1
#     while True:
#         # 종료조건
        
#         cnt+=1
#         new_jewels=[]
#         while jewels:
#             cx,cy,cw,cd,ci = jewels.pop()
#             dx,dy=dir[cd]
#             nx,ny=cx+dx,cy+dy 
#             new_jewels.append([nx,ny,cw,cd,ci])
        
#         collision={}
#         collision_pos=set()
#         will_collide = False
#         for i in range(len(new_jewels)):
#             for j in range(i+1,len(new_jewels)):
#                 ix,iy,iw,id,ii=new_jewels[i]
#                 jx,jy,jw,jd,ji=new_jewels[j]
#                 if (ix,iy)==(jx,jy):
#                     if (ix,iy) not in collision:
#                         collision[(ix,iy)]=set()
#                     collision[(ix,iy)].add((iw,ii,id))
#                     collision[(ix,iy)].add((jw,ji,jd))
#                     collision_pos.add((ix,iy))
#                 else:
#                     # 나중에 만날 가능성 체크
#                     dx1,dy1 = dir[id]
#                     dx2,dy2 = dir[jd]
#                     if (jx-ix)*(dx1-dx2) + (jy-iy)*(dy1-dy2) > 0:
#                         will_collide = True
#         if not will_collide and not collision:
#             break
#         if collision:
#             last_collision=cnt

#         surv_list=[]
#         for pos, marbles in collision.items():
#             cx,cy=pos
#             cw,ci,cd=max(marbles, key=lambda x:(x[0],x[1]))
#             surv_list.append([cx,cy,cw,cd,ci])

#         jewels=[]
#         for cx,cy,cw,cd,ci in new_jewels:
#             if (cx,cy) in collision_pos:
#                 if [cx,cy,cw,cd,ci] in surv_list:
#                     jewels.append([cx,cy,cw,cd,ci])
#             else:
#                 jewels.append([cx,cy,cw,cd,ci])

#     print(last_collision)


for _ in range(T):
    N = int(input())
    jewels = []
    for i in range(N):
        xi, yi, wi, di = input().split()
        jewels.append([int(xi), int(yi), int(wi), di, i+1])
    
    events = []  # (시간, i, j)
    for i in range(N):
        for j in range(i+1, N):
            x1,y1,w1,d1,i1 = jewels[i]
            x2,y2,w2,d2,i2 = jewels[j]
            dx1,dy1 = dir[d1]
            dx2,dy2 = dir[d2]
            
            # x1 + dx1*t == x2 + dx2*t → t*(dx1-dx2) == x2-x1
            # y1 + dy1*t == y2 + dy2*t → t*(dy1-dy2) == y2-y1
            ddx = dx1-dx2
            ddy = dy1-dy2
            
            if ddx == 0 and ddy == 0:
                continue
            
            if ddx == 0:
                if x1 != x2: continue
                if ddy == 0 or (y2-y1) % ddy != 0: continue
                t = (y2-y1) // ddy
            elif ddy == 0:
                if y1 != y2: continue
                if (x2-x1) % ddx != 0: continue
                t = (x2-x1) // ddx
            else:
                if (x2-x1) % ddx != 0: continue
                t = (x2-x1) // ddx
                if (y2-y1) % ddy != 0: continue
                if t != (y2-y1) // ddy: continue
            
            if t > 0 and t % 2 == 0:  # 2초에 1칸이므로 짝수 t만 유효
                events.append((t, i, j))
    
    events.sort()
    dead = set()
    last_collision = -1
    
    for t, i, j in events:
        if i in dead or j in dead:
            continue
        # 충돌 발생
        last_collision = t // 2  # 2배 스케일 아니므로 //2 불필요, t가 실제 시간
        w1,i1 = jewels[i][2], jewels[i][4]
        w2,i2 = jewels[j][2], jewels[j][4]
        if (w1, i1) > (w2, i2):
            dead.add(j)
        else:
            dead.add(i)
    
    print(last_collision)