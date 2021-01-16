# baekjoon_11403 경로 찾기
import math
N = int(input())

adj_arr = [list(map(int, input().split())) for _ in range(N)]

INF = math.inf
for a in range(N):
    for b in range(N):
        if adj_arr[a][b] == 0:
            adj_arr[a][b] = INF

for k in range(N):
    for a in range(N):
        for b in range(N):
            adj_arr[a][b] = min(adj_arr[a][b], adj_arr[a][k]+adj_arr[k][b])

for i in range(N):
    for j in range(N):
        if adj_arr[i][j] != INF:
            adj_arr[i][j] = 1
        else:
            adj_arr[i][j] = 0
for k in range(N):
    print(*adj_arr[k])