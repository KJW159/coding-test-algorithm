# baekjoon_2638 치즈
#v1
# from collections import deque
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# def melting_cheeze(c_i, c_j):
#     air_cnt = 0
#     melting_trg = False
#     for k in range(4):
#         c_x = c_i + dx[k]
#         c_y = c_j + dy[k]
#         if 0 <= c_x < N and 0 <= c_y < M and visited[c_x][c_y] == 1 and arr[c_x][c_y] == 0:
#             air_cnt += 1
#             if air_cnt == 2:
#                 melting_trg = True
#                 break
#     return melting_trg
#
#
# def bfs():
#     queue = deque()
#     queue.append([0, 0])
#     visited[0][0] = 1
#     cheezes_tmp = []
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M and visited[x][y] == 0:
#                 if arr[x][y] == 0:
#                     queue.append([x,y])
#                     visited[x][y] = 1
#                 if arr[x][y] == 1:
#                     cheezes_tmp.append([x, y])
#                     visited[x][y] = 1
#     return cheezes_tmp
#
#
# N, M = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# melting_time = 0
#
# while True:
#     trg = False
#     visited = [[0]*M for __ in range(N)]
#     cheezes = bfs()
#     for c_i, c_j in cheezes:
#         melting = melting_cheeze(c_i,c_j)
#         print(melting)
#         if melting == True:
#             arr[c_i][c_j] = 0
#     for i in range(N):
#         if trg:
#             break
#         for j in range(M):
#             if arr[i][j] == 1:
#                 trg = True
#                 melting_time += 1
#                 break
#     if trg == False:
#         melting_time += 1
#         break
# print(melting_time)


# v2
from collections import deque

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def melting_cheeze(c_i, c_j):
    air_cnt = 0
    melting_trg = False
    for k in range(4):
        c_x = c_i + dx[k]
        c_y = c_j + dy[k]
        if 0 <= c_x < N and 0 <= c_y < M and visited[c_x][c_y] == 1 and arr[c_x][c_y] == 0:
            air_cnt += 1
            if air_cnt == 2:
                melting_trg = True
                break
    return melting_trg


def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    cheezes_tmp = []

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M and visited[x][y] == 0:
                if arr[x][y] == 0:
                    queue.append([x,y])
                    visited[x][y] = 1
                if arr[x][y] == 1:
                    cheezes_tmp.append([x, y])
                    visited[x][y] = 1
    return cheezes_tmp


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
melting_time = 0

while True:
    trg = False
    visited = [[0]*M for __ in range(N)]
    cheezes_cand = bfs()
    cheezes = []
    for c_i, c_j in cheezes_cand:
        melting = melting_cheeze(c_i, c_j)
        if melting == True:
            cheezes.append([c_i, c_j])
    for cheeze in cheezes:
        arr[cheeze[0]][cheeze[1]] = 0
    for i in range(N):
        if trg:
            break
        for j in range(M):
            if arr[i][j] == 1:
                trg = True
                melting_time += 1
                break
    if trg == False:
        melting_time += 1
        break
print(melting_time)




