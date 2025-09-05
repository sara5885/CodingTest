n = 5
name = []
height = []
weight = []
people=[]
class person():
    def __init__(self, n,h,w):
        self.n=n 
        self.h=h 
        self.w=w 

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))
    people.append(person(n,int(h),float(w)))
people.sort(key=lambda x:x.n)
print('name')
for p in people:
    print(p.n, p.h, p.w)
people.sort(key=lambda x:-x.h)
print('')
print('height')
for p in people:
    print(p.n, p.h, p.w)

# Please write your code here.