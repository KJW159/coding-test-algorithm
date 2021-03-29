# baekjoon_1987 알파벳

# v1
# R, C = map(int, input().split())
#
# board = [list(input()) for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# step = 1
# stack =[[0,0,[board[0][0]]]]
#
# while stack:
#     s_i, s_j, visited = stack.pop()
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < R and 0 <= y < C:
#             if board[x][y] not in visited:
#                 visited_tmp = visited[:]
#                 visited_tmp.append(board[x][y])
#                 stack.append([x,y,visited_tmp])
#                 if step < len(visited_tmp):
#                     step = len(visited_tmp)
# print(step)


# v2
# R, C = map(int, input().split())
#
# board = [list(input()) for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# step = 1
# visited = set()
# visited.add(board[0][0])
# stack =[[0,0,visited]]
#
# while stack:
#     s_i, s_j, visited = stack.pop()
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < R and 0 <= y < C:
#             if board[x][y] not in visited:
#                 visited_tmp = list(visited)
#                 visited_tmp.append(board[x][y])
#                 stack.append([x,y,set(visited_tmp)])
#                 if step < len(visited_tmp):
#                     step = len(visited_tmp)
# print(step)


#v3
# import collections
#
# R, C = map(int, input().split())
#
# board = [list(input()) for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# step = 1
# visited = collections.defaultdict(lambda:1)
# visited[board[0][0]] = 1
# stack =[[0,0,visited]]
#
# while stack:
#     s_i, s_j, visited = stack.pop()
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < R and 0 <= y < C:
#             if board[x][y] not in visited:
#                 visited_tmp = dict(visited)
#                 visited_tmp[board[x][y]] = 1
#                 stack.append([x,y,visited_tmp])
#                 if step < len(visited_tmp):
#                     step = len(visited_tmp)
# print(step)


# v4

# import collections
#
# R, C = map(int, input().split())
#
# board =[]
# visited = collections.defaultdict()
# for i in range(R):
#     chars = list(input())
#     board.append(chars)
#     for char in chars:
#         visited[char] = 0
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# step = 1
# visited[board[0][0]] = 1
# stack =[[0,0,visited]]
#
# while stack:
#     s_i, s_j, visited = stack.pop()
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < R and 0 <= y < C:
#             if visited[board[x][y]] == 0:
#                 step_tmp = 0
#                 visited_tmp = dict(visited)
#                 visited_tmp[board[x][y]] = 1
#                 stack.append([x,y,visited_tmp])
#                 for num in visited_tmp.values():
#                     step_tmp += num
#                 if step < step_tmp:
#                     step = step_tmp
# print(step)

# v5
#
# def dfs(s_i, s_j, step_tmp):
#     global step
#     step = max(step, step_tmp)
#
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#
#         if 0 <= x < R and 0 <= y < C:
#             if board[x][y] not in visited:
#                 visited.append(board[x][y])
#                 dfs(x, y, step_tmp+1)
#                 visited.remove(board[x][y])
#
# R, C = map(int, input().split())
#
# board = [list(input()) for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# step = 1
# visited = []
# visited.append(board[0][0])
# dfs(0,0,step)
# print(step)


# v6
# import collections, sys
# sys.setrecursionlimit(10000)
#
# def dfs(s_i, s_j, step_tmp):
#     global step
#     step = max(step, step_tmp)
#
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#
#         if 0 <= x < R and 0 <= y < C:
#             if board[x][y] not in visited.keys() or visited[board[x][y]] == 0:
#                 visited[board[x][y]] = 1
#                 dfs(x, y, step_tmp+1)
#                 visited[board[x][y]] = 0
#
# R, C = map(int, input().split())
#
# board = [list(sys.stdin.readline()) for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# step = 1
# visited = collections.defaultdict(int)
# visited[board[0][0]] = 1
# dfs(0,0,step)
# print(step)

# v7
# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(s_i, s_j, step_tmp):
#     global step
#     step = max(step, step_tmp)
#
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#
#         if 0 <= x < R and 0 <= y < C:
#             if board[x][y] not in visited:
#                 visited.add(board[x][y])
#                 dfs(x, y, step_tmp+1)
#                 visited.discard(board[x][y])
#
# R, C = map(int, input().split())
#
# board = [list(sys.stdin.readline()) for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# step = 1
# visited = set()
# visited.add(board[0][0])
# dfs(0,0,step)
# print(step)

# v8
# import sys
#
# def dfs():
#     global step
#     stack = [(0, 0, board[0][0])]
#     visited[0][0] = board[0][0]
#
#     while stack:
#         s_i, s_j, visited_tmp = stack.pop()
#         step = max(step, len(visited_tmp))
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 if not board[x][y] in visited_tmp:
#                     # if visited[x][y] != visited_tmp + board[x][y]:
#                     visited[x][y] = visited_tmp + board[x][y]
#                     stack.append((x,y, visited[x][y]))
#
# R, C = map(int, input().split())
#
# board = [list(sys.stdin.readline()) for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# step = 1
# visited = [['']*C for _ in range(R)]
# dfs()
# print(step)

# v9
import sys

def dfs():
    global step
    stack = [(0, 0, board[0][0])]
    visited[0][0] = board[0][0]

    while stack:
        s_i, s_j, visited_tmp = stack.pop()
        step = max(step, len(visited_tmp))
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < R and 0 <= y < C:
                if not board[x][y] in visited_tmp:
                    if visited[x][y] != visited_tmp + board[x][y]:
                        visited[x][y] = visited_tmp + board[x][y]
                        stack.append((x,y, visited[x][y]))

R, C = map(int, input().split())

board = [list(sys.stdin.readline()) for _ in range(R)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

step = 1
visited = [['']*C for _ in range(R)]
dfs()
print(step)