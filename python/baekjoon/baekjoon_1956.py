# baekjoon_1956 운동

# 조건

# 도로의 정보가 주어짐. a,b,c 임.
# a -> b 이고 거리가 c임.
# 도로 길이의 합이 가장 작은 사이클 찾아 도로 길이의 합을 출력함.
# 불가능한 경우에는 -1을 출력함.


# 풀이
# 플로이드 와샬로 최단 거리 테이블 만듬
# 사이클이 있는 지 체크함
# 사이클 있으면 사이클 돌면서 거리 더해서 최단 거리 구함.
# 이렇게 해야하나 했는데 그냥 플로이드 와샬로 풀면 됐음.
# i에서 출발해서 j에 갈때의 비용을 2차원 행렬로 나타내니깐, i==j가 같으면 사이클임.
# 그리고 거기에 적혀있는 게 가장 작은 비용임. 따라서 이런 경우에는 i -> i 로 가는 경우를
# 처음에 초기화 시켜주면 안됌.

# v1
# import math
# import sys
#
# input = sys.stdin.readline
#
#
# V, E = map(int, input().split())
# INF = math.inf
# res = math.inf
# distance = [[INF]*(V+1) for _ in range(V+1)]
#
# # for i in range(1,V+1):
# #     for j in range(1, V+1):
# #         if i == j:
# #             distance[i][j] = 0
#
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     distance[a][b] = c
#
# for k in range(1, V+1):
#     for i in range(1, V+1):
#         for j in range(1, V+1):
#             distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
#
# for i in range(1, V+1):
#     res = min(res, distance[i][i])
#
# if res == INF:
#     print(-1)
# else:
#     print(res)

# v2
import math
import sys

input = sys.stdin.readline


V, E = map(int, input().split())
INF = math.inf
res = math.inf
distance = [[INF]*(V+1) for _ in range(V+1)]

# for i in range(1,V+1):
#     for j in range(1, V+1):
#         if i == j:
#             distance[i][j] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if distance[i][j] > distance[i][k]+distance[k][j]:
                distance[i][j] = distance[i][k]+distance[k][j]

for i in range(1, V+1):
    res = min(res, distance[i][i])

if res == INF:
    print(-1)
else:
    print(res)
