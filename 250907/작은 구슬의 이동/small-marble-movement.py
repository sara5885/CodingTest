n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# dir={'U':0,'D':3,'R':0,'L':2}
dir={'D':0, 'R':1, 'L':2, 'U':3}
# Please write your code here.
dx,dy=[1,0,0,-1],[0,1,-1,0]
# 0: (0,1), 1: (1,0), 2:(-1,0), 3:(0,-1)
def in_range(r,c):
    return r>=1 and r<=n and c>=1 and c<=n

    

# after T 
dir_num=dir[d]
for i in range(t):
    # print(f"(r,c):({r}),({c})")
    if not in_range(r+dx[dir_num], c+dy[dir_num]):
        dir_num=3-dir_num
        continue
    r,c=r+dx[dir_num], c+dy[dir_num]

print(r,c)