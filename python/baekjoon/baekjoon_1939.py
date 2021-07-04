# # baekjoon_1939 중량제한
#
#
# # v1
#
# import sys, heapq, math
#
# INF = math.inf
#
#
# def dijkstra(start_point):
#     heap = []
#     heapq.heappush(heap, [0, start_point])
#     weights[start_point] = 0
#
#     while heap:
#         weight, node = heapq.heappop(heap)
#         if weight > weights[node]:
#             continue
#
#         for next_node, next_weight in adj_list[node]:
#             cost = next_weight + weight
#             if cost < weights[next_node]:
#                 heapq.heappush(heap, [cost, next_node])
#                 weights[next_node] = cost
#
#
#
#
# N, M = map(int, input().split())
# adj_list = [[] for _ in range(N+1)]
# weights = [INF]*(N+1)
#
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     adj_list[a].append([b, c])
#     adj_list[b].append([a, c])
#
# start_point, end_point = map(int, input().split())
# dijkstra(start_point)
# print(weights[end_point])


# v2

# import sys, heapq, math
#
# INF = math.inf
#
#
# def dijkstra(start_point):
#     heap = []
#     heapq.heappush(heap, [0, start_point])
#     weights[start_point] = 0
#
#     while heap:
#         weight, node = heapq.heappop(heap)
#         if weight > weights[node]:
#             continue
#
#         for next_node, next_weight in adj_list[node]:
#             cost = next_weight + weight
#             if cost < weights[next_node]:
#                 heapq.heappush(heap, [cost, next_node])
#                 weights[next_node] = cost
#     return 0
#
#
#
# N, M = map(int, input().split())
# adj_list = [[] for _ in range(N+1)]
# weights = [INF]*(N+1)
# bridges = [[0]*(N+1) for _ in range(N+1)]
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     if bridges[a][b] < c:
#         bridges[a][b] = c
#         bridges[b][a] = c
#
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if bridges[i][j] != 0:
#             adj_list[i].append([j, bridges[i][j]])
#
# start_point, end_point = map(int, input().split())
# dijkstra(start_point)
# print(weights[end_point])


# v3
import sys, heapq, math

INF = math.inf
input = sys.stdin.readline

def dijkstra(start_point):
    heap = []
    heapq.heappush(heap, [-INF, start_point])
    weights[start_point] = INF

    while heap:
        weight, node = heapq.heappop(heap)
        weight *= -1
        if weight < weights[node]:
            continue

        for next_node, next_weight in adj_list[node]:
            cost = min(next_weight, weight)
            if cost > weights[next_node]:
                heapq.heappush(heap, [-cost, next_node])
                weights[next_node] = cost


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
weights = [0]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

start_point, end_point = map(int, input().split())

dijkstra(start_point)
print(weights[end_point])