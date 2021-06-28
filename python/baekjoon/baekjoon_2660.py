# baekjoon_2660 회장 뽑기

# v1
# import math
# import sys
#
# input = sys.stdin.readline
# INF = math.inf
# res = INF
# candiates = []
# N = int(input())
#
# friends = [[INF]*(N+1) for _ in range(N+1)]
#
# for i in range(1, N+1):
#         friends[i][i] = 0
#
# while True:
#     a, b = map(int, input().split())
#     if a == -1 and b == -1:
#         break
#     friends[a][b] = 1
#     friends[b][a] = 1
#
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             friends[i][j] = min(friends[i][j], friends[i][k]+friends[k][j])
#
#
# for i in range(1, N+1):
#     score_tmp = max(friends[i][1:])
#     if res > score_tmp:
#         res = score_tmp
#         candiates = [i]
#     elif res == score_tmp:
#         candiates.append(i)
#
# print("{} {}".format(res, len(candiates)))
# print(*candiates)


# v2
import math
import sys

input = sys.stdin.readline
INF = math.inf
res = INF
candiates = []
N = int(input())

friends = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
        friends[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    friends[a][b] = 1
    friends[b][a] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if friends[i][j] == 1 or friends[i][j] == 0:
                continue
            elif friends[i][j] > friends[i][k] + friends[k][j]:
                friends[i][j] = friends[i][k]+friends[k][j]


for i in range(1, N+1):
    score_tmp = max(friends[i][1:])
    if res > score_tmp:
        res = score_tmp
        candiates = [i]
    elif res == score_tmp:
        candiates.append(i)

print("{} {}".format(res, len(candiates)))
print(*candiates)

