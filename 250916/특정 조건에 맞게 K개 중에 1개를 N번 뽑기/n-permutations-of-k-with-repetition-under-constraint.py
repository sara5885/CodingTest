# 250916 (14:01)
K, N = map(int, input().split())
answer=[]

def print_answer():
    for i in answer:
        print(i,end=" ")
    print()

def choose(num):
    if num==N+1:
        print_answer()
        return 

    for i in range(1,K+1):
        if not(len(answer)>= 2 and answer[-1]==i and answer[-2]==i):
            
            answer.append(i)
            choose(num+1)
            answer.pop()
    return 


# 재귀
# end condition
# call same function 
choose(1)
