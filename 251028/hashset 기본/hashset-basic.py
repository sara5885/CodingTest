n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

tmp=set()

for i in range(n):
    if commands[i]=='find':
        if x[i] in tmp:
            print('true')
        else:
            print('false')
    elif commands[i]=='add':
        tmp.add(x[i])
    elif commands[i]=='remove':
        tmp.remove(x[i])