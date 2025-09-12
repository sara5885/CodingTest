n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_area=1600000000
for i in range(n):
    max_x,max_y=0,0
    min_x,min_y=40001,40001
    for j in range(n):
        if i==j:
            continue 
        max_x=max(max_x,x[j])
        max_y=max(max_y,y[j])
        min_x=min(min_x,x[j])
        min_y=min(min_y,y[j])
    min_area=min(min_area,(max_x-min_x)*(max_y-min_y))

print(min_area)