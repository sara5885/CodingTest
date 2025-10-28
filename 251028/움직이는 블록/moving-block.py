#251028 (22:14)
n = int(input())
blocks = [int(input()) for _ in range(n)]

total=0
for i in blocks:
    total+=i 

len_per_block=int(total/n)

move_block_cnt=0
b_out=0
b_in=0
for i in blocks:
    if i==len_per_block:
        continue 
    elif i>len_per_block:
        b_out+=i-len_per_block
    else:
        b_in+=len_per_block-i 

print(max(b_out,b_in))
