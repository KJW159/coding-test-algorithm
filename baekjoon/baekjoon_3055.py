# baekjoon_3055 탈출
import collections

def bfs():
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    queue = collections.deque(water)
    queue.append(start)
    visited[start[0]][start[1]] = 1
    res_tmp = 0

    while queue:
        i_x, j_y, k_type = queue.popleft()

        for c in range(4):
            x = i_x + dx[c]
            y = j_y + dy[c]
            if 0 <= x < R and 0 <= y < C:
                if arr[x][y] == '.' and visited[x][y] == 0:
                    if k_type == '*':
                        arr[x][y] = '*'
                        queue.append([x, y, '*'])
                        visited[x][y] = 1
                    elif k_type == 'S':
                        queue.append([x,y,'S'])
                        visited[x][y] = visited[i_x][j_y] + 1
                if arr[x][y] == 'D' and k_type == 'S':
                    visited[x][y] = visited[i_x][j_y] + 1
                    res_tmp = 1
                    return res_tmp

    return res_tmp


R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
visited = [[0]*C for __ in range(R)]
water = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            water.append([i, j, '*'])
        if arr[i][j] == 'S':
            start = [i, j, 'S']
        if arr[i][j] == 'D':
            end_point = [i, j]

res = bfs()

if res == 0:
    print("KAKTUS")
elif res == 1:
    print(visited[end_point[0]][end_point[1]]-1)