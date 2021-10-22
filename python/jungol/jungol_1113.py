#jungol_1113    119 구급대


# v1
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     visited = [[-1]*M for _ in range(N)]
#     visited[0][0] = 0
#     x,y = 0,0
#     for c in range(4):
#         x += dx[c]
#         y += dy[c]
#         if 0 <= x < N and 0 <= y < M and arr[x][y] == 1:
#             queue.append([x, y, c])
#             visited[x][y] = 0
#
#     while queue:
#         x, y, direction = queue.popleft()
#
#         if x == d_x-1 and y == d_y-1:
#             return visited[x][y]
#
#         for c in range(4):
#             nx = x + dx[c]
#             ny = y + dy[c]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if arr[nx][ny] == 1 and visited[nx][ny] == -1:
#                     queue.append([nx, ny, c])
#                     if direction != c:
#                         visited[nx][ny] = visited[x][y] + 1
#                     else:
#                         visited[nx][ny] = visited[x][y]
#     return 0
#
# M, N = map(int, input().split())
# # -1 씩 해야함.
# d_x, d_y = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
#
# res = bfs()
#
# print(res)


# v2
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     visited = [[-1]*M for _ in range(N)]
#     visited[0][0] = 0
#     x,y = 0,0
#     for c in range(4):
#         x += dx[c]
#         y += dy[c]
#         if 0 <= x < N and 0 <= y < M and arr[x][y] == 1:
#             queue.append([x, y, c])
#             visited[x][y] = 0
#
#     while queue:
#         x, y, direction = queue.popleft()
#
#         if x == d_x-1 and y == d_y-1:
#             return visited[x][y]
#
#         for c in range(4):
#             nx = x + dx[c]
#             ny = y + dy[c]
#             if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
#                 if direction != c:
#                     if visited[nx][ny] == -1:
#                         visited[nx][ny] = visited[x][y] + 1
#                         queue.append([nx, ny, c])
#                     elif visited[nx][ny] > visited[x][y] + 1:
#                         visited[nx][ny] = visited[x][y] + 1
#                         queue.append([nx, ny, c])
#                 else:
#                     if visited[nx][ny] == -1:
#                         visited[nx][ny] = visited[x][y]
#                         queue.append([nx, ny, c])
#
#     return 0
#
# M, N = map(int, input().split())
# # -1 씩 해야함.
# d_x, d_y = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
#
# res = bfs()
#
# print(res)


# v3
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     visited = [[-1]*M for _ in range(N)]
#     visited[0][0] = 0
#     x, y = 0, 0
#     for c in range(4):
#         x += dx[c]
#         y += dy[c]
#         if 0 <= x < N and 0 <= y < M and arr[x][y] == 1:
#             queue.append([x, y, c])
#             visited[x][y] = 0
#
#     while queue:
#         x, y, direction = queue.popleft()
#
#         if x == d_x and y == d_y:
#             return visited[x][y]
#
#         for c in range(4):
#             nx = x + dx[c]
#             ny = y + dy[c]
#             if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
#                 if direction != c:
#                     if visited[nx][ny] == -1:
#                         visited[nx][ny] = visited[x][y] + 1
#                         queue.append([nx, ny, c])
#                     elif visited[nx][ny] >= visited[x][y] + 1:
#                         visited[nx][ny] = visited[x][y] + 1
#                         queue.append([nx, ny, c])
#                 else:
#                     if visited[nx][ny] == -1:
#                         visited[nx][ny] = visited[x][y]
#                         queue.append([nx, ny, c])
#                     # 방문 체크는 안 한 경우만 하고, 방향이 추후 어떻게 될지 모르니깐
#                     # 회전 안하고 지나갈 수 있다면 큐에 넣어줌.
#                     elif visited[nx][ny] >= visited[x][y]:
#                         visited[nx][ny] = visited[x][y]
#                         queue.append([nx, ny, c])
#
#     return 0
#
#
# M, N = map(int, input().split())
# d_x, d_y = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
#
# res = bfs()
#
# print(res)


# v4
from collections import deque


def bfs():
    queue = deque()
    visited = [[-1]*M for _ in range(N)]
    visited[0][0] = 0
    x, y = 0, 0
    for c in range(4):
        x += dx[c]
        y += dy[c]
        if 0 <= x < N and 0 <= y < M and arr[x][y] == 1:
            queue.append([x, y, c])
            visited[x][y] = 0

    while queue:
        x, y, direction = queue.popleft()

        if x == d_x and y == d_y:
            return visited[x][y]

        for c in range(4):
            nx = x + dx[c]
            ny = y + dy[c]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                if visited[nx][ny] == -1:
                    if direction != c:
                        visited[nx][ny] = visited[x][y] + 1
                    else:
                        visited[nx][ny] = visited[x][y]
                    queue.append([nx,ny,c])
                else:
                    # 방문 했던 곳
                    # 방향이 달라질 때
                    if direction != c:
                        if visited[nx][ny] >= visited[x][y] + 1:
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append([nx, ny, c])
                    # 방향이 같은 경우
                    else:
                        if visited[nx][ny] == visited[x][y]:
                            queue.append([nx, ny, c])

    return 0


M, N = map(int, input().split())
d_x, d_y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

res = bfs()

print(res)


