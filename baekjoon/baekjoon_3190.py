# baekjoon_3190 뱀

# v1
# from collections import deque
#
# def moving_snake(s_i, s_j):
#     stack = []
#     stack.append([s_i, s_j])
#     curr_dir = 2
#     moving_time = 0
#     tail = deque()
#     tail.append([0,0])
#
#     while stack:
#         s_i, s_j = stack.pop()
#         if changes[moving_time]:
#             direction = changes[moving_time]
#             if direction == 'D':
#                 curr_dir = (curr_dir + 1) % 4
#             if direction == 'L':
#                 curr_dir = (curr_dir - 1) % 4
#         x = s_i + dx[curr_dir]
#         y = s_j + dy[curr_dir]
#         if 0 <= x < N and 0 <= y < N:
#             if board[x][y] == 1:
#                 moving_time += 1
#                 break
#             if board[x][y] == 2:
#                 board[x][y] = 1
#                 stack.append([x,y])
#                 tail.append([x,y])
#                 moving_time += 1
#             if board[x][y] == 0:
#                 t_i, t_j = tail.popleft()
#                 board[t_i][t_j] = 0
#                 board[x][y] = 1
#                 stack.append([x,y])
#                 tail.append([x,y])
#                 moving_time += 1
#         else:
#             moving_time += 1
#             break
#     return moving_time
#
#
# N = int(input())
# board = [[0]*N for _ in range(N)]
#
# K = int(input())
# # 사과 2, 뱀,1
# for _ in range(K):
#     a_i, a_j = map(int, input().split())
#     board[a_i-1][a_j-1] = 2
# L = int(input())
# changes = [False]*10001
# for _ in range(L):
#     idx, direction = input().split()
#     changes[int(idx)] = direction
# # 좌, 상, 우, 하
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# res = moving_snake(0,0)
# print(res)


# v2
from collections import deque


def moving_snake(s_i, s_j):
    stack = []
    stack.append([s_i, s_j])
    curr_dir = 2
    moving_time = 0
    tail = deque()
    tail.append([0,0])

    while stack:
        s_i, s_j = stack.pop()
        if changes[moving_time]:
            direction = changes[moving_time]
            if direction == 'D':
                curr_dir = (curr_dir + 1) % 4
            if direction == 'L':
                curr_dir = (curr_dir - 1) % 4
        x = s_i + dx[curr_dir]
        y = s_j + dy[curr_dir]
        moving_time += 1
        if 0 <= x < N and 0 <= y < N:
            if board[x][y] == 1:
                break
            if board[x][y] == 2:
                board[x][y] = 1
                stack.append([x,y])
                tail.append([x,y])
            if board[x][y] == 0:
                t_i, t_j = tail.popleft()
                board[t_i][t_j] = 0
                board[x][y] = 1
                stack.append([x,y])
                tail.append([x,y])
        else:
            break
    return moving_time


N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())
# 사과 2, 뱀,1
for _ in range(K):
    a_i, a_j = map(int, input().split())
    board[a_i-1][a_j-1] = 2
L = int(input())
changes = [False]*10001
for _ in range(L):
    idx, direction = input().split()
    changes[int(idx)] = direction
# 좌, 상, 우, 하
dx = [0,-1,0,1]
dy = [-1,0,1,0]

res = moving_snake(0,0)
print(res)