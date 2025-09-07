import sys 
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
INT_MAX=sys.maxsize 
INT_MIN=-sys.maxsize
min_dist=INT_MAX

for i in range(1,n):
    # i : removing checkpoint number 
    tmp_points=points[:i]+points[i+1:]
    # print(tmp_points)
    tmp_dist=0
    for j in range(len(tmp_points)-1): # checkpoint 0~N compute distance 
        tmp_dist=tmp_dist+abs(tmp_points[j][0]-tmp_points[j+1][0])+abs(tmp_points[j][1]-tmp_points[j+1][1])

    min_dist=min(min_dist,tmp_dist)

print(min_dist)