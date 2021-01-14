# 나동빈 다익스트라 문제
import math
import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (start, 0))
    distance[start] = 0

    while heap:
        now, dist = heapq.heappop(heap)
        # 방문하지 않은 노드 찾기  == 이미 최단 거리
        if distance[now] < dist:
            continue

        for i in adj_list[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (i[0], cost))


N, M, C = map(int, input().split())
adj_list = [[] for __ in range(N+1)]
INF = math.inf
distance = [INF]*(N+1)

for _ in range(M):
    x, y, z = map(int, input().split())
    adj_list[x].append((y,z))

dijkstra(C)

city_num = 0
delivery_time = 0
print(distance)
for i in range(1, N+1):
    if distance[i] == 'INF':
        continue
    else:
        city_num += 1
        delivery_time = max(delivery_time, distance[i])
print("{} {}".format(city_num-1, delivery_time))