# baekjoon_1937 욕심쟁이 판다

# v1
# def dfs(s_i, s_j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     stack = []
#     stack.append([s_i, s_j])
#     visited[s_i][s_j] = 1
#     days = 1
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if visited[x][y] == -1 and forest[x][y] > forest[s_i][s_j]:
#                     stack.append([x, y])
#                     visited[x][y] = 1
#                     days += 1
#                     break
#     return days
#
#
# N = int(input())
# forest = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# for i in range(N):
#     for j in range(N):
#         visited = [[-1] * N for _ in range(N)]
#         res = max(res, dfs(i,j))
# print(res)

# v2
# def dfs(s_i, s_j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     stack = []
#     stack.append([s_i, s_j])
#     visited[s_i][s_j] = 1
#     days = 0
#
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if forest[x][y] > forest[s_i][s_j]:
#                     stack.append([x, y])
#                     visited[x][y] = max(visited[x][y], visited[s_i][s_j]+1)
#                     days = max(days, visited[x][y])
#     return days
#
#
# N = int(input())
# forest = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# visited = [[-1] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         res = max(res, dfs(i,j))
# print(res)

# v3
# def dfs(s_i, s_j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     stack = []
#     stack.append([s_i, s_j])
#     visited[s_i][s_j] = 1
#     days = 0
#
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and forest[x][y] > forest[s_i][s_j]:
#                 if visited[x][y] < visited[s_i][s_j]+1:
#                     stack.append([x, y])
#                     # visited[x][y] = max(visited[x][y], visited[s_i][s_j]+1)
#                     visited[x][y] = visited[s_i][s_j] + 1
#                     days = max(days, visited[x][y])
#     return days
#
#
# N = int(input())
# forest = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# visited = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         res = max(res, dfs(i,j))
# print(res)

# v4

# def dfs(s_i, s_j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     stack = []
#     stack.append([s_i, s_j, 1])
#     visited[s_i][s_j] = 1
#     days = 0
#
#     while stack:
#         s_i, s_j, visited_tmp = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and forest[x][y] > forest[s_i][s_j]:
#                 if visited[x][y] != 0:
#                     # if visited[x][y] == visited[s_i][s_j]:
#                     #     visited[s_i][s_j] = visited[x][y]+1
#                     # else:
#                         visited[s_i][s_j] = max(visited_tmp, visited[s_i][s_j])
#                         days = max(days, visited[s_i][s_j])
#                 if visited[x][y] == 0:
#                     stack.append([x, y, visited_tmp+1])
#                     visited[x][y] = 1
#     return days
#
#
# N = int(input())
# forest = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# visited = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         res = max(res, dfs(i,j))
# print(res)


# v5
# def dfs(s_i, s_j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     stack = []
#     stack.append([s_i, s_j, 1])
#     visited[s_i][s_j] = 1
#     days = 0
#
#     while stack:
#         s_i, s_j, visited_tmp = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and forest[x][y] > forest[s_i][s_j]:
#                 visited[s_i][s_j] = max(visited_tmp, visited[s_i][s_j])
#                 days = max(days, visited_tmp)
#                 stack.append([x, y, visited_tmp+1])
#                 visited[x][y] = 1
#     return days
#
#
# N = int(input())
# forest = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# visited = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         res = max(res, dfs(i,j))
# print(res)

# v6
import sys
limit_number = 250001
sys.setrecursionlimit(limit_number)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(s_i, s_j):
    if visited[s_i][s_j]:
        return visited[s_i][s_j]
    visited[s_i][s_j] = 1
    for c in range(4):
        x = s_i + dx[c]
        y = s_j + dy[c]
        if 0 <= x < N and 0 <= y < N:
            if forest[x][y] > forest[s_i][s_j]:
                visited[s_i][s_j] = max(visited[s_i][s_j], dfs(x,y)+1 )
    return visited[s_i][s_j]


N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
res = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        res = max(res, dfs(i,j))
print(res)