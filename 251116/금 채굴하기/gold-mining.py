#251116 (12:35)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# # (0,0) 상대 좌표 (k=2)
# for i in range(-k,k+1): #(-2,-1,0,1,2)
#     for j in range(-(k-abs(i)),k-abs(i)+1): #k-abs(i)


max_gold=0

for x in range(n):
    for y in range(n):
        for k in range(2*n-1):
            tmp_gold=0
            val=0
            for i in range(-k,k+1): #(-2,-1,0,1,2)
                for j in range(-(k-abs(i)),k-abs(i)+1): #k-abs(i)
                    nx,ny=x+i,y+j
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]:
                        tmp_gold+=1
                        val+=m
            val=val-(k*k+(k+1)*(k+1))
            if val>=0:
                max_gold=max(max_gold,tmp_gold)
print(max_gold)
