# baekjoon_2206 벽 부수고 이동하기
import sys
import collections

# v1
# def maze_bfs(N, M):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#
#     step = [0, False]
#     queue = collections.deque()
#     queue.append([0,0,0])
#     visited[0][0] = 1
#
#     while queue:
#         i, j, brick = queue.popleft()
#         if i == N-1 and j == M-1:
#             step[0] = visited[i][j]
#             step[1] = True
#             break
#
#         for c in range(4):
#             x = i + dx[c]
#             y = j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if arr[x][y] == 0 and visited[x][y] == 0:
#                     queue.append([x,y,brick])
#                     visited[x][y] = visited[i][j] + 1
#                 if arr[x][y] == 1 and visited[x][y] == 0 and brick == 0:
#                     brick_tmp = 1
#                     queue.append([x,y,brick_tmp])
#                     visited[x][y] = visited[i][j] + 1
#     return step
#
# N, M = list(map(int, input().split()))
#
# arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
#
# res = maze_bfs(N, M)
#
# if res[1]:
#     print(res[0])
# else:
#     print(-1)



# v2
def maze_bfs(N, M):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    step = [0, False]
    queue = collections.deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1
    visited[1][0][0] = 1

    while queue:
        i, j, brick = queue.popleft()
        if i == N-1 and j == M-1:
            if brick == 1:
                step[0] = visited[1][i][j]
            if brick == 0:
                step[0] = visited[0][i][j]
            step[1] = True
            break

        for c in range(4):
            x = i + dx[c]
            y = j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == 0 and brick == 0 and visited[0][x][y] == 0:
                    queue.append([x, y, brick])
                    visited[0][x][y] = visited[0][i][j] + 1

                elif arr[x][y] == 0 and brick == 1 and visited[1][x][y] == 0:
                    queue.append([x, y, brick])
                    visited[1][x][y] = visited[1][i][j] + 1

                if arr[x][y] == 1 and brick == 0 and visited[0][x][y] == 0:
                    queue.append([x, y, 1])
                    visited[1][x][y] = visited[0][i][j] + 1
    return step



N, M = list(map(int, input().split()))

arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for __ in range(2)]

res = maze_bfs(N, M)

if res[1]:
    print(res[0])
else:
    print(-1)
