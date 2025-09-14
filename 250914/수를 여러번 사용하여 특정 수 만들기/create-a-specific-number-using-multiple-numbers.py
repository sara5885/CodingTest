# 250914 (16:13)
A, B, C = map(int, input().split())

max_num=0

max_a=C//A 
max_b=C//B 

for i in range(max_a+1):
    for j in range(max_b+1):
        if i*A+j*B <=C:
            max_num=max(max_num,i*A+j*B)

print(max_num)
        