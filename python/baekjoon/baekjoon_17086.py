# baekjoon_17086 아기 상어2


# v1
# from collections import deque
#
# def finding_safety(i,j):
#     visited = [[-1]*M for _ in range(N)]
#     visited[i][j] = 0
#     queue = deque()
#     queue.append([i,j])
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(8):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M and visited[x][y] == -1:
#                 visited[x][y] = visited[s_i][s_j] + 1
#                 if arr[x][y] == 0:
#                     queue.append([x,y])
#                 if arr[x][y] == 1:
#                     return visited[x][y]
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# res = 0
#
# dx = [0,-1,-1,-1,0,1,1,1]
# dy = [-1,-1,0,1,1,1,0,-1]
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             res = max(res, finding_safety(i,j))
#
# print(res)


# v2
from collections import deque

def finding_safety(sharks):
    queue = deque()
    for shark in sharks:
        queue.append(shark)
        visited[shark[0]][shark[1]] = 0

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(8):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == 0:
                    if visited[x][y] == -1:
                        queue.append([x, y])
                        visited[x][y] = visited[s_i][s_j] + 1
                    if visited[x][y] != -1:
                        visited[x][y] = min(visited[s_i][s_j]+1, visited[x][y])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
sharks = []
visited = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            sharks.append([i, j])
finding_safety(sharks)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            res = max(visited[i][j], res)

print(res)