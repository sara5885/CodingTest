# 250920 (16:31)
n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))
dict={}
for i in range(len(commands)):
    if commands[i][0]=='add':
        dict[commands[i][1]]=commands[i][2]
    elif commands[i][0]=='find':
        if commands[i][1] in dict:
            print(dict[commands[i][1]])
        else:
            print('None')
    elif commands[i][0]=='remove':
        dict.pop(commands[i][1])