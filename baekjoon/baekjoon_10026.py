# baekjoon_10026 적록 색약
import sys
import collections


def bfs_nc(i, j):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]


    queue_nc = collections.deque()
    queue_nc.append([i, j])
    visited_nc[i][j] = 1

    while queue_nc:
        c_i, c_j = queue_nc.popleft()
        for c in range(4):
            x = c_i + dx[c]
            y = c_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if pic[c_i][c_j] == pic[x][y] and visited_nc[x][y] == 0:
                    queue_nc.append([x, y])
                    visited_nc[x][y] = 1


def bfs_c(i, j):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]


    queue_c = collections.deque()
    queue_c.append([i, j])
    visited_c[i][j] = 1

    while queue_c:
        c_i, c_j = queue_c.popleft()
        for c in range(4):
            x = c_i + dx[c]
            y = c_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if pic[c_i][c_j] == 'B':
                    if pic[c_i][c_j] == pic[x][y] and visited_c[x][y] == 0:
                        queue_c.append([x, y])
                        visited_c[x][y] = 1
                else:
                    if pic[x][y] == 'R' or pic[x][y] == 'G':
                        if visited_c[x][y] == 0:
                            queue_c.append([x,y])
                            visited_c[x][y] = 1


N = int(input())
pic = [list(sys.stdin.readline().strip()) for _ in range(N)]
M = len(pic[0])
visited_nc = [[0]*M for __ in range(N)]
visited_c = [[0]*M for ___ in range(N)]
no_colorblind = 0
colorblind = 0

for i in range(N):
    for j in range(M):
        if visited_nc[i][j] == 0:
            bfs_nc(i,j)
            no_colorblind += 1
        if visited_c[i][j] == 0:
            bfs_c(i,j)
            colorblind += 1
print("{} {}".format(no_colorblind, colorblind))