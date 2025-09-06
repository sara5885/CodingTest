N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# N : 5명 
# M : 7 
# K : 3  => 3번 이상 벌칙 -> 벌금 

arr=[0]*(N+1)
first_idx=-1

for i in range(M):
    stu_idx=student[i]
    arr[stu_idx]+=1
    if arr[stu_idx]>=K:
        first_idx=stu_idx
        break

print(first_idx)

