n, m = map(int, input().split())

# Please write your code here.
dx,dy=[1,0,-1,0],[0,1,0,-1]
arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

n_x,n_y=0,0
idx=0
for i in range(1,n*m+1):
    arr[n_x][n_y]=i
    tmp_x,tmp_y=n_x+dx[idx],n_y+dy[idx]
    if tmp_x <0 or tmp_x>=n or tmp_y<0 or tmp_y>=m or arr[tmp_x][tmp_y]!=0: 
        idx=(idx+1)%4
    n_x,n_y=n_x+dx[idx],n_y+dy[idx]


for row in arr:
    for col in row:
        print(col, end=" ")
    print('')