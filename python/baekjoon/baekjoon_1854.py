# baekjoon_1854 K번째 최단경로 찾기

# v1
# import sys, heapq, math
#
# input = sys.stdin.readline
# INF = math.inf
#
#
# def dijkstra():
#     hq = []
#     heapq.heappush(hq, [0, 1])
#     visited[1][K-1] = 0
#     visited[1].sort()
#
#     while hq:
#         dist, cur_node = heapq.heappop(hq)
#
#         for next_node, next_dist in adj_list[cur_node]:
#             cost = next_dist + dist
#             if cost < visited[next_node][K-1]:
#                 heapq.heappush(hq, [cost, next_node])
#                 visited[next_node][K-1] = cost
#                 visited[next_node].sort()
#
#
# N, M, K = map(int, input().split())
# visited = [[INF]*K for _ in range(N+1)]
# adj_list = [[] for _ in range(N+1)]
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     adj_list[a].append([b, c])
#
# dijkstra()
#
# for i in range(1, N+1):
#     if visited[i][K-1] == INF:
#         print(-1)
#     else:
#         print(visited[i][K-1])


# v2
import sys, heapq, math

input = sys.stdin.readline
INF = math.inf


def dijkstra():
    hq = []
    heapq.heappush(hq, [0, 1])
    visited[1][0] = 0

    while hq:
        dist, cur_node = heapq.heappop(hq)

        for next_node, next_dist in adj_list[cur_node]:
            cost = next_dist + dist
            if cost < visited[next_node][K-1]:
                heapq.heappush(hq, [cost, next_node])
                visited[next_node][K-1] = cost
                visited[next_node].sort()


N, M, K = map(int, input().split())
visited = [[INF]*K for _ in range(N+1)]
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])

dijkstra()

for i in range(1, N+1):
    if visited[i][K-1] == INF:
        print(-1)
    else:
        print(visited[i][K-1])


