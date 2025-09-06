n = int(input())


class student:
    def __init__(self,idx, h,w):
        self.idx=idx
        self.h=h
        self.w=w 

# students = [
#     (h, w, i + 1)
#     for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
# ]
students=[]
for i in range(1,n+1):
    h,w=tuple(map(int,input().split()))
    students.append(student(i,h,w))

students.sort(key=lambda x:(x.h,-x.w))

for s in students:
    print(s.h,s.w,s.idx)
