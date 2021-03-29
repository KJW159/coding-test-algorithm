# baekjoon_17471 게리맨더링

# v1
# def dfs(start, k, cnt):
#     global res
#     if k == cnt:
#
#
#     for node in adj_list[start]:
#         if visited[node] == 0:
#             visited[node] = 1
#             dfs(node, k, cnt+1)
#             visited[node] = 0
#
#
# N = int(input())
# population = list(map(int, input().split()))
# population.insert(0,0)
# adj_list = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# res = 0
#
# for i in range(1, N+1):
#     tmp_list = list(map(int, input().split()))
#     area_num = tmp_list[0]
#     for j in range(1,area_num+1):
#         adj_list[i].append(tmp_list[j])

# for k in range(1, N//2+1):
#     for n in range(1, N+1):
#         visited[n] = 1
#         dfs(n, k, 1)

# v2
from itertools import combinations
import math

def dfs(zones, num):
    stack = []
    zones = list(zones)
    start = zones[0]
    stack.append(start)
    visited[start] = 1
    cnt = 1
    trg = False
    tmp = 0
    while stack:
        start = stack.pop()
        for node in adj_list[start]:
            if node in zones and visited[node] == 0:
                visited[node] = 1
                stack.append(node)
                cnt += 1
    if cnt == num:
        trg = True
        for node in zones:
            tmp += population[node]
    return trg, tmp


N = int(input())
population = list(map(int, input().split()))
population.insert(0, 0)
adj_list = [[] for _ in range(N + 1)]

res = math.inf
zone_num = set(range(1,N+1))


for i in range(1, N + 1):
    tmp_list = list(map(int, input().split()))
    area_num = tmp_list[0]
    for j in range(1, area_num + 1):
        adj_list[i].append(tmp_list[j])

zone_visited = []
for num in range(1, N//2+1):
    for zone1 in combinations(zone_num, num):
        zone1 = set(zone1)
        zone2 = zone_num - zone1
        if zone1 in zone_visited:
            continue
        zone_visited.append(zone1)
        visited = [0] * (N + 1)
        trg1, people1 = dfs(zone1, num)
        trg2, people2 = dfs(zone2, N-num)

        if trg1 and trg2:
            res = min(res, abs(people1 - people2))
if res == math.inf:
    print(-1)
else:
    print(res)