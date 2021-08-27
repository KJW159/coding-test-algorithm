# baekjoon_14940 쉬운 최단거리


# v1
from collections import deque


def bfs(start_point):
    queue = deque()
    s_i, s_j = start_point
    queue.append([s_i, s_j])
    visited[s_i][s_j] = 0

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if visited[x][y] == -1 and land[x][y] == 1:
                    queue.append([x,y])
                    visited[x][y] = visited[s_i][s_j] + 1


N, M = map(int, input().split())
visited = [[-1]*M for _ in range(N)]
start_point = []
land = []
for i in range(N):
    tmp = list(map(int, input().split()))
    land.append(tmp)
    for j in range(M):
        if tmp[j] == 2:
            start_point = [i,j]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

bfs(start_point)


for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and land[i][j] == 1:
            visited[i][j] = -1
        if land[i][j] == 0:
            visited[i][j] = 0

for i in range(N):
    print(*visited[i])