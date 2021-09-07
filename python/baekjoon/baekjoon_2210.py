# baekjoon_2210 숫자판 점프


# v1
from collections import defaultdict


def dfs(cnt, num, x, y):
    if cnt == 6:
        if visited[int(num)] == 0:
            visited[int(num)] = 1
        return
    for c in range(4):
        nx = x + dx[c]
        ny = y + dy[c]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(cnt+1, num+board[nx][ny],nx,ny)

dx = [0,-1,0,1]
dy = [-1,0,1,0]

board = [list(input().split()) for _ in range(5)]
visited = defaultdict(int)

for i in range(5):
    for j in range(5):
        dfs(1, board[i][j], i, j)


print(len(visited))