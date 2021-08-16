# baekjoon_14442 벽 부수고 이동하기 2

# v1
# from collections import deque
#
# def bfs():
#     queue = deque()
#     queue.append([0,0])
#     visited[0][0][0] = 1
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if world[x][y] == 0 and visited[x][y][0] == 0:
#                     queue.append([x, y])
#                     visited[x][y][0] = visited[s_i][s_j][0] + 1
#                     visited[x][y][1] = visited[s_i][s_j][1]
#                     if x == N-1 and y == M-1:
#                         return visited[x][y][0]
#                 if world[x][y] == 1 and visited[x][y][0] == 0:
#                     if visited[s_i][s_j][1] + 1 <= K:
#                         queue.append([x, y])
#                         visited[x][y][0] = visited[s_i][s_j][0] + 1
#                         visited[x][y][1] = visited[s_i][s_j][1] + 1
#
#     return -1
#
# N, M, K = map(int, input().split())
# world = [list(map(int, input())) for _ in range(N)]
# # 이동횟수, 벽 부순 횟수
# visited = [[[0, 0] for __ in range(M)] for _ in range(N)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# res = bfs()
# print(visited)
# print(res)


# v2
# from collections import deque
# import math
#
#
# def bfs():
#     queue = deque()
#     queue.append([0,0])
#     visited[0][0][0] = 1
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if world[x][y] == 0:
#                     if visited[s_i][s_j][1] < visited[x][y][1]:
#                         queue.append([x, y])
#                         visited[x][y][0] = visited[s_i][s_j][0] + 1
#                         visited[x][y][1] = visited[s_i][s_j][1]
#                     if x == N-1 and y == M-1:
#                         return visited[x][y][0]
#                 if world[x][y] == 1 and visited[s_i][s_j][1] + 1 <= K:
#                     queue.append([x, y])
#                     visited[x][y][0] = visited[s_i][s_j][0] + 1
#                     visited[x][y][1] = visited[s_i][s_j][1] + 1
#     return -1
#
# N, M, K = map(int, input().split())
# world = [list(map(int, input())) for _ in range(N)]
# INF = math.inf
# # 이동횟수, 벽 부순 횟수
# visited = [[[0, INF] for __ in range(M)] for _ in range(N)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# res = bfs()
# print(res)


# v3
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     queue.append([0, 0, 0])
#     visited[0][0][0] = 1
#
#     while queue:
#         s_i, s_j, cnt = queue.popleft()
#         if s_i == N - 1 and s_j == M - 1:
#             return visited[s_i][s_j][cnt]
#
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if world[x][y] == 0 and visited[x][y][cnt] == 0:
#                     queue.append([x, y, cnt])
#                     visited[x][y][cnt] = visited[s_i][s_j][cnt] + 1
#
#                 if world[x][y] == 1 and cnt+1 <= K:
#                     queue.append([x, y, cnt+1])
#                     visited[x][y][cnt+1] = visited[s_i][s_j][cnt] + 1
#     return -1
#
#
# N, M, K = map(int, input().split())
# world = [list(map(int, input())) for _ in range(N)]
# visited = [[[0]*(K+1) for __ in range(M)] for _ in range(N)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# res = bfs()
# print(res)


# v4
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     queue.append([0, 0, 0])
#     visited[0][0][0] = 1
#
#     while queue:
#         s_i, s_j, cnt = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if world[x][y] == 0 and visited[x][y][cnt] == 0:
#                     queue.append([x, y, cnt])
#                     visited[x][y][cnt] = visited[s_i][s_j][cnt] + 1
#                     if x == N - 1 and y == M - 1:
#                         return visited[x][y][cnt]
#
#                 if world[x][y] == 1 and cnt+1 <= K:
#                     queue.append([x, y, cnt+1])
#                     visited[x][y][cnt+1] = visited[s_i][s_j][cnt] + 1
#     return -1
#
#
# N, M, K = map(int, input().split())
# world = [list(map(int, input())) for _ in range(N)]
# visited = [[[0]*(K+1) for __ in range(M)] for _ in range(N)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# res = bfs()
# print(res)


# v5
from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1

    while queue:
        s_i, s_j, cnt = queue.popleft()
        if s_i == N - 1 and s_j == M - 1:
            return visited[s_i][s_j][cnt]

        moving_cnt = visited[s_i][s_j][cnt] + 1
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if world[x][y] == 0 and visited[x][y][cnt] == 0:
                    queue.append([x, y, cnt])
                    visited[x][y][cnt] = moving_cnt

                if world[x][y] == 1 and cnt+1 <= K and visited[x][y][cnt+1] == 0 :
                    queue.append([x, y, cnt+1])
                    visited[x][y][cnt+1] = moving_cnt
    return -1


N, M, K = map(int, input().split())
world = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*(K+1) for __ in range(M)] for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

res = bfs()
print(res)