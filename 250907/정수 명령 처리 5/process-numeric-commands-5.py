N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

arr=[]
# Please write your code here.
for i in range(len(command)):
    if command[i]=='push_back':
        arr.append(num[i])
    elif command[i]=='get':
        idx=num[i]
        print(arr[idx-1])
    elif command[i]=='size':
        print(len(arr))
    elif command[i]=='pop_back':
        idx=num[i]
        del arr[idx-1]

