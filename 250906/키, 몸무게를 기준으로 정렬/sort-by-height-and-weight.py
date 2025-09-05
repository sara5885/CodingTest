n = int(input())
name = []
height = []
weight = []
people=[]
class person():
    def __init__(self,n,h,w):
        self.n=n 
        self.h=h 
        self.w=w

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))
    people.append(person(n_i,int(h_i),int(w_i)))

people.sort(key=lambda x:(x.h, -x.w))

for p in people:
    print(p.n, p.h,p.w)