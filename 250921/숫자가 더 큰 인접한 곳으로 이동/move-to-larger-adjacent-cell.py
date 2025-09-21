#250921 (23:21)
n, r, c = map(int, input().split())
a = [[0] * (n ) for _ in range(n)]

for i in range(n ):
    row = list(map(int, input().split()))
    for j in range(n):
        a[i][j] = row[j]

dx,dy=[-1,1,0,0],[0,0,-1,1]

n_r,n_c=r-1,c-1
print(a[n_r][n_c],end=" ")
while True:
    if 0<=n_r<n and 0<=n_c<n:
        changed=False 
        for i in range(4):
            tmp_r,tmp_c=n_r+dx[i], n_c+dy[i]
            print('DEBUGGING:',r,c,tmp_r,tmp_c, a[tmp_r][tmp_c])
            if 0<=tmp_r<n and 0<=tmp_c<n and a[tmp_r][tmp_c]>a[r][c]:
                
                n_r,n_c=tmp_r,tmp_c
                changed=True 
                print(a[n_r][n_c],end=" ")
        if changed==False:
            break
    else:
        break 
