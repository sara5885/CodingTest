n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

grid=[
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

dx,dy=[1,-1,0,0],[0,0,1,-1]

def in_range(r,c):
    return r>=1 and r<=n and c>=1 and c<=n

for i in range(m):
    r,c=points[i]
    grid[r][c]=1
    cnt=0
    for j in range(4):
        if in_range(r+dx[j],c+dy[j]) and grid[r+dx[j]][c+dy[j]]==1:
            cnt+=1

    if cnt==3:
        print(1)
    else:
        print(0)


