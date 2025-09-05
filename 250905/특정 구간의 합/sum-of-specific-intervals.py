n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def compute_sum(a1,a2):
    global arr 
    answer=0
    for i in range(a1-1,a2):
        answer+=arr[i]
    return answer 



for i in range(len(queries)):
    a1,a2=queries[i]
    print(compute_sum(a1,a2))