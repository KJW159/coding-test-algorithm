# algo_1223_동빈나
import collections

def bfs(start):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    queue.append(start)
    i,j = start
    visited[i][j] = 1

    while queue:
        node = queue.popleft()
        if node[0] == N-1 and node[1] == M-1:
            return visited[node[0]][node[1]]

        for c in range(4):
            x = node[0]+dx[c]
            y = node[1]+dy[c]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == 1 and visited[x][y] == 0:
                    queue.append([x,y])
                    visited[x][y] = visited[node[0]][node[1]] +1


N, M = list(map(int, input().split()))

arr = [list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
queue = collections.deque()
start = [0,0]
min_dis = bfs(start)
print('{}'.format(min_dis))




