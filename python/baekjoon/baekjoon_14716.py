# baekjoon_14716 현수막

# v1
from collections import deque
import sys

input = sys.stdin.readline

def bfs(s_i, s_j):
    queue = deque()
    queue.append([s_i, s_j])
    visited[s_i][s_j] = 1

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(8):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < M and 0 <= y < N:
                if visited[x][y] == 0 and banners[x][y] == 1:
                    queue.append([x, y])
                    visited[x][y] = 1


M, N = map(int, input().split())
banners = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
res = 0

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

for i in range(M):
    for j in range(N):
        if banners[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j)
            res += 1
print(res)