# baekjoon_1012 유기농 배추

def dfs(i,j):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    cnt = 1

    stack = []
    stack.append([i,j])
    visited[i][j] = 1

    while stack:
        cabbage = stack.pop()
        for c in range(4):
            x = cabbage[0]+dx[c]
            y = cabbage[1]+dy[c]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == 1 and visited[x][y] == 0:
                    stack.append([x, y])
                    visited[x][y] = 1
                    cnt += 1
                else:
                    visited[x][y] = 1
    return cnt


T = int(input())

for tc in range(T):
    M, N, K = list(map(int, input().split()))
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    worms = 0
    for n in range(K):
        j, i = list(map(int, input().split()))
        arr[i][j] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                cabb_num = dfs(i,j)
                if cabb_num >= 1:
                    worms += 1
            else:
                visited[i][j] = 1
    print('{}'.format(worms))

