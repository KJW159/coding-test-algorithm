# baekjoon_2636 치즈
import collections

def bfs(s_i, s_j):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    queue = collections.deque()
    queue.append([s_i, s_j])
    visited[s_i][s_j] = 1
    cheeze_cnt_tmp = 0
    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == 0 and visited[x][y] == 0:
                    queue.append([x,y])
                    visited[x][y] = 1
                if arr[x][y] == 1 and visited[x][y] == 0:
                    cheeze_cnt_tmp += 1
                    arr[x][y] = 0
                    visited[x][y] = 1

    return cheeze_cnt_tmp



N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

hours = 0
cheeze_cnt = 0

while True:
    visited = [[0]*M for __ in range(N)]
    tmp = bfs(0,0)
    if tmp > 0:
        cheeze_cnt = tmp
        hours += 1
    elif tmp == 0:
        break
print("{}\n{}".format(hours, cheeze_cnt))