K, N = map(int, input().split())

# Please write your code here.
answer=[]
def print_answer():
    for elem in answer:
        print(elem,end=" ")
    print()
    return 


def choose(num):
    if num==N+1:
        print_answer()
        return 
    for i in range(1,K+1):
        answer.append(i)
        choose(num+1)
        answer.pop()
    return

choose(1)