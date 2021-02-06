# baekjoon_1926 그림

# v1
# import sys
# limit_number = 2500000
# sys.setrecursionlimit(limit_number)
# def dfs(s_i, s_j):
#     global paint_area
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#
#     paint_area = max(paint_area, visited[s_i][s_j])
#
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < N and 0 <= y < M:
#             if visited[x][y] == -1 and arr[x][y] == 1:
#                 visited[x][y] = visited[s_i][s_j] + 1
#                 dfs(x, y)
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[-1]*(M) for _ in range(N)]
# paint_cnt = 0
# paint_area = 0
# for i in range(N):
#     for j in range(M):
#         if visited[i][j] == -1 and arr[i][j] == 1:
#             visited[i][j] = 1
#             dfs(i,j)
#             paint_cnt += 1
# print(paint_cnt)
# print(paint_area)

# v2

# def dfs(s_i, s_j, cnt_tmp):
#     global paint_area
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#
#     paint_area = max(paint_area, cnt_tmp)
#
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < N and 0 <= y < M:
#             if visited[x][y] == 0 and arr[x][y] == 1:
#                 visited[x][y] = 1
#                 cnt_tmp += 1
#                 dfs(x, y, cnt_tmp)
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*(M) for _ in range(N)]
# paint_cnt = 0
# paint_area = 0
# for i in range(N):
#     for j in range(M):
#         if visited[i][j] == 0 and arr[i][j] == 1:
#             visited[i][j] = 1
#             cnt_tmp = 1
#             dfs(i, j, cnt_tmp)
#             paint_cnt += 1
# print(paint_cnt)
# print(paint_area)


# v3

def dfs(s_i, s_j):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    cnt_tmp = 1
    stack = []
    stack.append([s_i, s_j])

    while stack:
        s_i, s_j = stack.pop()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if visited[x][y] == 0 and arr[x][y] == 1:
                    visited[x][y] = 1
                    cnt_tmp += 1
                    stack.append([x,y])
    return cnt_tmp


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)]
paint_cnt = 0
paint_area = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j] == 1:
            visited[i][j] = 1
            cnt_tmp = dfs(i, j)
            paint_cnt += 1
            paint_area = max(paint_area, cnt_tmp)
print(paint_cnt)
print(paint_area)
