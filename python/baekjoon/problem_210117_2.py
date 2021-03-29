# 나동빈 플로이드 워셜 알고리즘
import math

def floyd_w():
    for k in range(1,N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])


N, M = map(int, input().split())

INF = math.inf
distance = [[INF]*(N+1) for _ in range(N+1)]

for __ in range(M):
    x, y = map(int, input().split())
    distance[x][y] = 1
    distance[y][x] = 1
destination, K = map(int, input().split())

for k in range(N+1):
    distance[k][k] = 0

floyd_w()
res = distance[1][K] + distance[K][destination]
if res == INF:
    print(-1)
else:
    print(res)
