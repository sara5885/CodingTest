# 250907 (16:10)
n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Down & \ : Right
# Down & / : Left 
# Right & \ : Down 
# Right & / : Up
# Up & \ :Left 
# Up & / : RIght 
# Left & \ : Up
# Left & / : Down 

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

cnt=0
dir={'D':0, 'L':1,'U':2, 'R':3 }
dx,dy=[1,0,-1,0],[0,-1,0,1]

# initialization 
# 1. now_dir
# (1,2,3):0, (4,5,6):1, (7,8,9):2, (10,11,12):3 
now_dir=(k-1)//n

# 2. n_dx,n_dy 
#n_dx,n_dy=(k-1)//n, (k-1)%n => WRONG 

# x0,y0 구하기
# => 가장자리 변마다 설정해주기 (하나의 계산식으로 바로 구할 수 없음) 
t =(k-1)%n #각 변에서의 순서 
# 각 변의 start 좌료 (x0,y0)
# d=0(위쪽):  (0, +1)
# d=1(오른쪽): (+1, 0)
# d=2(아래쪽): (0, -1)
# d=3(왼쪽):  (-1, 0)
sr = [0, 1, 0, -1]
sc = [1, 0, -1, 0]
r0,c0=[0,0,n-1,n-1],[0,n-1,n-1,0]
n_dx=r0[now_dir]+sr[now_dir]*t
n_dy=c0[now_dir]+sc[now_dir]*t 



while True:    
    # now grid (old dir -> new dir)
    #print(n_dx,n_dy,now_dir)
    if grid[n_dx][n_dy]=='\\':
        now_dir=3-now_dir
    elif grid[n_dx][n_dy]=='/': 
        if now_dir%2==0: #0,2,4
            now_dir=(now_dir+3)%4
        elif now_dir%2==1: #1,3 
            now_dir=(now_dir+1)%4
    cnt+=1 
    # location update
    n_dx,n_dy=n_dx+dx[now_dir],n_dy+dy[now_dir]
    # update grid location => if update location is not in range : break 
    if not in_range(n_dx,n_dy):
        break

print(cnt)