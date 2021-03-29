# baekjoon_7569 토마토

import collections


def tomato_bfs():
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    dz = [-1, 1]

    queue = collections.deque(start_point)
    while queue:
        k_z, i_x, j_y = queue.popleft()

        # 위층, 아래층
        for c2 in range(2):
            z = k_z + dz[c2]
            if 0 <= z < H:
                if arr[z][i_x][j_y] == 0:
                    arr[z][i_x][j_y] = arr[k_z][i_x][j_y] + 1
                    queue.append([z, i_x, j_y])

        # 2차원에서 상하좌우
        for c1 in range(4):
            x = i_x + dx[c1]
            y = j_y + dy[c1]
            if 0 <= x < N and 0 <= y < M:
                if arr[k_z][x][y] == 0:
                    arr[k_z][x][y] = arr[k_z][i_x][j_y] + 1
                    queue.append([k_z, x, y])


M, N, H = list(map(int, input().split()))

arr = [[list(map(int, input().split())) for _ in range(N)] for h in range(H)]
start_point = []
res = True
date = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                start_point.append([k, i, j])

tomato_bfs()
trg = False
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                res = False
                trg = True
                break
            if arr[k][i][j] > date:
                date = arr[k][i][j]
    if trg:
        break
if res:
    print(date-1)
else:
    print(-1)




