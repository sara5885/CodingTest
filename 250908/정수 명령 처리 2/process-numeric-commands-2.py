from collections import deque 

N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.

class Queue:
    def __init__(self):
        self.dq=deque()
    def push(self,item):
        self.dq.append(item)
    def empty(self):
        if len(self.dq)==0:
            return 1
        else:
            return 0
    def size(self):
        return len(self.dq)
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()
    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq[0]

dq=Queue()
for i in range(N):
    if command[i]=='push':
        dq.push(A[i])

    elif command[i]=='pop':
        print(dq.pop())

    elif command[i]=='size':
        print(dq.size())

    elif command[i]=='empty':
        print(dq.empty())

    elif command[i]=='front':
        print(dq.front())