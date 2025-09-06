N, K, P, T = map(int, input().split())

engineers=[0]
class engineer:
    def __init__(self,disease=0, infect_num=0):
        self.disease=disease
        self.infect_num=infect_num

for i in range(1,N+1):
    if i==P:
        engineers.append(engineer(1,2))
    else:
        engineers.append(engineer())

# handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes=[]
class handshake:
    def __init__(self,t,x,y):
        self.t=t 
        self.x=x 
        self.y=y

for i in range(T):
    t,x,y=tuple(map(int,input().split()))
    handshakes.append(handshake(t,x,y))

handshakes.sort(key=lambda x:x.t)


for handshake in handshakes:
    tmp_x=handshake.x
    tmp_y=handshake.y 

    # case 1 : 둘다 병 X 
    if engineers[tmp_x].disease==0 and engineers[tmp_y].disease==0:
        continue
    # case 2 : 한명만 병 => 병걸린 사람이 안걸린사람에게 전염시킴 
    elif engineers[tmp_x].disease==0 and engineers[tmp_y].disease==1:
        # 감염횟수 차감 
        if engineers[tmp_y].infect_num>0:
            engineers[tmp_y].infect_num-=1
            # 감염시키기
            engineers[tmp_x].disease=1
            engineers[tmp_x].infect_num=2

    elif engineers[tmp_x].disease==1 and engineers[tmp_y].disease==0:
        # 감염횟수 차감 
        if engineers[tmp_x].infect_num>0:
            engineers[tmp_x].infect_num-=1
            engineers[tmp_y].disease=1
            engineers[tmp_y].infect_num=2
            
    # case 3 : 둘다 병 (횟수차감)
    elif engineers[tmp_x].disease==1 and engineers[tmp_y].disease==1:
        if engineers[tmp_x].infect_num>0:
            engineers[tmp_x].infect_num-=1
        if engineers[tmp_y].infect_num>0:
            engineers[tmp_y].infect_num-=1


for i in range(1,N+1):
    print(engineers[i].disease,end='')