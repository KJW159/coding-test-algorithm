# baekjoon_2665 미로만들기

# v1
# from itertools import combinations
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     queue.append([0,0])
#     board_copy[0][0] = 2
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         if s_i == N-1 and s_j == N-2:
#             return 1
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if board_copy[x][y] == 1:
#                     queue.append([x, y])
#                     board_copy[x][y] = 2
#     return 0
#
#
# N = int(input())
# board = [list(map(int, input())) for _ in range(N)]
# black_rooms = []
# black_rooms_cnt = 0
# trg = False
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = 0
#
# for i in range(N):
#     for j in range(N):
#         if board[i][j] == 0:
#             black_rooms.append([i,j])
#             black_rooms_cnt += 1
#
# for i in range(black_rooms_cnt+1):
#     if trg:
#         break
#     for black_to_white in combinations(black_rooms, i):
#         board_copy = [board[k][:] for k in range(N)]
#         for b_x, b_y in black_to_white:
#             board_copy[b_x][b_y] = 1
#         if bfs():
#             trg = True
#             res = i
#             break
# print(res)

# v2
# from itertools import combinations
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     queue.append([0,0])
#     board_copy[0][0] = 2
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         if s_i == N-1 and s_j == N-1:
#             return 1
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if board_copy[x][y] == 1:
#                     queue.append([x, y])
#                     board_copy[x][y] = 2
#     return 0
#
#
# N = int(input())
# board = [list(map(int, input())) for _ in range(N)]
# black_rooms = []
# black_rooms_cnt = 0
# trg = False
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = 0
#
# for i in range(N):
#     for j in range(N):
#         if board[i][j] == 0:
#             black_rooms.append([i,j])
#             black_rooms_cnt += 1
#
# for i in range(black_rooms_cnt+1):
#     if trg:
#         break
#     for black_to_white in combinations(black_rooms, i):
#         board_copy = [board[k][:] for k in range(N)]
#         for b_x, b_y in black_to_white:
#             board_copy[b_x][b_y] = 1
#         if bfs():
#             trg = True
#             res = i
#             break
# print(res)

# v3
# import math
# from collections import deque
#
# def bfs():
#     queue = deque()
#     queue.append([0,0,0])
#     res_tmp = INF
#     while queue:
#         s_i, s_j, black_cnt = queue.popleft()
#         if s_i == N-1 and s_j == N-1:
#             if res_tmp > black_cnt:
#                 res_tmp = black_cnt
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if board[x][y] == 0 and visited[x][y] > black_cnt+1:
#                     queue.append([x,y,black_cnt+1])
#                     visited[x][y] = black_cnt + 1
#                 if board[x][y] == 1 and visited[x][y] > black_cnt:
#                     queue.append([x,y,black_cnt])
#                     visited[x][y] = black_cnt
#     return res_tmp
#
#
# N = int(input())
# board = [list(map(int, input())) for _ in range(N)]
# INF = math.inf
# visited = [[INF]*N for _ in range(N)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
#
# res = bfs()
# print(res)

# v4
import math
from collections import deque

def bfs():
    queue = deque()
    queue.append([0,0,0])
    while queue:
        s_i, s_j, black_cnt = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < N:
                if board[x][y] == 0 and visited[x][y] > black_cnt+1:
                    queue.append([x,y,black_cnt+1])
                    visited[x][y] = black_cnt + 1
                if board[x][y] == 1 and visited[x][y] > black_cnt:
                    queue.append([x,y,black_cnt])
                    visited[x][y] = black_cnt


N = int(input())
board = [list(map(int, input())) for _ in range(N)]
INF = math.inf
visited = [[INF]*N for _ in range(N)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]

bfs()
res = visited[N-1][N-1]
print(res)