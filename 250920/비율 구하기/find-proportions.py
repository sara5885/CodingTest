# 250920 (16:48)
from sortedcontainers import SortedDict 
n = int(input())
words = [input() for _ in range(n)]

dict=SortedDict()
for i in range(n):
    if words[i] in dict:
        dict[words[i]]+=1
    else:
        dict[words[i]]=1

for key,value in dict.items():
    print(f"{key} {value/n*100:.4f}")