# 260215 (14:17)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_value=0
max_size=0
fsx,fsy,fex,fey=0,0,0,0
fh,fw=0,0
for sx in range(n):
    for sy in range(m):
        # start point : (i,j)-th 
        if grid[sx][sy]<0: 
            continue 

        for h in range(1,n+1-sx):
            for w in range(1,m+1-sy):
                # [sx:sx+h], [sy:sy+w]
                tmp_sum=0
                minus_flag=False 
                # print(sx,sx+h,sy,sy+w)
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
                # if sx==1 and sy==0 and h==2 and w==3:
                #     print("tmp_sum:",tmp_sum)
                # if sx==2 and sy==2 and h==2 and w==2:
                #     print("tmp_sum:",tmp_sum)
                if tmp_sum>max_value :
                    max_value=tmp_sum
                    max_size=h*w
                    fsx,fsy,fex,fey=sx,sy,sx+h,sy+w
                    fh,fw=h,w
# print(fsx,fsy)
# print(fh,fw)
# print(max_value)
if max_value==0:
    print(-1)
else: print(max_size)

                        


