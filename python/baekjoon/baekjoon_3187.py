# baekjoon_3187 양치기 꿍


# v1
from collections import deque


def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1
    wolf_num_tmp = 0
    sheep_num_tmp = 0
    if corral[i][j] == 'v':
        wolf_num_tmp = 1
    elif corral[i][j] == 'k':
        sheep_num_tmp = 1


    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M and visited[x][y] == 0:
                if corral[x][y] == '.':
                    queue.append([x,y])
                    visited[x][y] = 1
                elif corral[x][y] == 'v':
                    queue.append([x,y])
                    visited[x][y] = 1
                    wolf_num_tmp += 1
                elif corral[x][y] == 'k':
                    queue.append([x,y])
                    visited[x][y] = 1
                    sheep_num_tmp += 1
    if wolf_num_tmp >= sheep_num_tmp:
        animal_num[0] -= sheep_num_tmp
    else:
        animal_num[1] -= wolf_num_tmp


N, M = map(int, input().split())
# 양, 늑대
animal_num = [0,0]
corral = []
visited = [[0]*M for _ in range(N)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]

for _ in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j] == 'v':
            animal_num[1] += 1
        if tmp[j] == 'k':
            animal_num[0] += 1
    corral.append(tmp)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and corral[i][j] != '#':
            bfs(i,j)

print(*animal_num)