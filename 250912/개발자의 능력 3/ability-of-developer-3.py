abilities = list(map(int, input().split()))

# Please write your code here.
total_sum=sum(abilities)
min_sum=30000001
for i in range(len(abilities)):
    for j in range(i+1,len(abilities)):
        for k in range(j+1,len(abilities)):
            team1=abilities[i]+abilities[j]+abilities[k]
            team2=total_sum-team1
            min_sum=min(min_sum,abs(team1-team2))

print(min_sum)

