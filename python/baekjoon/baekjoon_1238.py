# baekjoon_1238 파티






# v1
# import math, heapq
#
# INF = math.inf
#
#
# def dijkstra(student):
#     heap = []
#     distance[student][student] = 0
#     heapq.heappush(heap, [0, student])
#
#     while heap:
#         dist, start = heapq.heappop(heap)
#
#         if distance[student][start] < dist:
#             continue
#
#         for next_node, dist_next in adj_list[start]:
#             cost = dist + dist_next
#             if cost < distance[student][next_node]:
#                 distance[student][next_node] = cost
#                 heapq.heappush(heap, [cost, next_node])
#
# def dijkstra_v2(village):
#     heap = []
#     distance2[village] = 0
#     heapq.heappush(heap, [0, village])
#
#     while heap:
#         dist, start = heapq.heappop(heap)
#
#         if distance2[start] < dist:
#             continue
#
#         for next_node, dist_next in adj_list[start]:
#             cost = dist + dist_next
#             if cost < distance2[next_node]:
#                 distance2[next_node] = cost
#                 heapq.heappush(heap, [cost, next_node])
#
# N, M, X = map(int, input().split())
# adj_list = [[] for _ in range(N+1)]
# distance = [[INF]*(N+1) for _ in range(N+1)]
# distance2 = [INF]*(N+1)
#
# res = 0
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     adj_list[a].append([b,c])
#
#
# for i in range(1, N+1):
#     dijkstra(i)
#
# dijkstra_v2(X)
# for i in range(1, N+1):
#     res = max(res, distance[i][X] + distance2[i])
#
# print(res)

# v2
# import math, heapq, sys
#
# INF = math.inf
# input = sys.stdin.readline
#
#
# def dijkstra(student):
#     heap = []
#     distance[student][student] = 0
#     heapq.heappush(heap, [0, student])
#
#     while heap:
#         dist, start = heapq.heappop(heap)
#
#         if distance[student][start] < dist:
#             continue
#
#         for next_node, dist_next in adj_list[start]:
#             cost = dist + dist_next
#             if cost < distance[student][next_node]:
#                 distance[student][next_node] = cost
#                 heapq.heappush(heap, [cost, next_node])
#
# def dijkstra_v2(village):
#     heap = []
#     distance2[village] = 0
#     heapq.heappush(heap, [0, village])
#
#     while heap:
#         dist, start = heapq.heappop(heap)
#
#         if distance2[start] < dist:
#             continue
#
#         for next_node, dist_next in adj_list[start]:
#             cost = dist + dist_next
#             if cost < distance2[next_node]:
#                 distance2[next_node] = cost
#                 heapq.heappush(heap, [cost, next_node])
#
# N, M, X = map(int, input().split())
# adj_list = [[] for _ in range(N+1)]
# distance = [[INF]*(N+1) for _ in range(N+1)]
# distance2 = [INF]*(N+1)
#
# res = 0
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     adj_list[a].append([b,c])
#
#
# for i in range(1, N+1):
#     dijkstra(i)
#
# dijkstra_v2(X)
# for i in range(1, N+1):
#     res = max(res, distance[i][X] + distance2[i])
#
# print(res)


# v3
import math, heapq, sys

INF = math.inf
input = sys.stdin.readline


def dijkstra(student):
    heap = []
    distance[student][student] = 0
    heapq.heappush(heap, [0, student])

    while heap:
        dist, start = heapq.heappop(heap)

        if distance[student][start] < dist:
            continue

        for next_node, dist_next in adj_list[start]:
            cost = dist + dist_next
            if cost < distance[student][next_node]:
                distance[student][next_node] = cost
                heapq.heappush(heap, [cost, next_node])

N, M, X = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
distance = [[INF]*(N+1) for _ in range(N+1)]
res = 0


for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append([b,c])

for i in range(1, N+1):
    dijkstra(i)

for i in range(1, N+1):
    res = max(res, distance[i][X] + distance[X][i])

print(res)






