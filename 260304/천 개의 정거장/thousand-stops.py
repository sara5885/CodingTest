import heapq 
import sys 
INT_MAX=sys.maxsize 
A, B, N = map(int, input().split())

bus_fare = []
stop_count = []
bus_stops = []
graph=[[(INT_MAX,INT_MAX) for _ in range(1001)] for _ in range(1001)]
for _ in range(N):
    fare, count = map(int, input().split())
    bus_fare.append(fare)
    stop_count.append(count)
    bus_stops.append(list(map(int, input().split())))
    for i in range(count-1):
        for j in range(i+1, count):
            a=bus_stops[-1][i]
            b=bus_stops[-1][j]
            if graph[a][b]>(fare,j-i):
                graph[a][b]=(fare,j-i)

# cost, time 
dist=[(INT_MAX,INT_MAX)]*(1001)
pq=[]
heapq.heappush(pq,(A,(0,0)))
while pq:
    c_node, (c_cost,c_time) = heapq.heappop(pq)
    if dist[c_node]< (c_cost,c_time):
        continue 
    for i in range(1,1001):
        if graph[c_node][i]==(INT_MAX,INT_MAX):
            continue 
        (next_cost,next_time)=graph[c_node][i]
        new_cost=c_cost+next_cost
        new_time=c_time+next_time
        if dist[i]>(new_cost,new_time):
            dist[i]=(new_cost,new_time)
            heapq.heappush(pq,(i,(new_cost,new_time)))

a,b=dist[B]
if (a,b)==(INT_MAX,INT_MAX):
    print(-1,-1)
else:
    print(a,b)
