# 250913 (21:22)
N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)


max_pill=0

# each i-th cheeze 
for i in range(1,M+1): # each cheeze
    # 1) sick_p 탐색. sick_p가 먹은 cheeze가 아니면 break (sick_p중에 한명이라도 먹었는지)
    eat_flag=True 
    sick_cnt=0
    # check patient record (to check i-th cheeze)
    for j in range(len(sick_p)): # patient 기록 확인 => patient별 섭취한 치즈 확인 (이때 아픈기록보다 이전시점)
        # j-th patient => check cheeze eating record 
        for k in range(D): #p,m,t(치즈 먹은 기록)=>j환자가 먹은 치즈 확인 
            if p[k]==sick_p[j] and m[k]==i and t[k]<=sick_t[j]-1:
                # 치즈후보임 
                print(f"치즈후보 : (i,sick_p[j],m[k]):({i},{sick_p[j]},{m[k]})")
                sick_cnt+=1 
            # else:
            #     break
    # 진짜 후보 (조건 만족) => 이 치즈 먹은 사람 다 찾기 
    if sick_cnt==S:
        print('상한치즈 후보:',i)
        people=[0]*(N+1)
        for k in range(D): #p,m,t (치즈먹은기록)
            if m[k]==i:
                people[p[k]]=1
        tmp_pill=sum(people)
        print('tmp_pill:',tmp_pill)
        max_pill=max(tmp_pill,max_pill)

print(max_pill)