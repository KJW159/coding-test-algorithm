# baekjoon_1719 택배

# v1
# import math, sys
#
# input = sys.stdin.readline
# INF = math.inf
#
# N, M = map(int, input().split())
#
# distance = [[INF]*(N+1) for _ in range(N+1)]
# route = [[0]*(N+1) for _ in range(N+1)]
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     distance[a][b] = c
#     distance[b][a] = c
#     route[a][b] = b
#     route[b][a] = a
#
# for i in range(1, N+1):
#     distance[i][i] = 0
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if distance[i][j] > distance[i][k] + distance[k][j]:
#                 distance[i][j] = distance[i][k] + distance[k][j]
#                 # if route[i][j] > k:
#                 route[i][j] = k
# print(distance)
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i == j:
#             print("-", end=" ")
#         else:
#             print(route[i][j],end=" ")
#     print()


# v2
import math, sys

input = sys.stdin.readline
INF = math.inf

N, M = map(int, input().split())

distance = [[INF]*(N+1) for _ in range(N+1)]
route = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    distance[a][b] = c
    distance[b][a] = c
    route[a][b] = b
    route[b][a] = a

for i in range(1, N+1):
    distance[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                route[i][j] = route[i][k]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            print("-", end=" ")
        else:
            print(route[i][j],end=" ")
    print()








