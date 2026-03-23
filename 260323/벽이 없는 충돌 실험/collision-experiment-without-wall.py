T = int(input())

dir={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}

for _ in range(T):
    N = int(input())
    jewels = []
    for i in range(N):
        xi, yi, wi, di = input().split()
        jewels.append([int(xi), int(yi), int(wi), di, i+1])
    
    events = []
    for i in range(N):
        for j in range(i+1, N):
            x1,y1,w1,d1,i1 = jewels[i]
            x2,y2,w2,d2,i2 = jewels[j]
            dx1,dy1 = dir[d1]
            dx2,dy2 = dir[d2]
            
            ddx = dx1-dx2
            ddy = dy1-dy2
            
            if ddx == 0 and ddy == 0:
                continue
            
            if ddx == 0:
                if x1 != x2: continue
                if ddy == 0 or (y2-y1) % ddy != 0: continue
                t = 2*(y2-y1) // ddy
            elif ddy == 0:
                if y1 != y2: continue
                if (x2-x1) % ddx != 0: continue
                t = 2*(x2-x1) // ddx
            else:
                if (x2-x1) % ddx != 0: continue
                t = 2*(x2-x1) // ddx
                if (y2-y1) % ddy != 0: continue
                if t != 2*(y2-y1) // ddy: continue
            
            if t > 0:
                events.append((t, i, j))
    
    events.sort()
    dead = set()
    last_collision = -1
    
    for t, i, j in events:
        if i in dead or j in dead:
            continue
        last_collision = t
        w1,i1 = jewels[i][2], jewels[i][4]
        w2,i2 = jewels[j][2], jewels[j][4]
        if (w1, i1) > (w2, i2):
            dead.add(j)
        else:
            dead.add(i)
    
    print(last_collision)