n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]


# x1,y1 / x2,y2/ x3,y3 
# 
def compute_parallel_triangle(i,j,k):
    x1,y1=x[i],y[i]
    x2,y2=x[j],y[j]
    x3,y3=x[k],y[k]
    arr=[]
    arr.append(points[i])
    arr.append(points[j])
    arr.append(points[k])
    max_triangle=0
    # x평행 & y 평행 => compute  
    for i in range(3): # center (얘는 x도 하나 같고 y도 하나 같음 )
        for j in range(3):
            for k in range(3):
                if i==j or j==k or k==i:
                    continue 
                if arr[i][0]==arr[j][0] and arr[i][1]==arr[k][1]:
                    dist_x=abs(arr[i][1]-arr[j][1])
                    dist_y=abs(arr[i][0]-arr[k][0])
                    max_triangle=max(max_triangle,dist_x*dist_y)

    return max_triangle

# 하나는 x축과 평행, 하나는 y축과 평행한 걸 찾아야함 
# x축 평행 (2 points 조합찾기) & y축 평행 (2 points 조합 찾기)
total_max=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            total_max=max(total_max,compute_parallel_triangle(i,j,k))

print(total_max)


            
        