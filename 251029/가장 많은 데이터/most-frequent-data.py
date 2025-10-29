n = int(input())
words = [input() for _ in range(n)]

dictionary={}

for word in words:
    if word not in dictionary:
        dictionary[word]=1
    else:
        dictionary[word]+=1 

max_cnt=0
for value in dictionary.values():
    max_cnt=max(max_cnt,value)

print(max_cnt)