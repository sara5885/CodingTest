n, m = map(int, input().split())

# Please write your code here.
arr=[
    [
        'a' for _ in range(m)
    ]
    for _ in range(n)
]

dx,dy=[0,1,0,-1],[1,0,-1,0]
idx=0
nx,ny=0,0
# ord('A'),ord('Z')+1
alpha='A'
for i in range(n*m):
    # tmp=chr(i)
    arr[nx][ny]=alpha
    tmp_dx,tmp_dy=nx+dx[idx],ny+dy[idx]
    if tmp_dx<0 or tmp_dx>=n or tmp_dy<0 or tmp_dy>=m or arr[tmp_dx][tmp_dy]!='a':
        idx=(idx+1)%4
    
    nx,ny=nx+dx[idx],ny+dy[idx]
    alpha=chr(ord(alpha)+1)

# print(arr)
for row in arr:
    for col in row:
        print(col, end=" ")
    print('')