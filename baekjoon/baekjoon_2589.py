# baekjoon_2589 보물섬
# import collections
#
#
# def bfs(s_i, s_j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     visited = [[0]*M for _ in range(N)]
#     queue = collections.deque()
#     queue.append([s_i, s_j])
#     visited[s_i][s_j] = 1
#     time = 0
#
#     while queue:
#         s_i, s_j = queue.popleft()
#
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if visited[x][y] == 0 and arr[x][y] == 'L':
#                     queue.append([x,y])
#                     visited[x][y] = visited[s_i][s_j] + 1
#
#     for n in range(N):
#         for m in range(M):
#             if visited[n][m] > time:
#                 time = visited[n][m]
#
#     return time-1
#
#
#
# N, M = map(int, input().split())
#
# arr = [list(input()) for _ in range(N)]
#
# res = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'L':
#             tmp = bfs(i,j)
#             if tmp > res:
#                 res = tmp
# print(res)

# v2
# import collections
#
#
# def bfs(s_i, s_j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     visited = [[0]*M for _ in range(N)]
#     queue = collections.deque()
#
#     visited[s_i][s_j] = 1
#     queue.append([s_i, s_j, visited[s_i][s_j]])
#     time = 0
#
#     while queue:
#         s_i, s_j, dist = queue.popleft()
#
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if visited[x][y] == 0 and arr[x][y] == 'L':
#                     visited[x][y] = visited[s_i][s_j] + 1
#                     queue.append([x,y,visited[x][y]])
#     if dist > time:
#         time = dist
#
#     return time-1
#
#
#
# N, M = map(int, input().split())
#
# arr = [list(input()) for _ in range(N)]
#
# res = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'L':
#             tmp = bfs(i,j)
#             if tmp > res:
#                 res = tmp
# print(res)

# v3

import collections


def bfs(s_i, s_j):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    visited = [[0]*M for _ in range(N)]
    queue = collections.deque()

    visited[s_i][s_j] = 1
    queue.append([s_i, s_j])
    time = 0

    while queue:
        s_i, s_j = queue.popleft()

        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if visited[x][y] == 0 and arr[x][y] == 'L':
                    visited[x][y] = visited[s_i][s_j] + 1
                    queue.append([x,y])
                    time = max(time, visited[x][y])

    return time-1



N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            tmp = bfs(i,j)
            if tmp > res:
                res = tmp
print(res)