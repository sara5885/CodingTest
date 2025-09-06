dirs = input()

# Please write your code here.
dx,dy=[1,0,-1,0],[0,-1,0,1]
# 0:동, 1:남, 2:서, 3:북

now_dir=3 
x,y=0,0
for i in range(len(dirs)):
    if dirs[i]=='L':
        now_dir=(now_dir+3)%4
    elif dirs[i]=='R':
        now_dir=(now_dir+1)%4
    elif dirs[i]=='F':
        x,y=x+dx[now_dir],y+dy[now_dir]


print(x,y)