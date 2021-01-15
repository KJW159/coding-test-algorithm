# baekjoon_1753 최단 경로

# v1
# import sys
# import math
# import heapq
#
# def dijkstra(start):
#     heap = []
#     distance[start] = 0
#     heapq.heappush(heap, (start, 0))
#
#     while heap:
#         now, dist = heapq.heappop(heap)
#
#         if distance[now] < dist:
#             continue
#
#         for next_node, next_dist in adj_list[now]:
#             travel_time = distance[now] + next_dist
#
#             if travel_time < distance[next_node]:
#                 distance[next_node] = travel_time
#                 heapq.heappush(heap, (next_node, travel_time))
#
#
# V, E = map(int, sys.stdin.readline().split())
# K = int(sys.stdin.readline())
# adj_list = [[] for _ in range(V+1)]
#
# INF = math.inf
#
# distance = [INF] * (V+1)
#
# for __ in range(E):
#     u, v, w = map(int, sys.stdin.readline().split())
#     adj_list[u].append((v, w))
#
# dijkstra(K)
#
# for n in range(1, V+1):
#     if distance[n] != INF:
#         print(distance[n])
#     else:
#         print("INF")

# v2
# import sys
# import math
# import heapq
#
# def dijkstra(start):
#     heap = []
#     distance[start] = 0
#     heapq.heappush(heap, (start, 0))
#
#     while heap:
#         now, dist = heapq.heappop(heap)
#
#         if distance[now] < dist:
#             continue
#
#         for next_node, next_dist in adj_list[now]:
#             travel_time = distance[now] + next_dist
#
#             if travel_time < distance[next_node]:
#                 distance[next_node] = travel_time
#                 heapq.heappush(heap, (next_node, travel_time))
#
#
# V, E = map(int, sys.stdin.readline().split())
# K = int(sys.stdin.readline())
# adj_list = [[] for _ in range(V+1)]
#
# INF = math.inf
#
# distance = [INF] * (V+1)
#
# for __ in range(E):
#     u, v, w = map(int, sys.stdin.readline().split())
#     adj_list[u].append((v, w))
#
# dijkstra(K)
#
# for n in range(1, V+1):
#     if distance[n] != INF:
#         print(distance[n])
#     else:
#         print("INF")

# v3
import sys
import math
import heapq

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue
        for i in adj_list[now]:
            travel_time = distance[now] + i[1]
            if travel_time < distance[i[0]]:
                distance[i[0]] = travel_time
                heapq.heappush(heap, (travel_time, i[0]))


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
adj_list = [[] for _ in range(V+1)]

INF = math.inf

distance = [INF] * (V+1)

for __ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj_list[u].append((v, w))

dijkstra(K)

for n in range(1, V+1):
    if distance[n] == INF:
        print("INF")
    else:
        print(distance[n])
