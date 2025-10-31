n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

l=[0]*n
r=[0]*n

for i in range(1,n):
    l[i]=l[i-1]+abs(x[i]-x[i-1])+abs(y[i]-y[i-1])
for i in range(n-2,-1,-1):
    r[i]=r[i+1]+abs(x[i+1]-x[i])+abs(y[i+1]-y[i])
# print(l)
# print(r)
min_dist=10000000
for i in range(1,n-1):
    tmp_dist=l[i-1]+r[i+1]+abs(x[i+1]-x[i-1])+abs(y[i+1]-y[i-1])
    if tmp_dist<min_dist:
        # print("i:",i)
        # print(l[i-1],r[i+1],abs(x[i+1]-x[i-1])+abs(y[i+1]-y[i-1]))
        min_dist=tmp_dist
print(min_dist)