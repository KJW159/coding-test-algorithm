# baekjoon_1504 특정한 최단 경로





# v1

import sys, math, heapq

input = sys.stdin.readline
INF = math.inf

def dijkstra(start):
    distance = [INF] * (N + 1)
    heap = []
    distance[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue
        for next_node, next_dist in adj_list[node]:
            cost = dist + next_dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(heap, [cost, next_node])
    return distance


N, E = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

V1, V2 = map(int, input().split())

from_one = dijkstra(1)
from_v1 = dijkstra(V1)
from_v2 = dijkstra(V2)
res = min(from_one[V1]+from_v1[V2]+from_v2[N], from_one[V2]+from_v2[V1]+from_v1[N])

if res != INF:
    print(res)
else:
    print(-1)