text = input() #N
pattern = input() #M

# Please write your code here.

def check_part():
    for i in range(len(text)-len(pattern)+1):
        for j in range(len(pattern)):
            if pattern[j]!=text[j+i]:
                break
            if j==len(pattern)-1:
                return i 
    return -1

print(check_part())
            