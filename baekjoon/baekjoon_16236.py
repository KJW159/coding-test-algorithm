# baekjoon_16236 아기 상어
import collections

def bfs(s_i, s_j, shark_size):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    visited = [[0]*N for __ in range(N)]
    queue = collections.deque()
    queue.append([s_i, s_j])
    visited[s_i][s_j] = 1
    eating = []
    finding_mom = False

    while queue:
        s_i, s_j = queue.popleft()

        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < N:
                if visited[x][y] == 0:
                    if arr[x][y] == shark_size or arr[x][y] == 0:
                        queue.append([x,y])
                        visited[x][y] = visited[s_i][s_j] + 1
                    if 0 < arr[x][y] < shark_size:
                        visited[x][y] = visited[s_i][s_j] + 1
                        eating.append([x, y, visited[x][y]-1])

    if len(eating) == 0:
        finding_mom = True
        tmp =[0,0,0]
    else:
        # 조건에 따른 먹을 수 있는 물고기 정렬
        eating.sort(key= lambda x: (x[2], x[0], x[1]))
        # 1마리만 먹음
        tmp = [eating[0][0], eating[0][1], eating[0][2]]
    return (tmp, finding_mom)



N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start = [i, j]
            arr[i][j] = 0

shark_size = 2
time = 0
cnt = 0
while True:
    # bfs로 이동시 물고기 먹었던 위치로 가고 visited 초기화
    fish, mom = bfs(start[0], start[1], shark_size)
    if mom == True:
        break
    else:
        cnt += 1
        time += fish[2]
        if cnt == shark_size:
            shark_size += 1
            cnt = 0

        start = [fish[0], fish[1]]
        arr[fish[0]][fish[1]] = 0
print(time)

