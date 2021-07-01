# baekjoon_17182 우주 탐사선


# 주어진 시간이 최소 시간이 아님. 즉 i -> j로 가는 게 최소 시간이 아니라 그냥 이동시간임.
# 다른 문제에서는 노드 간 이동 시간이 최소시간인데 여긴 최소 시간이라는 보장이 없음.
# 따라서 일단 플로이드 와샬로 주어진 시간에서 최소 시간으로 구하고 모든 노드 최소 시간 구하는 듯.
# 플로이드 와샬을 다시 봐야할 듯. 헷갈리네, 왜 별도로 dfs를 통해서 완전 탐색을 해야하는지.

# v1
# import math
#
# def dfs(x, cost, step):
#     global res
#     if step == N-1:
#         res = min(res, cost)
#         return
#
#     if cost > res:
#         return
#
#     for c in range(N):
#         if c != x and visited[c] == 0:
#             visited[c] = 1
#             dfs(c, cost + distance[x][c], step+1)
#             visited[c] = 0
#
#
# N, K = map(int, input().split())
# distance = [list(map(int, input().split())) for _ in range(N)]
# visited = [0]*N
# visited[K] = 1
# res = math.inf
#
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
#
# for x in range(N):
#     if x != K and visited[x] == 0:
#         visited[x] = 1
#         dfs(x, distance[k][x], 0)
#         visited[x] = 0
#
# print(res)


# v2
# import math
#
# def dfs(x, cost, step):
#     global res
#     if step == N-1:
#         res = min(res, cost)
#         return
#
#     if cost > res:
#         return
#
#     for c in range(N):
#         if c != x and visited[c] == 0:
#             visited[c] = 1
#             dfs(c, cost + distance[x][c], step+1)
#             visited[c] = 0
#
#
# N, K = map(int, input().split())
# distance = [list(map(int, input().split())) for _ in range(N)]
# visited = [0]*N
# visited[K] = 1
# res = math.inf
#
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
#
# dfs(K, 0, 0)
# print(res)


# v3
import math, sys

input = sys.stdin.readline

def dfs(x, cost, step):
    global res
    if step == N-1:
        res = min(res, cost)
        return

    if cost > res:
        return

    for c in range(N):
        if c != x and visited[c] == 0:
            visited[c] = 1
            dfs(c, cost + distance[x][c], step+1)
            visited[c] = 0


N, K = map(int, input().split())
distance = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
visited[K] = 1
res = math.inf

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

dfs(K, 0, 0)
print(res)