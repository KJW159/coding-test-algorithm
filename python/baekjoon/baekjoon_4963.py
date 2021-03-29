# baekjoon_4963 섬의 개수
import sys

def dfs(i,j):
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    stack = []
    stack.append([i,j])
    visited[i][j] = 1

    while stack:
        i_x, j_y = stack.pop()
        for c in range(8):
            x = i_x + dx[c]
            y = j_y + dy[c]
            if 0 <= x < h and 0 <= y < w:
                if lands[x][y] == 1 and visited[x][y] == 0:
                    stack.append([x, y])
                    visited[x][y] = 1

while True:
    w, h = list(map(int, sys.stdin.readline().split()))
    if w == 0 and h == 0:
        break
    lands = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for __ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if lands[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)