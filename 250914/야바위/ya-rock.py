# 250914 (15:52)
n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

max_score=0
# 초기 조약돌 위치 
for i in range(1,n+1):
    rock_idx=i
    score=0
    for j in range(len(moves)):
        # a,b컵 교환 
        if a[j]==rock_idx:
            rock_idx=b[j]
        elif b[j]==rock_idx:
            rock_idx=a[j]

        # c 확인 후 점수 
        if rock_idx==c[j]:
            score+=1

    max_score=max(max_score, score)
print(max_score)