# baekjoon_10282 해킹

#1
import heapq, sys, math

input = sys.stdin.readline
INF = math.inf

def dijkstra(start):
    hq = []
    distance[start] = 0
    heapq.heappush(hq, [0, start])

    while hq:
        dist, cur_node = heapq.heappop(hq)
        if distance[cur_node] < dist:
            continue

        for next_node, next_dist in adj_list[cur_node]:
            cost = next_dist + dist
            if cost < distance[next_node]:
                heapq.heappush(hq, [cost, next_node])
                distance[next_node] = cost


T = int(input())

for t in range(T):
    n, d, c = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        adj_list[b].append([a, s])

    dijkstra(c)
    res = [0,0]
    for i in range(1, n+1):
        if distance[i] != INF:
            res[0] += 1
            res[1] = max(res[1], distance[i])
    print(*res)