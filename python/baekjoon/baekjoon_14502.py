# baekjoon_14502 연구소
# import sys
# import collections

# def comb(safety_zones, r):
#     for n in range(len(safety_zones)):
#         if r == 1:
#             yield [safety_zones[n]]
#         else:
#             for next in comb(safety_zones[n+1:], r-1):
#                 yield [safety_zones[n]] + next
#
# def virus_bfs(arr_copy):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#     cnt  = 0
#
#     queue = collections.deque()
#     for virus in viruses:
#         queue.append(virus)
#
#     while queue:
#         v_x, v_y = queue.popleft()
#         for c in range(4):
#             x = v_x + dx[c]
#             y = v_y + dy[c]
#             if 0 <= x < N and 0<= y < M:
#                 if arr_copy[x][y] == 0:
#                     arr_copy[x][y] = 2
#                     queue.append([x,y])
#     for u in range(N):
#         for v in range(M):
#             if arr_copy[u][v] == 0:
#                 cnt += 1
#     return cnt
#
#
#
# def setting_wall(safety_zone):
#     w1, w2, w3 = safety_zone
#     arr_copy = [arr[i][:] for i in range(N)]
#
#     arr_copy[w1[0]][w1[1]] = 1
#     arr_copy[w2[0]][w2[1]] = 1
#     arr_copy[w3[0]][w3[1]] = 1
#
#     return virus_bfs(arr_copy)
#
#
# N, M = map(int, input().split())
#
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# safety_zones = []
# viruses = []
# safety_max = 0
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             safety_zones.append([i,j])
#         if arr[i][j] == 2:
#             viruses.append([i,j])
#
#
# for safety_zone in comb(safety_zones, 3):
#     res_tmp = setting_wall(safety_zone)
#     if res_tmp > safety_max:
#         safety_max = res_tmp
#
# print(safety_max)

# re-v1
# from collections import deque
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]]+next
#
# def spreading(rooms):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#     lab_copy = [lab[i][:] for i in range(N)]
#
#     for r_i, r_j in rooms:
#         lab_copy[r_i][r_j] = 1
#
#     queue = deque()
#     for virus in viruses:
#         queue.append(virus)
#
#     virus_cnt = 0
#     while queue:
#         v_i, v_j = queue.popleft()
#         for c in range(4):
#             x = v_i + dx[c]
#             y = v_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if lab_copy[x][y] == 0:
#                     queue.append([x,y])
#                     lab_copy[x][y] = 2
#                     virus_cnt += 1
#     return virus_cnt
#
#
# N, M = map(int, input().split())
#
# lab = [list(map(int, input().split())) for _ in range(N)]
#
# empty = []
# viruses = []
# res = 0
# for i in range(N):
#     for j in range(M):
#         if lab[i][j] == 0:
#             empty.append([i,j])
#         if lab[i][j] == 2:
#             viruses.append([i,j])
#
# safe_room = len(empty)-3
# for rooms in combinations1(empty, 3):
#     tmp = safe_room - spreading(rooms)
#     res = max(res, tmp)
# print(res)

# re-v2
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]]+next
#
# def spreading_dfs(rooms):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#     lab_copy = [lab[i][:] for i in range(N)]
#
#     for r_i, r_j in rooms:
#         lab_copy[r_i][r_j] = 1
#
#     stack = []
#     for virus in viruses:
#         stack.append(virus)
#
#     virus_cnt = 0
#     while stack:
#         v_i, v_j = stack.pop()
#         for c in range(4):
#             x = v_i + dx[c]
#             y = v_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if lab_copy[x][y] == 0:
#                     stack.append([x,y])
#                     lab_copy[x][y] = 2
#                     virus_cnt += 1
#     return virus_cnt
#
#
# N, M = map(int, input().split())
#
# lab = [list(map(int, input().split())) for _ in range(N)]
#
# empty = []
# viruses = []
# res = 0
# for i in range(N):
#     for j in range(M):
#         if lab[i][j] == 0:
#             empty.append([i,j])
#         if lab[i][j] == 2:
#             viruses.append([i,j])
#
# safe_room = len(empty)-3
# for rooms in combinations1(empty, 3):
#     tmp = safe_room - spreading_dfs(rooms)
#     res = max(res, tmp)
# print(res)



# re-v3
from itertools import combinations
from collections import deque


def spreading(viruses, zone_num_tmp):
    queue = deque(viruses)
    zone_num_tmp -= 3
    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if arr_tmp[x][y] == 0:
                    queue.append([x,y])
                    arr_tmp[x][y] = 2
                    zone_num_tmp -= 1
    return zone_num_tmp

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0
safety_zone = []
viruses = []

dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            safety_zone.append([i,j])
        if arr[i][j] == 2:
            viruses.append([i,j])
zone_num = len(safety_zone)
for wall in combinations(safety_zone, 3):
    arr_tmp = [arr[i][:] for i in range(N)]
    for w1, w2 in wall:
        arr_tmp[w1][w2] = 1
    res = max(res, spreading(viruses, zone_num))
print(res)



