# baekjoon_15683 감시

# v1
# 좌, 상, 우 ,하
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# directions = [[],[[0],[1],[2],[3]],
#              [[0,2],[1,3]],
#              [[1,2],[2,3],[0,3],[0,1]],
#              [[1,2,3],[0,2,3],[0,1,3],[0,1,2]],
#              [[0,1,2,3]]
#              ]
# def checking(cctv, arr_tmp, direction):
#     s_i, s_j, cctv_num = cctv
#     for d in direction:
#         # 방향이 여러개인 것들은 시작점에서 여러번 출발해야하니깐 직접적으로 사용 못함.
#         x = s_i
#         y = s_j
#         while True:
#             x += dx[d]
#             y += dy[d]
#             if 0 <= x < N and 0 <= y < M:
#                 if arr_tmp[x][y] == 6:
#                     break
#                 elif arr_tmp[x][y] == 0:
#                     arr_tmp[x][y] = '#'
#             else:
#                 break
#
# def dfs(arr, cnt):
#     global res
#     if cnt == len(cctvs):
#         space = 0
#         for i in range(N):
#             for j in range(M):
#                 if arr[i][j] == 0:
#                     space += 1
#         res = min(res, space)
#         return
#     else:
#         # arr_tmp = [arr[i][:] for i in range(N)]
#         cctv = cctvs[cnt]
#         for direction in directions[cctv[2]]:
#             arr_tmp = [arr[i][:] for i in range(N)]
#             checking(cctv, arr_tmp, direction)
#             dfs(arr_tmp, cnt+1)
#
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# cctvs = []
# for i in range(N):
#     for j in range(M):
#         if 0 < arr[i][j] < 6:
#             cctvs.append([i,j,arr[i][j]])
#
# res = N*M
# dfs(arr, 0)
# print(res)


# re-v1
# import math
#
#
# def checking_space(arr_tmp, direction, cctv, safe_space):
#     c_i, c_j, cctv_kinds  = cctv
#     for d in direction:
#         x = c_i
#         y = c_j
#         while True:
#             x += dx[d]
#             y += dy[d]
#             if 0 <= x < N and 0 <= y < M:
#                 if arr_tmp[x][y] == 0:
#                     arr_tmp[x][y] = 7
#                     safe_space -= 1
#                 if arr_tmp[x][y] == 6:
#                     break
#             else:
#                 break
#     return safe_space
#
# def dfs(arr, cctvs, zero_space, cctvs_num, total_cctvs):
#     global res
#     if cctvs_num == total_cctvs:
#         res = min(res, zero_space)
#         return
#     else:
#         cctv = cctvs[cctvs_num]
#         for direction in directions[cctv[2]]:
#             arr_tmp = [arr[i][:] for i in range(N)]
#             zero_space_tmp = checking_space(arr_tmp, direction, cctv, zero_space)
#             dfs(arr_tmp, cctvs, zero_space_tmp, cctvs_num+1, total_cctvs)
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# cameras = []
#
# # 좌 상 우 하
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# directions = [
#     [],
#     [[0],[1],[2],[3]],
#     [[0,2],[1,3]],
#     [[0,1],[1,2],[2,3],[3,0]],
#     [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
#     [[0,1,2,3]]
# ]
#
# cctvs = []
# zero_space = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             zero_space += 1
#         if 1 <= arr[i][j] < 6:
#             cctvs.append([i,j,arr[i][j]])
# total_cctvs = len(cctvs)
# res = math.inf
# dfs(arr, cctvs, zero_space, 0, total_cctvs)
# print(res)

# re-v2
# import math
# def checking_space(direction, cctv, k1, k2):
#     c_i, c_j, cctv_kinds = cctv
#     for d in direction:
#         x = c_i
#         y = c_j
#         while True:
#             x += dx[d]
#             y += dy[d]
#             if 0 <= x < N and 0 <= y < M:
#                 if arr[x][y] == k1:
#                     arr[x][y] = k2
#                 if arr[x][y] == 6:
#                     break
#             else:
#                 break
#
# def dfs(cctvs, cctvs_num, total_cctvs):
#     global res
#     if cctvs_num == total_cctvs:
#         zero_space = 0
#         for i in range(N):
#             for j in range(M):
#                 if arr[i][j] == 0:
#                     zero_space += 1
#         res = min(res, zero_space)
#         return
#     else:
#         cctv = cctvs[cctvs_num]
#         for direction in directions[cctv[2]]:
#             checking_space(direction, cctv, 0, 7)
#             dfs(cctvs, cctvs_num+1, total_cctvs)
#             checking_space(direction, cctv, 7, 0)
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
#
# # 좌 상 우 하
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# directions = [
#     [],
#     [[0],[1],[2],[3]],
#     [[0,2],[1,3]],
#     [[0,1],[1,2],[2,3],[3,0]],
#     [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
#     [[0,1,2,3]]
# ]
#
# cctvs = []
#
# for i in range(N):
#     for j in range(M):
#         if 1 <= arr[i][j] < 6:
#             cctvs.append([i,j,arr[i][j]])
# total_cctvs = len(cctvs)
# res = math.inf
# dfs(cctvs, 0, total_cctvs)
# print(res)


# re-v3
import math
def checking_space(direction, cctv, k):
    c_i, c_j, cctv_kinds = cctv
    for d in direction:
        x = c_i
        y = c_j
        while True:
            x += dx[d]
            y += dy[d]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] >= 7:
                    arr[x][y] += k
                if arr[x][y] == 6:
                    break
            else:
                break

def dfs(cctvs, cctvs_num, total_cctvs):
    global res
    if cctvs_num == total_cctvs:
        zero_space = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 7:
                    zero_space += 1
        res = min(res, zero_space)
        return
    else:
        cctv = cctvs[cctvs_num]
        for direction in directions[cctv[2]]:
            checking_space(direction, cctv, 1)
            dfs(cctvs, cctvs_num+1, total_cctvs)
            checking_space(direction, cctv, -1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# 좌 상 우 하
dx = [0,-1,0,1]
dy = [-1,0,1,0]

directions = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

cctvs = []

for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] < 6:
            cctvs.append([i,j,arr[i][j]])
        if arr[i][j] == 0:
            arr[i][j] = 7
total_cctvs = len(cctvs)
res = math.inf
dfs(cctvs, 0, total_cctvs)
print(res)

