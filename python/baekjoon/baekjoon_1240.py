# baekjoon_1240 노드 사이의 거리

# v1
# import math
#
# INF = math.inf
#
#
# N, M = map(int, input().split())
# distance = [[INF]*(N+1) for _ in range(N+1)]
#
# for _ in range(N-1):
#     a, b, dist = map(int, input().split())
#     distance[a][b] = dist
#     distance[b][a] = dist
#
#
# for i in range(1, N+1):
#     distance[i][i] = 0
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     print(distance[a][b])


# v2
# import math, heapq
#
# INF = math.inf
#
#
# def dijkstra(start):
#     hq = []
#     heapq.heappush(hq, [0, start])
#     distance[start] = 0
#
#     while hq:
#         dist, cur_node = heapq.heappop(hq)
#         if distance[cur_node] < dist:
#             continue
#         for next_node, dist_input in adj_list[cur_node]:
#             next_dist = dist + dist_input
#             if next_dist < distance[next_node]:
#                 distance[next_node] = next_dist
#                 heapq.heappush(hq, [next_dist, next_node])
#
#
# N, M = map(int, input().split())
# adj_list = [[] for _ in range(N + 1)]
#
# for _ in range(N-1):
#     a, b, dist = map(int, input().split())
#     adj_list[a].append([b, dist])
#     adj_list[b].append([a, dist])
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     distance = [INF] * (N + 1)
#     dijkstra(a)
#     print(distance[b])



# v3
import math
from collections import deque

INF = math.inf


def bfs(start, end):
    queue = deque()
    queue.append(start)
    distance[start] = 0

    while queue:
        cur_node = queue.popleft()
        if cur_node == end:
            return
        for next_node, dist_input in adj_list[cur_node]:
            if distance[next_node] == INF:
                distance[next_node] = distance[cur_node] + dist_input
                queue.append(next_node)

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b, dist = map(int, input().split())
    adj_list[a].append([b, dist])
    adj_list[b].append([a, dist])

for _ in range(M):
    a, b = map(int, input().split())
    distance = [INF] * (N + 1)
    bfs(a, b)
    print(distance[b])