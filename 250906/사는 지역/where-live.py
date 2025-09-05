n = int(input())
name = []
street_address = []
region = []
people=[]
class person():
    def __init__(self, name,address,region):
        self.name=name 
        self.address=address
        self.region=region 


for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)
    people.append(person(n_i,s_i,r_i))

name.sort()
last_name=name[-1]

for i in range(len(people)):
    if people[i].name==last_name:
        print(f"name {people[i].name}")
        print(f"addr {people[i].address}")
        print(f"city {people[i].region}")
        break

# Please write your code here.
