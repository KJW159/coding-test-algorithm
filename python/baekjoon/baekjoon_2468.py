# baekjoon_2468 안전 영역
import sys

def dfs(s_i, s_j, rain):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    stack = []
    stack.append([s_i, s_j])
    visited[s_i][s_j] = 1

    while stack:
        s_i, s_j = stack.pop()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < N:
                if visited[x][y] == 0 and arr[x][y] > rain:
                    stack.append([x,y])
                    visited[x][y] = 1


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

rain_min = 101
rain_max = 0
safe_area = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] > rain_max:
            rain_max = arr[i][j]
        if arr[i][j] < rain_min:
            rain_min = arr[i][j]

for rain in range(rain_min, rain_max+1):
    visited = [[0]*N for __ in range(N)]
    area_tmp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] > rain:
                dfs(i,j, rain)
                area_tmp += 1
    safe_area = max(safe_area, area_tmp)

print(safe_area)