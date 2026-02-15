# 260215 (14:17)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_cnt=0
for sx in range(n):
    for sy in range(m):
        # start point : (i,j)-th 
        if grid[sx][sy]<0: 
            continue 
        for h in range(1,n+1-sx):
            for w in range(1,m+1-sy):
                
                tmp_sum=0
                minus_flag=False 
                
                for i in range(sx,sx+h):
                    for j in range(sy,sy+w):    
                        if grid[i][j]<=0:
                            minus_flag=True 
                            tmp_sum=0
                            break
                        else:
                            tmp_sum+=1
                    if minus_flag==True :
                        break 
                if minus_flag==True: break 
               
                if tmp_sum>max_cnt :
                    max_cnt=tmp_sum
if max_cnt==0:
    print(-1)
else: print(max_cnt)

                        


