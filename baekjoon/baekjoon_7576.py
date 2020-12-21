# baekjoon_7576 토마토
import collections

def bfs():
    pass

M, N = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

queue = collections.deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i,j])
            visited[i][j] = 1

if len(queue) == 0:
    result = -1
else:
    bfs(queue)

