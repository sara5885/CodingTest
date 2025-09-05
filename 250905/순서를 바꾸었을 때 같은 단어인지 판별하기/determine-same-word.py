word1 = input()
word2 = input()

# Please write your code here.
tmp1=''.join(sorted(word1))
tmp2=''.join(sorted(word2))
if tmp1==tmp2:
    print('Yes')
else:
    print('No')