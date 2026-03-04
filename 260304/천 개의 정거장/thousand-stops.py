# 260304 (14:45)
import sys
import heapq 
INT_MAX=sys.maxsize
A, B, N = map(int, input().split())

bus_fare = []
stop_count = []
bus_stops = []
graph=[[(INT_MAX, INT_MAX) for _ in range(1001)] for _ in range(1001)]
for _ in range(N):
    fare, count = map(int, input().split())
    bus_fare.append(fare)
    stop_count.append(count)
    bus_stops.append(list(map(int, input().split())))

# Please write your code here.

for idx in range(N):
    tmp_fare=bus_fare[idx]
    for i in range(len(bus_stops[idx])):
        for j in range(i+1, len(bus_stops[idx])):
            # 여러 노선 있으면 가장 짧은 노선 
            if graph[bus_stops[idx][i]][bus_stops[idx][j]] > (tmp_fare,j-i):
                graph[bus_stops[idx][i]][bus_stops[idx][j]]=(tmp_fare, j-i)

# 최소 비용, 값은 여기에 저장 
dist=[(INT_MAX,INT_MAX)]*(1001)
pq=[]
heapq.heappush(pq,(A,(0,0)))
while pq:
    c_node, (c_fare, c_time)= heapq.heappop(pq)
    if dist[c_node] < (c_fare, c_time): continue
    for i in range(1,1001):
        if graph[c_node][i]==(INT_MAX, INT_MAX): continue 
        n_fare, n_time= graph[c_node][i]
        if dist[i]>(n_fare+c_fare, n_time+c_time):
            dist[i]=(n_fare+c_fare, n_time+c_time)
            heapq.heappush(pq,(i,(n_fare+c_fare, n_time+c_time)))

if dist[B]==(INT_MAX,INT_MAX):
    print(-1, -1)
else:
    print(dist[B][0], dist[B][1])