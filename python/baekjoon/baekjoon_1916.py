# baekjoon_1916 최소비용 구하기.

# v1
import sys
import math
import heapq

input = sys.stdin.readline


def dijkstra(start_city):
    distance[start_city] = 0
    heap = []
    heapq.heappush(heap, [0, start_city])

    while heap:
        dist, cur_city = heapq.heappop(heap)
        if distance[cur_city] < dist:
            continue
        for next_city, next_dist in adj_list[cur_city]:
            cost = distance[cur_city] + next_dist
            if distance[next_city] > cost:
                distance[next_city] = cost
                heapq.heappush(heap, [cost, next_city])


N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]
distance = [math.inf]*(N+1)

for _ in range(M):
    s,e,w = map(int, input().split())
    adj_list[s].append([e,w])

start_city, destination = map(int, input().split())

dijkstra(start_city)

print(distance[destination])
