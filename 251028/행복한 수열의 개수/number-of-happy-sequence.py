#251028 (11:10)
from collections import deque 
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
happy=0

def check_row(x):
    # x: x-th row 
    global m
    cnt=1
    prev_num=grid[x][0]
    for i in range(1,n):
        if prev_num==grid[x][i]:
            cnt+=1 
            if cnt>=m:
                return True
        else:
            cnt=1
        prev_num=grid[x][i]
    if cnt>=m:
        return True 
    else:
        return False 


def check_col(x):
    # x : x-th col 
    global m 
    cnt=1
    prev_num=grid[0][x]
    for i in range(1,n):
        if prev_num==grid[i][x]:
            cnt+=1
            if cnt>=m:
                return True 
        else:
            cnt=1
        prev_num=grid[i][x]
    if cnt>=m:
        return True 
    else:
        return False 

for i in range(n):
    if check_row(i):
        happy+=1
    if check_col(i):
        happy+=1 

print(happy)