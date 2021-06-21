# baekjoon_11779 최소비용 구하기2




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
                route[next_city] = cur_city

def finding_route(destination, start_city):
    res_tmp = [destination]
    x = destination
    while True:
        y = route[x]
        if y == start_city:
            res_tmp.append(y)
            return res_tmp
        else:
            res_tmp.append(y)
            x = y

N = int(input())
M = int(input())
adj_list = [[] for _ in range(N+1)]
distance = [math.inf]*(N+1)
route = [i for i in range(N+1)]


for _ in range(M):
    a,b,w = map(int, input().split())
    adj_list[a].append([b,w])

start_city, destination = map(int, input().split())


dijkstra(start_city)
res = finding_route(destination, start_city)
res.reverse()
print(distance[destination])
print(len(res))
print(*res)