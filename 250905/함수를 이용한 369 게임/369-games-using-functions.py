a, b = map(int, input().split())

def is_in_num(num):
    return str(3) in str(num) or str(6) in str(num) or str(9) in str(num)
def is_magic_num(num):
    return num%3==0 or is_in_num(num)
cnt=0
for i in range(a,b+1):
    
    if is_magic_num(i):
        #print(i)
        cnt+=1

print(cnt)