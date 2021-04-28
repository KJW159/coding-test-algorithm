# baekjoon_21609 상어 중학교



# # v1
# from collections import defaultdict
#
# def dfs(x,y,block_num):
#     stack = []
#     stack.append([x,y])
#     visited[x][y] = 1
#
#     group_size = 1
#     # 무지개 리스트
#     rainbow_position = []
#     rainbow_cnt = 0
#     # 무지개 포함 블록 리스트
#     group_position = [[x,y]]
#     trg_tmp = True
#     # 무지개 없는 블록 리스트
#     block_position = [[x,y]]
#     standard_block = []
#
#     while stack:
#         x, y = stack.pop()
#         for c in range(4):
#             nx = x + dx[c]
#             ny = y + dy[c]
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
#                 if arr[nx][ny] == block_num:
#                     stack.append([nx, ny])
#                     visited[nx][ny] = 1
#                     group_size += 1
#                     group_position.append([nx,ny])
#                     block_position.append([nx,ny])
#                 if arr[nx][ny] == 0:
#                     stack.append([nx, ny])
#                     visited[nx][ny] = 1
#                     group_size += 1
#                     rainbow_cnt += 1
#                     group_position.append([nx, ny])
#                     rainbow_position.append([nx, ny])
#     if group_size > 1:
#         block_position.sort(key=lambda x: (x[0],x[1]))
#         standard_block = block_position[0]
#     else:
#         trg_tmp = False
#     return trg_tmp, group_position, group_size, rainbow_cnt, rainbow_position, standard_block
#
#
# def falling_block():
#     for f_x in range(N-2, -1, -1):
#         for f_y in range(N):
#             if 0 <= arr[f_x][f_y] <= M:
#                 block_num = arr[f_x][f_y]
#                 nx = f_x
#                 while True:
#                     if (nx+1) < N:
#                         if arr[nx+1][f_y] != -2:
#                             arr[f_x][f_y] = -2
#                             arr[nx][f_y] = block_num
#                             break
#                         else:
#                             nx += 1
#                     else:
#                         arr[f_x][f_y] = -2
#                         arr[nx][f_y] = block_num
#                         break
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# trg1 = False
# res = 0
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
#
# while True:
#     visited = [[0]*N for _ in range(N)]
#     group_idx = 1
#     group_dict = defaultdict(list)
#     group_ordered = []
#     for i in range(N):
#         for j in range(N):
#             if 1 <= arr[i][j] <= M and visited[i][j] == 0:
#                 trg2, group_position, group_size, rainbow_cnt, rainbow_position, standard_block = dfs(i,j, arr[i][j])
#                 if trg2:
#                     group_ordered.append([group_size, rainbow_cnt, standard_block[0], standard_block[1], group_idx])
#                     group_dict[group_idx].append(group_position)
#                     group_idx += 1
#                     trg1 = True
#                     for r_i, r_j in rainbow_position:
#                         visited[r_i][r_j] = 0
#     if not trg1:
#         break
#     else:
#         if group_ordered:
#             group_ordered.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
#             group_num = group_ordered[0][4]
#             res += group_ordered[0][0]**2
#             for i, j in group_dict[group_num][0]:
#                 arr[i][j] = -2
#             falling_block()
#             for _ in range(3):
#                 arr = list(list(zip(*arr[::-1])))
#             for i in range(N):
#                 arr[i] = list(arr[i])
#             falling_block()
#         else:
#             break
# print(res)



# v2
from collections import defaultdict

def dfs(x,y,block_num):
    stack = []
    stack.append([x,y])
    visited[x][y] = 1

    group_size = 1
    # 무지개 리스트
    rainbow_position = []
    rainbow_cnt = 0
    # 무지개 포함 블록 리스트
    group_position = [[x,y]]
    trg_tmp = True
    # 무지개 없는 블록 리스트
    block_position = [[x,y]]
    standard_block = []

    while stack:
        x, y = stack.pop()
        for c in range(4):
            nx = x + dx[c]
            ny = y + dy[c]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] == block_num:
                    stack.append([nx, ny])
                    visited[nx][ny] = 1
                    group_size += 1
                    group_position.append([nx,ny])
                    block_position.append([nx,ny])
                if arr[nx][ny] == 0:
                    stack.append([nx, ny])
                    visited[nx][ny] = 1
                    group_size += 1
                    rainbow_cnt += 1
                    group_position.append([nx, ny])
                    rainbow_position.append([nx, ny])
    if group_size > 1:
        block_position.sort(key=lambda x: (x[0],x[1]))
        standard_block = block_position[0]
    else:
        trg_tmp = False
    return trg_tmp, group_position, group_size, rainbow_cnt, rainbow_position, standard_block


def falling_block():
    for f_x in range(N-2, -1, -1):
        for f_y in range(N):
            if 0 <= arr[f_x][f_y] <= M:
                block_num = arr[f_x][f_y]
                nx = f_x
                while True:
                    if (nx+1) < N:
                        if arr[nx+1][f_y] != -2:
                            arr[f_x][f_y] = -2
                            arr[nx][f_y] = block_num
                            break
                        else:
                            nx += 1
                    else:
                        arr[f_x][f_y] = -2
                        arr[nx][f_y] = block_num
                        break

def rotating_block():
    arr_tmp = [[0]*N for _ in range(N)]
    for r_x in range(N):
        for r_y in range(N):
            arr_tmp[r_y][N-1-r_x] = arr[r_x][r_y]
    return arr_tmp

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
trg1 = False
res = 0

dx = [0,-1,0,1]
dy = [-1,0,1,0]


while True:
    visited = [[0]*N for _ in range(N)]
    group_idx = 1
    group_dict = defaultdict(list)
    group_ordered = []
    for i in range(N):
        for j in range(N):
            if 1 <= arr[i][j] <= M and visited[i][j] == 0:
                trg2, group_position, group_size, rainbow_cnt, rainbow_position, standard_block = dfs(i,j, arr[i][j])
                if trg2:
                    group_ordered.append([group_size, rainbow_cnt, standard_block[0], standard_block[1], group_idx])
                    group_dict[group_idx].append(group_position)
                    group_idx += 1
                    trg1 = True
                    for r_i, r_j in rainbow_position:
                        visited[r_i][r_j] = 0
    if not trg1:
        break
    else:
        if group_ordered:
            group_ordered.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
            group_num = group_ordered[0][4]
            res += group_ordered[0][0]**2
            for i, j in group_dict[group_num][0]:
                arr[i][j] = -2
            falling_block()
            for _ in range(3):
                arr = rotating_block()
            falling_block()
        else:
            break
print(res)