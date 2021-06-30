# baekjoon_11404 플로이드

# v1
import sys, math

INF = math.inf

N = int(input())
M = int(input())

cost = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if c < cost[a][b]:
        cost[a][b] = c

for i in range(1, N+1):
    cost[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
            # cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if cost[i][j] == INF:
            print("0", end=" ")
        else:
            print("{} ".format(cost[i][j]), end="")
    print()

