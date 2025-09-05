n = int(input())
name = []
korean = []
english = []
math = []

students=[]

class student():
    def __init__(self,n,k,e,m):
        self.n=n
        self.k=k
        self.e=e 
        self.m=m 


for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))
    students.append(student(name[-1],korean[-1],english[-1],math[-1]))

students.sort(key=lambda x:(-x.k,-x.e,-x.m))

for i in range(len(students)):
    print(f"{students[i].n} {students[i].k} {students[i].e} {students[i].m}")
# Please write your code here.