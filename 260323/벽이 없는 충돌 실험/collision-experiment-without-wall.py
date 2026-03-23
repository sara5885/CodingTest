import sys 
INT_MAX = sys.maxsize
T = int(input())
grid = [[-1]*4001 for _ in range(4001)]
dir = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}

for _ in range(T):
    N = int(input())
    jewels = []
    for i in range(N):
        xi, yi, wi, di = input().split()
        x, y = 2*int(xi)+2000, 2*int(yi)+2000
        jewels.append([x, y, i, int(wi), di])
        grid[x][y] = i  # 초기 위치 grid에 등록

    final_collision = -1

    for i in range(1, 4001):
        next_grid_cells = []  # 이번 스텝에서 grid에 쓴 셀 기록

        for j in range(len(jewels)):
            cx, cy, cidx, cw, cdir = jewels[j]
            if cx == INT_MAX:
                continue

            dx, dy = dir[cdir]
            nx, ny = cx+dx, cy+dy

            # 이전 위치 grid 제거
            grid[cx][cy] = -1

            if not (0 <= nx < 4001 and 0 <= ny < 4001):
                jewels[j][0] = INT_MAX
                jewels[j][1] = INT_MAX
                continue

            if grid[nx][ny] != -1:
                final_collision = i
                oidx = grid[nx][ny]
                ox, oy, _, ow, odir = jewels[oidx]

                if cw > ow or (cw == ow and cidx > oidx):
                    # 현재 구슬 승리
                    jewels[oidx][0] = INT_MAX
                    jewels[oidx][1] = INT_MAX
                    grid[nx][ny] = cidx
                    jewels[j] = [nx, ny, cidx, cw, cdir]
                    next_grid_cells.append((nx, ny))
                else:
                    # 기존 구슬 승리, 현재 구슬 제거
                    jewels[j][0] = INT_MAX
                    jewels[j][1] = INT_MAX
            else:
                grid[nx][ny] = cidx
                jewels[j] = [nx, ny, cidx, cw, cdir]
                next_grid_cells.append((nx, ny))

    print(final_collision)

    # 테스트케이스 끝: grid 전체 초기화 (살아있는 구슬 위치만)
    for j in range(len(jewels)):
        cx, cy = jewels[j][0], jewels[j][1]
        if cx != INT_MAX:
            grid[cx][cy] = -1