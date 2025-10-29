#251029 (18:12)
from sortedcontainers import SortedSet 
s=SortedSet()
n = int(input())
command = []
x = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        x.append(int(line[1]))
    else:
        x.append(0)


# Please write your code here.
for i in range(len(command)):
    c=command[i]
    if c=='add':
        s.add(x[i])
    elif c=='remove':
        s.remove(x[i])
    elif c=='find':
        if x[i] in s:
            print('true')
        else:
            print('false')
    elif c=='lower_bound':
        if s.bisect_left(x[i])<len(s) :
            print(s[s.bisect_left(x[i])])
        else:
            print('None')
    elif c=='upper_bound':
        if s.bisect_right(x[i])<len(s):
            print(s[s.bisect_right(x[i])])
        else:
            print('None')
    elif c=='largest':
        if len(s)!=0:
            print(s[-1])
        else:
            print('None')
    elif c=='smallest':
        if len(s)!=0:
            print(s[0])
        else:
            print('None')