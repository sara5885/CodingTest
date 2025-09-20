# 250920 (13:43) (14:23)
# (15:20 )
n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]


for i in range(q): #q번 바람 
    r,d=winds[i]
    r-=1
    if d=='L':
        tmp=a[r][-1]
        for j in range(m-1,0,-1):
            a[r][j]=a[r][j-1]
        a[r][0]=tmp

    elif d=='R':
        tmp=a[r][0]
        for j in range(0,m-1,1):
            a[r][j]=a[r][j+1]
        a[r][-1]=tmp 

    # r 기준으로 위 / 아래 
    # print(f"{i}번째 q:{a}")
    up_same=False 
    down_same=False 
    up_r=r #기준 row 
    down_r=r #기준 row 
    while up_r-1>=0:
        same_flag=False 
        for idx in range(m):
            if a[up_r][idx]==a[up_r-1][idx]:
                same_flag=True 
                break 
        if same_flag==False :
            break 
        else :
            if (d=='R' and abs(r-up_r)%2==0) or (d=='L' and abs(r-up_r)%2==1): #왼->쪽 
                
                tmp=a[up_r-1][-1]
                for j in range(m-1,0,-1):
                    a[up_r-1][j]=a[up_r-1][j-1]
                a[up_r-1][0]=tmp
            else:
            # elif (d=='R' and abs(r-down_r)%2==0)or(d=='L' and abs(r-down_r)%2==1):
                
                tmp=a[up_r-1][0]
                for j in range(0,m-1,1):
                    a[up_r-1][j]=a[up_r-1][j+1]
                a[up_r-1][-1]=tmp 
            
            up_r-=1
    
    while down_r+1<n:
        same_flag=False 
        for idx in range(m):
            if a[down_r][idx]==a[down_r+1][idx]:
                same_flag=True 
                break 
        if same_flag==False :
            break 
        elif same_flag==True :
            # if d=='L':
            if (d=='R' and abs(r-down_r)%2==0)or(d=='L' and abs(r-down_r)%2==1):
                
                tmp=a[down_r+1][-1]
                for j in range(m-1,0,-1):
                    a[down_r+1][j]=a[down_r+1][j-1]
                a[down_r+1][0]=tmp
            # elif d=='R':
            else:
                
                tmp=a[down_r+1][0]
                for j in range(0,m-1,1):
                    a[down_r+1][j]=a[down_r+1][j+1]
                a[down_r+1][-1]=tmp 
            # print(f"{i}번째 q+{down_r} : {a}")
            down_r+=1
        



for row in a:
    print(*row)
