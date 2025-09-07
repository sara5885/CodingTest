import sys 
INT_MIN=-sys.maxsize 
INT_MAX=sys.maxsize
a = input()

max_num=INT_MIN
for i in range(len(a)):
    # 1110 => 0110, 1010, 1100, 1111 
    
    tmp_num=0
    for j in range(len(a)):
        if j==i and a[i]=='0':
            tmp_num=2*tmp_num+1
        elif j==i and a[i]=='1':
            tmp_num=2*tmp_num
        else : 
            tmp_num=2*tmp_num+int(a[j])
    max_num=max(max_num,tmp_num)
    
print(max_num)
