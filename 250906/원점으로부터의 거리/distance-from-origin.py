points=[]
# Please write your code here.
class point():
    def __init__(self, x,y,idx):
        self.x=x
        self.y=y 
        self.idx=idx 


n = int(input())
for i in range(1,n+1):
    x,y=tuple(map(int,input().split()))
    points.append(point(x,y,i))

points.sort(key=lambda x:(abs(x.x+x.y),x.idx))

for i in points:
    print(i.idx)
