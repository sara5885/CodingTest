N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)
    
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        if len(self.items)==0:
            return 1
        else :
            return 0

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()


s=Stack()
for i in range(N):
    if command[i]=='push':
        s.push(value[i])
    
    elif command[i]=='pop':
        print(s.pop())

    elif command[i]=='top':
        print(s.top())

    elif command[i]=='size':
        print(s.size())
    elif command[i]=='empty':
        print(s.empty())