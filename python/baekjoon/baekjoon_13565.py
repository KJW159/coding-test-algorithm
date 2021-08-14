# baekjoon_13565 침투

# 1
from collections import deque

def bfs(start_point):
    queue = deque()

    for start in start_point:
        queue.append(start)
        visited[start[0]][start[1]] = 1

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < M and 0 <= y < N:
                if visited[x][y] == 0 and arr[x][y] == 0:
                    queue.append([x, y])
                    visited[x][y] = 1
                    if x == M-1:
                        return True
    return False


M, N = map(int, input().split())

arr = [list(map(int, input())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]


start_point = []
for i in range(N):
    if arr[0][i] == 0:
        start_point.append([0, i])

res = bfs(start_point)
if res:
    print("YES")
else:
    print("NO")