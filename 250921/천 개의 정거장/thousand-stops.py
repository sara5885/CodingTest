import sys
import heapq

# 0. 기본 설정
input = sys.stdin.readline
INF = sys.maxsize
MAX_LOCATIONS = 1000  # 문제 제한 조건에서 지점 최대 번호

# --- 1. 입력 받기 및 3가지 자료구조 준비 ---

# A(출발), B(도착), N(버스 개수)
A, B, N = map(int, input().split())

# 1-1. 각 버스의 '요금' (0번 버스부터 N-1번 버스까지)
bus_fare = [0] * N
# 1-2. 각 버스의 '노선 리스트'
bus_stops = [[] for _ in range(N)]
# 1-3. 각 '지점'에 어떤 버스가 서는지 (0번 지점부터 1000번 지점까지)
buses_per_node = [[] for _ in range(MAX_LOCATIONS + 1)]

# N개의 버스 정보 입력받기
for i in range(N):
    # "버스 요금, (정류장 개수)"
    fare, stop_count = map(int, input().split())
    # "노선 리스트"
    route = list(map(int, input().split()))
    
    # 1-1. i번 버스의 요금 저장
    bus_fare[i] = fare
    # 1-2. i번 버스의 노선 저장
    bus_stops[i] = route
    
    # 1-3. 노선을 순회하며 각 '지점'에 'i번' 버스가 정차한다고 기록
    for stop in route:
        buses_per_node[stop].append(i)

# --- 2. 다익스트라(Dijkstra) 준비 ---

# dist[i] = "A에서 i번 지점까지 가는 (최소 비용, 최소 시간)"
dist = [(INF, INF)] * (MAX_LOCATIONS + 1)
# 우선순위 큐
pq = []

# 시작점 A 초기화
dist[A] = (0, 0)
# 큐에 ((비용, 시간), 지점) 튜플을 넣음
heapq.heappush(pq, ((0, 0), A))

# --- 3. 다익스트라(Dijkstra) 핵심 반복 ---

while pq:
    # 1. 현재 '최고의 경로'를 꺼냄
    (current_price, current_time), current_node = heapq.heappop(pq)

    # 2. 낡은 정보(이미 더 좋은 경로를 찾은)는 무시
    if (current_price, current_time) > dist[current_node]:
        continue

    # 3. 현재 지점(current_node)에서 탈 수 있는 모든 버스를 확인
    for bus_id in buses_per_node[current_node]:
        
        # 4. 해당 버스(bus_id)의 요금과 노선도를 가져옴
        this_cost = bus_fare[bus_id]
        this_route = bus_stops[bus_id]
        route_len = len(this_route)

        # 5. 노선도에서 현재 내 위치(current_node)의 인덱스를 찾음
        start_idx = this_route.index(current_node)

        # 6. 현재 정류장 *다음*부터 노선을 한 바퀴 순회
        # (i=1: 다음 정류장, i=2: 다다음 정류장 ...)
        for i in range(1, route_len):
            
            # 7. 다음 정류장 정보 계산
            time_to_next_node = i
            next_node_idx = (start_idx + i) % route_len  # 순환 처리
            next_node = this_route[next_node_idx]

            # 8. '새로운 경로'의 총 비용과 총 시간 계산
            new_price = current_price + this_cost
            new_time = current_time + time_to_next_node

            # 9. '새로운 경로'가 기존 '최고 기록'보다 좋으면 갱신
            if (new_price, new_time) < dist[next_node]:
                dist[next_node] = (new_price, new_time)
                heapq.heappush(pq, ((new_price, new_time), next_node))

# --- 4. 결과 출력 ---

final_result = dist[B]

if final_result[0] == INF:
    print("-1 -1")
else:
    # (최소 비용, 최소 시간)을 공백으로 구분해 출력
    print(*final_result)