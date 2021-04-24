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
# import math
# def permutations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in permutations1(arr[:i]+arr[i+1:], r-1):
#                 yield [arr[i]] + next
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
# for rotation in permutations1(rotations, K):
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




#re-v1


# 조건
# 배열 A의 각 행의 합의 최소값이 배열 A의 값
# 행, 열 1부터 시작함.
# r,c,s
# 가장 윗칸이 r-s,c-s, 아래가 r+s, c+s
# 주어진 r,c,s 배열을 시계방향으로 1회 회전시킴.
# 이때의 최소값
# 풀이

# 행, 열 1부터 시작하므로 -1 해서 받을 것.
# 연산 순서에 따라서 달라지니
# 범위 크기 만큼 배열만듬.
# r-s,c-s 해당 하는 값 따로 빼두고 왼쪽 해서 내려가면서 당김.
# 가장 마지막 행에서 왼쪽에서 출발해서 당김.
# 오른쪽 열에서 올라가면서 당김.
# 가장 위에 행에서 왼쪽으로 가면서 당김.
# 아까 따로 빼둔 값을 r-s,c-s+1 칸에 저장함.
# 그리고 r-s+1, c-s+1을 해줌.(즉 가장 상단에 i에 대한 for문이 돔.0부터 S-1까지)
# 모든 연산 끝나면 행을 더하고 최소값 비교, 끝냄.

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
for k in range(K):
    r,c,s = map(int, input().split())
    rotations.append([r-1,c-1,s])

res = math.inf

for orders in permutations1(rotations, K):
    arr_tmp = [arr[j][:] for j in range(N)]
    for rotation in orders:
        r,c,s = rotation
        for i in range(s):
            val_tmp = arr_tmp[r-s+i][c-s+i]
            for r1 in range(r-s+i, r+s-i):
                arr_tmp[r1][c-s+i] = arr_tmp[r1+1][c-s+i]
            for c1 in range(c-s+i, c+s-i):
                arr_tmp[r+s-i][c1] = arr_tmp[r+s-i][c1+1]
            for r1 in range(r+s-i, r-s+i, -1):
                arr_tmp[r1][c+s-i] = arr_tmp[r1-1][c+s-i]
            for c1 in range(c+s-i, c-s+i, -1):
                arr_tmp[r-s+i][c1] = arr_tmp[r-s+i][c1-1]
            arr_tmp[r-s+i][c-s+1+i] = val_tmp

    for row in arr_tmp:
        num_sum = sum(row)
        res = min(res, num_sum)

print(res)





























