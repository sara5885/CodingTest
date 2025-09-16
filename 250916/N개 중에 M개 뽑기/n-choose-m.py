# 250916 (15:03)
# 건너뛰는 경우도 추가한것. 그래서 cnt도 따로 추가하기 
N, M = map(int, input().split())

answer=[]
def print_answer():
    for i in answer:
        print(i,end=" ")
    print()

def choose(num,cnt):
    if num==N+1: # 모든 경우의 수를 탐색하긴 해야함 
        if len(answer)==M:
            print_answer()
        return 
    
    answer.append(num)
    choose(num+1,cnt+1)
    answer.pop()

    # 그냥 건너뛰기. => append, pop 할 필요 없음 
    choose(num+1,cnt)
    return 

choose(1,0)