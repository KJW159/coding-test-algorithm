# baekjoon_17406 배열 돌리기 4


# v1
# from itertools import permutations
#
#
# N, M, K = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# rotations = []
# for _ in range(K):
#     r,c,s = map(int, input().split())
#     rotations.append([r-1, c-1, s])
#
# for rotation in permutations(rotations):
#     arr_tmp = [arr[i][:] for i in range(N)]
#     print(rotation)
#     for cal in rotation:
#         r, c, s = cal
#         part_tmp = [arr_tmp[j][c-s:c+s+1] for j in range(r-s, r+s+1)]
#         part_tmp = list(zip(*part_tmp[::-1]))
#         print(part_tmp)
#         nx = 0
#         for x in range(r-s, r+s+1):
#             ny = 0
#             for y in range(c-s, c+s+1):
#                 arr_tmp[x][y] = part_tmp[nx][ny]
#                 ny += 1
#             nx += 1

# v2
# from itertools import permutations
# import math
#
#
# N, M, K = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# rotations = []
# res = math.inf
# for _ in range(K):
#     r,c,s = map(int, input().split())
#     rotations.append([r-1, c-1, s])
#
# for rotation in permutations(rotations):
#     part_tmp = [arr[i][:] for i in range(N)]
#     for cal in rotation:
#         r, c, s = cal
#         # 한칸씩 회전
#         for n in range(s, 0, -1):
#             tmp = part_tmp[r-n][c+n]
#             part_tmp[r-n][c-n+1:c+n+1] = part_tmp[r-n][c-n:c+n]
#             for x in range(r-n, r+n):
#                 part_tmp[x][c-n] = part_tmp[x+1][c-n]
#             part_tmp[r+n][c-n:c+n] = part_tmp[r+n][c-n+1:c+n+1]
#             for x in range(r+n, r-n, -1):
#                 part_tmp[x][c+n] = part_tmp[x-1][c+n]
#             part_tmp[r-n+1][c+n] = tmp
#
#     for row in part_tmp:
#         res = min(res, sum(row))
#
# print(res)


# v3
import math
def permutations1(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutations1(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + next


N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
rotations = []
res = math.inf
for _ in range(K):
    r,c,s = map(int, input().split())
    rotations.append([r-1, c-1, s])

for rotation in permutations1(rotations, K):
    part_tmp = [arr[i][:] for i in range(N)]
    for cal in rotation:
        r, c, s = cal
        # 한칸씩 회전
        for n in range(s, 0, -1):
            tmp = part_tmp[r-n][c+n]
            part_tmp[r-n][c-n+1:c+n+1] = part_tmp[r-n][c-n:c+n]
            for x in range(r-n, r+n):
                part_tmp[x][c-n] = part_tmp[x+1][c-n]
            part_tmp[r+n][c-n:c+n] = part_tmp[r+n][c-n+1:c+n+1]
            for x in range(r+n, r-n, -1):
                part_tmp[x][c+n] = part_tmp[x-1][c+n]
            part_tmp[r-n+1][c+n] = tmp

    for row in part_tmp:
        res = min(res, sum(row))

print(res)

