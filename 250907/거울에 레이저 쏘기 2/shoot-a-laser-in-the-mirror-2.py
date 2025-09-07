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
now_dir=(k-1)//n
n_dx,n_dy=(k-1)//n, (k-1)%n
# now_dir
# (1,2,3):0, (4,5,6):1, (7,8,9):2, (10,11,12):3 
# (k-1)//3

# dx,dy : k => ((k-1)//3,(k-1)%3)
# 1:(0,0), 2(0,1), 3(0,2)
# 4:(1,0), 5(1,1), 6(1,2)
# 7:(2,0), 8(2,1), 9(2,2)


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