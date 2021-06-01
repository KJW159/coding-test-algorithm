# baekjoon_7576 토마토
import collections

# v2
# def check(tomato_c, queue, cnt):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#     x_i, y_j = tomato_c
#     for c in range(4):
#         x = x_i + dx[c]
#         y = y_j + dy[c]
#         if 0 <= x < N and 0 <= y < M:
#             if arr[x][y] == 0 and visited[x][y] == 0:
#                 queue.append([x, y])
#                 visited[x][y] = arr[x_i][y_j] + 1
#                 if cnt < visited[x][y]:
#                     cnt = visited[x][y]
#             if arr[x][y] == -1 and visited[x][y] == 0:
#                 visited[x][y] = 1
#                 cnt = 0
#             if arr[x][y] == 1 and visited[x][y] == 0:
#                 visited[x][y] = 1
#                 cnt = -1
#     return cnt
#
#
#
# def bfs(i, j):
#
#     queue = collections.deque()
#     queue.append([i, j])
#     visited[i][j] = 1
#     cnt = 0
#     while queue:
#         if len(queue) == 0:
#             return cnt
#         tomato_c = queue.popleft()
#         cnt = check(tomato_c, queue, cnt)
#
#
# M, N = list(map(int, input().split()))
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# res_tmp = -1
# res = 0
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1 and visited[i][j] == 0:
#             res = bfs(i, j)
#         elif arr[i][j] == 0 and visited[i][j] == 0:
#             res = res_tmp
#         elif arr[i][j] == -1 and visited[i][j] == 0:
#             res = res_tmp
#
# print('{}'.format(res))

#v3
# import collections
#
# def tomato_bfs():
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     queue = collections.deque(start_point)
#     print(queue)
#
#     while queue:
#         i_x, j_y = queue.popleft()
#         for c in range(4):
#             x = i_x + dx[c]
#             y = j_y + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if arr[x][y] == 0:
#                     queue.append([x,y])
#                     arr[x][y] = arr[i_x][j_y] + 1
#
# M, N = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(N)]
# start_point = []
# date = 0
# res = True
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             start_point.append([i,j])
#
# tomato_bfs()
#
# for i in arr:
#     if 0 in i:
#         res = False
#         break
#     for j in i:
#         if j > date:
#             date = j
#
# if res:
#     print(date-1)
# else:
#     print(-1)


# re-v1

from collections import deque


# def bfs():
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#
#     queue = deque()
#
#     for tomato in tomatos:
#         queue.append([tomato[0], tomato[1]])
#
#     while queue:
#         t_i, t_j = queue.popleft()
#         for c in range(4):
#             x = t_i + dx[c]
#             y = t_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if box[x][y] == 0:
#                     queue.append([x,y])
#                     box[x][y] = box[t_i][t_j] + 1
#
#
# M, N = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# days = 0
# tomatos = []
# for i in range(N):
#     for j in range(M):
#         if box[i][j] == 1:
#             tomatos.append([i,j])
# bfs()
# trg = False
# for i in range(N):
#     if trg:
#         res = -1
#         break
#     for j in range(M):
#         if box[i][j] == 0:
#             trg = True
#             break
#         elif box[i][j] > days:
#             days = box[i][j]
#
# if trg:
#     print(res)
# else:
#     print(days-1)




# re-v2


from collections import deque

def bfs():
    global res
    queue = deque(tomato)
    cnt = 0

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if farm[x][y] == 0:
                    queue.append([x,y])
                    farm[x][y] = farm[s_i][s_j] + 1
                    res = max(res, farm[x][y])
                    cnt += 1
    return cnt

M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]

tomato = []
tomato_zero = 0
res = 0

dx = [0,-1,0,1]
dy = [-1,0,1,0]
for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            tomato.append([i,j])
        if farm[i][j] == 0:
            tomato_zero += 1

red_tomato = bfs()

if red_tomato == tomato_zero:
    res -= 1
    res = max(res, 0)
    print(res)
else:
    print(-1)
