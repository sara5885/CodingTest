# 260320 (17:15)
T = int(input())

for _ in range(T):
    
    N, M = map(int, input().split())
    x, y, d = [], [], []
    grid=[[0 for _ in range(N)] for _ in range(N) ]
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi)-1)
        y.append(int(yi)-1)
        d.append(di)
        grid[int(xi)-1][int(yi)-1]=di 

    # 바뀌는 것 . x,y, d 
    dir={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
    # 2*N 했는데도 

    for _ in range(2*N+2):
        new_grid=[[0 for _ in range(N)] for _ in range(N)]
        bombed_set=set()
        for i in range(N):
            for j in range(N): 
                # 원래 grid에 값이 있으면 움직여야함 
                # 새로운 위치 update -> 이 값이 new_grid에 이미 존재하면 둘다사라짐 
                if grid[i][j]!=0:
                    dx,dy = dir[grid[i][j]]
                    nx,ny=i+dx,j+dy 
                    # out of range면 방향 바꾸기 -> 이 때도 확인헤야함 
                    if not (0<=nx<N and 0<=ny<N): 
                        if grid[i][j]=='U':
                            if new_grid[i][j] or (i,j) in bombed_set:
                                bombed_set.add((i,j))
                                new_grid[i][j]=0
                            else:
                                new_grid[i][j]='D'
                        if grid[i][j]=='D':
                            if new_grid[i][j] or (i,j) in bombed_set:
                                bombed_set.add((i,j))
                                new_grid[i][j]=0
                            else:
                                new_grid[i][j]='U'
                        if grid[i][j]=='R':
                            if new_grid[i][j] or (i,j) in bombed_set:
                                bombed_set.add((i,j))
                                new_grid[i][j]=0
                            else:
                                new_grid[i][j]='L'
                        if grid[i][j]=='L':
                            if new_grid[i][j] or (i,j) in bombed_set:
                                bombed_set.add((i,j))
                                new_grid[i][j]=0
                            else:
                                new_grid[i][j]='R'
                    # 아니면 한칸 이동핟기 
                    else:
                        #new_grid확인하기
                        if new_grid[nx][ny] or (nx,ny) in bombed_set:
                            new_grid[nx][ny]=0
                            bombed_set.add((nx,ny))
                        else:
                            new_grid[nx][ny]=grid[i][j]
        grid=new_grid
        # for row in new_grid:
        #     for col in row:
        #         print(col,end=" ")
        #     print()
        # print("--")
        # for row in grid:
        #     for col in row:
        #         print(col,end=" ")
        #     print()
        # print()

    ans=0
    for row in grid:
        for col in row:
            if col !=0:
                ans+=1 
    print(ans)   
