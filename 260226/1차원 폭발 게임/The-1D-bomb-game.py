# 260226 (18:03)

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

if m==1:
    print(0)
else:
    while True:
        # 터질 폭탄이 더이상 없을 때 : break 
            # m이상 연속된 길이의 숫자 없음 
        bomb_flag=False
        # 터질 폭탄 확인 
        cnt=1
        start_i=0
        new_numbers=numbers.copy()
        for n in range(1,len(numbers)):
            if numbers[n]==numbers[n-1]:
                cnt+=1
                if cnt>=m: # 터질 폭탄들 
                    # start_i부터 현재까지의 폭탄들 제거 
                    new_numbers=numbers[:start_i]+numbers[n+1:]
                    cnt=1
                    bomb_flag=True
            else:
                cnt=1 # 이전 폭탄이랑 숫자 다름 => cnt 1로 초기화 
                start_i=n #시작 point 현재 num으로 update 
        if not bomb_flag : break
        numbers=new_numbers
        # print(numbers)

    print(len(numbers))
    for i in numbers:
        print(i)
