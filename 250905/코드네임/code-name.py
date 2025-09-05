MAX_N = 5

codenames = []
scores = []
people=[]
class person:
    def __init__(self, codename='',score=0):
        self.codename=codename
        self.score=score 

for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))
    people.append(person(codename,score))

# Please write your code here.
min_score=101
min_codename=''
for i in range(len(people)):
    p=people[i]
    
    if int(p.score)<min_score:
        min_score=int(p.score) 
        min_codename=p.codename

print(min_codename,min_score)