# baekjoon_1743 음식물 피하기

# v1
from collections import deque

def bfs(s_i, s_j):
    queue = deque()
    queue.append([s_i, s_j])
    visited[s_i][s_j] = 1
    cnt = 1

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if visited[x][y] == 0 and arr[x][y] == 1:
                    queue.append([x, y])
                    visited[x][y] = 1
                    cnt += 1
    return cnt


N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
res = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j] == 1:
            res = max(res, bfs(i, j))
print(res)