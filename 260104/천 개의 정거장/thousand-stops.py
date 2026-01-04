import heapq 
import sys 
INT_MAX=sys.maxsize 
A, B, N = map(int, input().split())

bus_fare = []
stop_count = []
bus_stops = []
graph=[[] for _ in range(1001)]
for _ in range(N):
    fare, count = map(int, input().split())
    bus_fare.append(fare)
    stop_count.append(count)
    bus_stops.append(list(map(int, input().split())))
    for i in range(count-1):
        for j in range(i+1, count):
            a=bus_stops[-1][i]
            b=bus_stops[-1][j]
            graph[a].append((b,fare,j-i))

# cost, time 
dist=[(INT_MAX,INT_MAX)]*(1001)
pq=[]
heapq.heappush(pq,(A,(0,0)))
while pq:
    c_node, (c_cost,c_time) = heapq.heappop(pq)
    if dist[c_node]< (c_cost,c_time):
        continue 
    for n_node, n_cost, n_time in graph[c_node]:
        new_cost=c_cost+n_cost
        new_time=c_time+n_time
        if dist[n_node]>(new_cost,new_time):
            dist[n_node]=(new_cost,new_time)
            heapq.heappush(pq,(n_node,(new_cost,new_time)))

a,b=dist[B]
if (a,b)==(INT_MAX,INT_MAX):
    print(-1,-1)
else:
    print(a,b)