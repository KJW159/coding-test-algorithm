# baekjoon_2178 미로탐색

import collections

def bfs(N,M):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    queue = collections.deque()
    queue.append([0,0])
    visited[0][0] = 1
    while queue:
        cord = queue.popleft()
        if cord[0] == N-1 and cord[1] == M-1:
            return visited[cord[0]][cord[1]]

        for c in range(4):
            x = cord[0] + dx[c]
            y = cord[1] + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == 1 and visited[x][y] == 0:
                    queue.append([x,y])
                    visited[x][y] = visited[cord[0]][cord[1]] + 1

N, M = list(map(int, input().split()))
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
distance_min = bfs(N,M)
print('{}'.format(distance_min))