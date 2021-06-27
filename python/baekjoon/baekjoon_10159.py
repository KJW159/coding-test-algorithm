# baekjoon_10159 저울



# v1
#
# N = int(input())
# M = int(input())
#
# weight = [[2]*(N+1) for _ in range(N+1)]
#
# # 자기 자신은 비교 불가이니 1롤 초기화해줄 필요 없음.
# # for i in range(1, N+1):
# #     for j in range(1, N+1):
# #         if i == j:
# #             weight[i][j] = 1
#
# # 1은 비교 가능이고 a > b를 의미. 2는 비교 불가능(자기끼리 비교도 불가)
# for _ in range(M):
#     a, b = map(int, input().split())
#     weight[a][b] = 1
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if weight[i][k] + weight[k][j] == 2:
#                 weight[i][j] = 1
#
# for i in range(1,N+1):
#     res = 0
#     for j in range(1,N+1):
#         # 비교 불가능을 찾아야 하니깐 작을 수도 클 수도 있니까 둘다 만족해야하고
#         # 자기자신끼리도 불가능으로 되어 있어서 res가 +1 되지 않도록 해야함.
#         if weight[i][j] == 2 and weight[j][i] == 2 and i != j:
#             res += 1
#     print(res)

# v2
N = int(input())
M = int(input())

weight = [[2]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    weight[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if weight[i][k] + weight[k][j] == 2:
                weight[i][j] = 1

for i in range(1,N+1):
    res = 0
    for j in range(1,N+1):
        if weight[i][j] == 2 and weight[j][i] == 2 and i != j:
            res += 1
    print(res)

# v3
import sys

input = sys.stdin.readline


N = int(input())
M = int(input())

weight = [[2]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    weight[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if weight[i][k] + weight[k][j] == 2:
                weight[i][j] = 1

for i in range(1,N+1):
    res = 0
    for j in range(1,N+1):
        if weight[i][j] == 2 and weight[j][i] == 2 and i != j:
            res += 1
    print(res)