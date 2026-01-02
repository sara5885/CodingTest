#250102 (12:44)
import sys 
INT_MIN=-sys.maxsize 
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 직사각형 2개 한번에 잡기 
ans=INT_MIN

# def overlap(i,j,h,w,i2,j2,h2,w2):
#     if i==i2 and j==j2 : return True 
#     if i<i2<=i+h and j<j2<=j+w: return True 
#     if i2<i<=i2+h2 and j2<j<=j2+w2: return True 
#     return False

# def overlap(i, j, h, w, i2, j2, h2, w2):
#     # 세로(행) 구간이 겹치는지 확인
#     # "내 시작점이 쟤 끝점보다 작고" AND "쟤 시작점이 내 끝점보다 작아야" 함
#     vertical_overlap = (i < i2 + h2) and (i2 < i + h)
    
#     # 가로(열) 구간이 겹치는지 확인
#     horizontal_overlap = (j < j2 + w2) and (j2 < j + w)
    
#     # 둘 다 겹쳐야 진짜 겹친 것
#     return vertical_overlap and horizontal_overlap

def overlap(i, j, h, w, i2, j2, h2, w2):
    visited=[[0 for _ in range(m)] for _ in range(n)]
    for x in range(i,i+h):
        for y in range(j,j+w):
            visited[x][y]+=1 
    for x in range(i2,i2+h2):
        for y in range(j2,j2+w2):
            visited[x][y]+=1
            if visited[x][y]>=2: return True 
    return False 

def get_score(i,j,h,w,i2,j2,h2,w2):
    score=0
    for x in range(i,i+h):
        for y in range(j,j+w):
            score+=grid[x][y]
    # print("1번 직사각형 : ", score)
    for x in range(i2,i2+h2):
        for y in range(j2,j2+w2):
            score+=grid[x][y]
    # print("최종 직사각형 : ", score)
    # print("======================")
    return score

for i in range(n):
    for j in range(m):
        for h in range(1,n-i+1): # *******
            for w in range(1,m-j+1):
                for i2 in range(n):
                    for j2 in range(m):
                        for h2 in range(1,n-i2+1):
                            for w2 in range(1,m-j2+1):
                                # check overlap
                                # if (i,j,h,w,i2,j2,h2,w2)==(0,0,1,1,1,1,1,1):
                                #     print(overlap(i,j,h,w,i2,j2,h2,w2))
                                if overlap(i,j,h,w,i2,j2,h2,w2):
                                    continue 
                                score=get_score(i,j,h,w,i2,j2,h2,w2)
                                if score>ans:
                                    tmp=[i,j,h,w,i2,j2,h2,w2]
                                ans=max(ans, score)

print(ans)
# print(tmp)