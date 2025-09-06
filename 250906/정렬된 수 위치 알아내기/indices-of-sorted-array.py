n = int(input())
sequence = list(map(int, input().split()))
nums=[]
# Please write your code here.
class num():
    def __init__(self,idx,value):
        self.idx=idx 
        self.value=value 

for i in range(len(sequence)):
    nums.append(num(i+1,sequence[i]))


nums.sort(key=lambda x: x.value)

# results의 index : 원래 index 
# results의 value : 바뀐 위치
results=[0]*(n+1)

for i,num in enumerate(nums, start=1):
    results[num.idx]=i 

for i in range(1,len(nums)+1):
    print(results[i], end=" ")
