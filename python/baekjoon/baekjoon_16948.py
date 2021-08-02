# baekjoon_16948 데스 나이트

# v1
from collections import deque

def bfs():
    while queue:
        i, j = queue.popleft()
        if i == r2 and j == c2:
            return visited[i][j]
        for c in range(6):
            x = i + dx[c]
            y = j + dy[c]
            if 0 <= x < N and 0 <= y < N:
                if visited[x][y] == -1:
                    queue.append([x,y])
                    visited[x][y] = visited[i][j] + 1
    return -1


N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

queue = deque()
queue.append([r1, c1])
visited = [[-1]*N for _ in range(N)]
visited[r1][c1] = 0

res = bfs()

print(res)
