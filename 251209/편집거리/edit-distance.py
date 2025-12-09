A = input()
B = input()

n=len(A)
m=len(B)

dp=[[0 for _ in range(m)] for _ in range(n)]

# 1. (0, 0) 처리: 첫 글자끼리 비교
if A[0] == B[0]:
    dp[0][0] = 0
else:
    dp[0][0] = 1

# 2. 첫 번째 열 (B의 첫 글자 'B[0]'만 있는 경우) 초기화
# A의 i번째까지 문자를 -> B[0] 하나로 바꾸는 비용
for i in range(1, n):
    # 직전 비용 + 1 (삭제) vs i개 삭제 후 현재 글자 교체/매칭
    # A[i]가 B[0]과 같으면, 앞의 i개 글자를 지우는 비용(i)만 듦
    # 다르면, 앞의 i개 지우고(i) + 교체(1) = i+1
    cost_replace = i if A[i] == B[0] else i + 1
    dp[i][0] = min(dp[i-1][0] + 1, cost_replace)

# 3. 첫 번째 행 (A의 첫 글자 'A[0]'만 있는 경우) 초기화
# A[0] 하나를 -> B의 j번째까지 문자로 바꾸는 비용
for j in range(1, m):
    # 직전 비용 + 1 (삽입) vs j개 삽입 후 현재 글자 교체/매칭
    cost_replace = j if A[0] == B[j] else j + 1
    dp[0][j] = min(dp[0][j-1] + 1, cost_replace)

# 4. 나머지 채우기 (로직 동일)
for i in range(1, n):
    for j in range(1, m):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

print(dp[n-1][m-1])