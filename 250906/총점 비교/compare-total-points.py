n = int(input())

name = []
score1 = []
score2 = []
score3 = []

students=[]

class student():
    def __init__(self,n,s1,s2,s3):
        self.n=n
        self.s1=s1 
        self.s2=s2 
        self.s3=s3 

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))
    students.append(student(name[-1],score1[-1],score2[-1],score3[-1]))

students.sort(key=lambda x:x.s1+x.s2+x.s3)

for i in range(len(students)):
    print(f"{students[i].n} {students[i].s1} {students[i].s2} {students[i].s3}")


# Please write your code here.