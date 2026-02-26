# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()
tmp=[[0 for _ in range(4)] for _ in range(4)]

for i in tmp:
    for j in i:
        print(j,end=" ")
    print()
# if dir=='R':
    
# elif dir=='L':
# elif dir=='U':
# elif dir=='D':