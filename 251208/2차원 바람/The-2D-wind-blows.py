#251208 (12:43)
import copy 
n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]


for w in winds:
    r1,c1,r2,c2=w
    r1,c1,r2,c2=r1-1,c1-1,r2-1,c2-1
    # 1. 경계 rotation
    # 하 -> 우->상->좌 
    tmp_value=a[r1][c1]
    for i in range(r1,r2):
        a[i][c1]=a[i+1][c1]
    for j in range(c1,c2):
        a[r2][j]=a[r2][j+1]
    for i in range(r2,r1,-1):
        a[i][c2]=a[i-1][c2]
    for j in range(c2,c1,-1):
        a[r1][j]=a[r1][j-1]
    a[r1][c1+1]=tmp_value
    
    # for i in a:
    #     for j in i:
    #         print(j,end=" ")
    #     print()
    # print()
    # 2. 평균 score update 
    tmp=copy.deepcopy(a)
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            cx,cy=i,j #center 
            c_value=a[cx][cy]
            cnt=1
            for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
                nx,ny=cx+dx,cy+dy
                if 0<=nx<n and 0<=ny<m :
                    c_value+=a[nx][ny]
                    cnt+=1
            tmp[cx][cy]=c_value//cnt 
    a=tmp 

for i in a:
    for j in i:
        print(j,end=" ")
    print()