# baekjoon_2636 치즈
# import collections
#
# def bfs(s_i, s_j):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#
#     queue = collections.deque()
#     queue.append([s_i, s_j])
#     visited[s_i][s_j] = 1
#     cheeze_cnt_tmp = 0
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if arr[x][y] == 0 and visited[x][y] == 0:
#                     queue.append([x,y])
#                     visited[x][y] = 1
#                 if arr[x][y] == 1 and visited[x][y] == 0:
#                     cheeze_cnt_tmp += 1
#                     arr[x][y] = 0
#                     visited[x][y] = 1
#
#     return cheeze_cnt_tmp
#
#
#
# N, M = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# hours = 0
# cheeze_cnt = 0
#
# while True:
#     visited = [[0]*M for __ in range(N)]
#     tmp = bfs(0,0)
#     if tmp > 0:
#         cheeze_cnt = tmp
#         hours += 1
#     elif tmp == 0:
#         break
# print("{}\n{}".format(hours, cheeze_cnt))


# re-v1

from collections import deque

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def melting_cheeze():
    queue = deque()
    queue.append([0,0])
    visited[0][0] = 1
    cheezes_tmp = []

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0<= y < M and visited[x][y] == 0:
                if arr[x][y] == 0:
                    queue.append([x,y])
                    visited[x][y] = 1
                if arr[x][y] == 1:
                    cheezes_tmp.append([x,y])
                    visited[x][y] = 1
    return cheezes_tmp

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheeze_cnt = 0
step = 0
while True:
    visited = [[0]*M for _ in range(N)]
    cheezes = melting_cheeze()
    if cheezes:
        for c_i, c_j in cheezes:
            arr[c_i][c_j] = 0
        cheeze_cnt = len(cheezes)
        step += 1
    else:
        break
print(step)
print(cheeze_cnt)