import sys

# 입력 속도 향상을 위해 사용 (필수는 아님)
input = sys.stdin.readline

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# dp[i][j][k] : i층, j번째 방에 왔을 때, k번째 방에서 시작한 경우의 최대값
# 초기값은 -1 또는 아주 작은 수로 설정하여 방문하지 않음을 표시
dp = [[[-1] * 3 for _ in range(3)] for _ in range(n)]

# 1. 초기화 (1층)
# 1층에서는 자신이 시작점이므로 dp[0][0][0], dp[0][1][1], dp[0][2][2]만 유효
for j in range(3):
    dp[0][j][j] = grid[0][j]

# 2. DP 진행 (2층 ~ N층)
for i in range(1, n):
    for j in range(3):          # 현재 층의 방 (Current)
        for k in range(3):      # 이전 층의 방 (Previous)
            if j == k: continue # 연속된 같은 방향 금지
            
            # 이전 층까지의 모든 '시작점 경우의 수'를 끌어옴
            for start in range(3):
                if dp[i-1][k][start] != -1: # 유효한 경로라면
                    dp[i][j][start] = max(dp[i][j][start], dp[i-1][k][start] + grid[i][j])

# 3. 정답 출력
ans = 0
for j in range(3):          # 마지막 층의 방 위치
    for start in range(3):  # 1층의 방 위치
        if j == start: continue # 마지막 층과 1층의 위치가 같으면 안 됨
        ans = max(ans, dp[n-1][j][start])

print(ans)