# 250916 (14:15)
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# 1-m 까지 
max_score=0
answer=[]

# 값 구하기 
def compute_score():
    # [1번말, 2번말, 1번말]
    global max_score
    arr_k=[0]*(k+1)
    for i in range(len(answer)):
        arr_k[answer[i]]+=nums[i]
    score=0
    for i in arr_k:
        if i>=m-1:
            score+=1
    # print(f"arr_k:{arr_k}, answer={answer}, score:{score}")
    max_score=max(max_score,score)

# 턴마다 하나씩 선택 

# 모든 경우 check 
def choose(num):
    if num==n+1: # 총 n번의 턴 
        compute_score()
        return 
    
    # k개의 말 
    for i in range(k):
        answer.append(i)
        choose(num+1)
        answer.pop()


choose(1)
print(max_score)