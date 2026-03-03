# 260303 (16:58)
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def drop(arr):
    # 중력으로 떨어뜨리기 
    new_arr=[[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        piv=n-1
        for i in range(n-1,-1,-1):
            if new_arr[piv][j]!=0:
                piv-=1 
            new_arr[piv][j]=arr[i][j]
    return new_arr


def bomb(arr,m):
    # arr에서 m개 이상 같은 숫자 (column 기준) 있으면 터뜨려서 보내기 
    new_arr=arr.copy()
    
    # pointer 2개 쓰기 
    for j in range(n):
        start=0 
        end=0
        for i in range(n):
            if arr[i][j]==arr[start][j]: 
                end=i
            else:
                if end-start+1>=m:
                    for idx in range(start, end+1):
                        new_arr[idx][j]=0
                start=i
            if i==n-1 and end-start+1>=m:
                for idx in range(start,n):
                    new_arr[idx][j]=0
    # for i in new_arr:
    #     for j in i:
    #         print(j,end=" ")
    #     print() 
    # print("---------")
    return drop(new_arr)


    # 중력으로 떨어뜨림

def rotate(arr):
    # 90도 회전
    # 중력으로 떨어뜨림 
    new_arr=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j]=arr[n-j-1][i]
    new_arr=drop(new_arr)
    return new_arr

for cnt in range(k) :
    # print("-------------",cnt,"-----------")
    new_arr=bomb(arr,m)
    # for i in new_arr:
    #     for j in i:
    #         print(j,end=" ")
    #     print()
    # print("----------------")
    arr=rotate(new_arr)
    # for i in arr:
    #     for j in i:
    #         print(j,end=" ")
    #     print()
    
    if cnt==k-1:
        tmp_arr=bomb(arr,m)
        if tmp_arr!=arr:
            arr=tmp_arr 
ans=0
for i in arr:
    for j in i:
        if j!=0: ans+=1 
print(ans)
        