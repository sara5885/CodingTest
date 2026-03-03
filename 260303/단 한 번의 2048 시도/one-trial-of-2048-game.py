# 260303 (15:29)
# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()
new_grid=[[0 for _ in range(4)] for _ in range(4)]
if dir=='L':
    for i in range(4):
        piv=0
        piv_cnt=0
        for j in range(4):
            if grid[i][j]!=0:
                if new_grid[i][piv]==0:
                    new_grid[i][piv]=grid[i][j]
                elif new_grid[i][piv]==grid[i][j] and piv_cnt==0:
                    new_grid[i][piv]+=grid[i][j] 
                    piv_cnt+=1
                else:
                    piv+=1
                    piv_cnt=0
                    new_grid[i][piv]=grid[i][j]
elif dir=='R':
    for i in range(4): # 각 row 
        piv=3 # 새로운 grid에 들어갈 위치
        piv_cnt=0
        for j in range(3,-1,-1): #오른쪽에서부터 하나씩 봄 
            if grid[i][j]!=0:
                if new_grid[i][piv]==0:
                    new_grid[i][piv]=grid[i][j]
                elif new_grid[i][piv]==grid[i][j] and piv_cnt==0:
                    new_grid[i][piv]+=grid[i][j]
                    piv_cnt+=1
                else : # 그 다음 pivot에 추가
                    piv-=1
                    piv_cnt=0
                    new_grid[i][piv]=grid[i][j]
elif dir=='U':
    for i in range(4):
        piv=0
        piv_cnt=0
        for j in range(4):
            if grid[j][i]!=0:
                if new_grid[piv][i]==0:
                    new_grid[piv][i]=grid[j][i]
                elif new_grid[piv][i]==grid[j][i] and piv_cnt==0:
                    new_grid[piv][i]+=grid[j][i] 
                    piv_cnt+=1
                else:
                    piv+=1
                    piv_cnt=0
                    new_grid[piv][i]=grid[j][i]

elif dir=='D':
    for i in range(4): # 각 row 
        piv=3 # 새로운 grid에 들어갈 위치
        piv_cnt=0
        for j in range(3,-1,-1): #오른쪽에서부터 하나씩 봄 
            if grid[j][i]!=0:
                if new_grid[piv][i]==0:
                    new_grid[piv][i]=grid[j][i]
                elif new_grid[piv][i]==grid[j][i] and piv_cnt==0:
                    new_grid[piv][i]+=grid[j][i]
                    piv_cnt+=1
                else : # 그 다음 pivot에 추가
                    piv-=1
                    piv_cnt=0
                    new_grid[piv][i]=grid[j][i]

for i in new_grid:
    for j in i :
        print(j,end=" ")
    print()