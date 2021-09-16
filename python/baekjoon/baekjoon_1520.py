# baekjoon_1520 내리막 길


# v1 시간초과 뜸.
# DP로 풀어야한다는 건 이미 알고 있었는데 뭘 알려줘야하지?
# 해당 좌표를 지나가면 몇가지 방식으로 도착할 수 있는지를 DP에 저장함.
# 도착점에 도착을 하면 지나왔던 곳을 return 하면서 DP의 해당 좌표에 +1을 함.
# 그럼 해당 DP가 0이면 v1대로 진행을 하고 DP가 0이 아니면 DP에 적혀진 숫자만큼 res에 더해주고 return함


# v1
# def dfs(s_i, s_j, height):
#     global res
#
#     if s_i == M-1 and s_j == N-1:
#         res += 1
#         return
#
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < M and 0 <= y < N:
#             if arr[x][y] < height and visited[x][y] == 0:
#                 visited[x][y] = 1
#                 dfs(x, y, arr[x][y])
#                 visited[x][y] = 0
#
#
# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(M)]
# visited = [[0]*N for _ in range(M)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = 0
#
#
# dfs(0,0,arr[0][0])
# print(res)


# v2
# import sys
#
# input = sys.stdin.readline
#
# def dfs(s_i, s_j):
#     global res
#
#     if s_i == M-1 and s_j == N-1:
#         res += 1
#         return 1
#     if dp[s_i][s_j] != 0:
#         res += dp[s_i][s_j]
#         return 0
#
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < M and 0 <= y < N:
#             if arr[x][y] < arr[s_i][s_j] and visited[x][y] == 0:
#                 visited[x][y] = 1
#                 dp[s_i][s_j] += dfs(x, y)
#                 visited[x][y] = 0
#     return 0
#
#
# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(M)]
# visited = [[0]*N for _ in range(M)]
# dp = [[0]*N for _ in range(M)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = 0
#
# dfs(0,0)
# print(res)


# v3
# import sys
#
# input = sys.stdin.readline
#
# def dfs(s_i, s_j):
#     global res
#     if s_i == M-1 and s_j == N-1:
#         res += 1
#         return 1
#     if dp[s_i][s_j] != 0:
#         res += dp[s_i][s_j]
#         return dp[s_i][s_j]
#
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < M and 0 <= y < N:
#             if arr[x][y] < arr[s_i][s_j] and visited[x][y] == 0:
#                 visited[x][y] = 1
#                 dp[s_i][s_j] += dfs(x, y)
#                 visited[x][y] = 0
#     return dp[s_i][s_j]
#
#
# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(M)]
# visited = [[0]*N for _ in range(M)]
# dp = [[0]*N for _ in range(M)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = 0
#
# dfs(0,0)
# print(res)


# v4
import sys

input = sys.stdin.readline

def dfs(s_i, s_j):

    if s_i == M-1 and s_j == N-1:
        return 1
    if dp[s_i][s_j] != -1:
        return dp[s_i][s_j]

    # -1이 한번도 방문하지 않은 좌표임. 따라서 방문 처리는 하기 위해서 0을 저장함.
    dp[s_i][s_j] = 0
    for c in range(4):
        x = s_i + dx[c]
        y = s_j + dy[c]
        if 0 <= x < M and 0 <= y < N:
            if arr[x][y] < arr[s_i][s_j]:
                dp[s_i][s_j] += dfs(x, y)
    return dp[s_i][s_j]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]
res = dfs(0,0)
print(res)