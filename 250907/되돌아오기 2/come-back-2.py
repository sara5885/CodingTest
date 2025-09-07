commands = input()

# Please write your code here.
now_dir=0 

idx={'E':0,'S':1,'W':2,'N':3}

dx,dy=[0,1,0,-1],[1,0,-1,0]

now_dir=3 
n_dx,n_dy=0,0
cnt=0
find_flag=False 
for i in range(len(commands)):
    if commands[i]=='L':
        now_dir=(now_dir+3)%4
    elif commands[i]=='R':
        now_dir=(now_dir+1)%4
    elif commands[i]=='F':
        n_dx,n_dy=n_dx+dx[now_dir],n_dy+dy[now_dir]
    cnt+=1

    if n_dx==0 and n_dy==0:
        find_flag=True 
        break

if find_flag:
    print(cnt)
else:
    print(-1)

