#251029 (18:22)
from sortedcontainers import SortedSet 
T = int(input())

for _ in range(T):
    s=SortedSet()
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    command = [op[0] for op in operations]
    n = [int(op[1]) for op in operations]

    # Please write your code here.
    for i in range(k):
        if command[i]=='I':
            s.add(n[i])
        elif command[i]=='D':
            if len(s)==0:
                continue 
            if n[i]==1:
                s.remove(s[-1])
            elif n[i]==-1:
                s.remove(s[0])

    if len(s)==0:
        print('EMPTY')
    else:
        print(s[-1],s[0])

            