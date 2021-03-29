import collections

def bfs(u, v):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    queue = collections.deque()
    queue.append([u,v])
    visited[u][v] = 1
    cnt = 1

    while queue:
        i_x, j_y = queue.popleft()
        for c in range(4):
            x = i_x + dx[c]
            y = j_y + dy[c]
            if 0 <= x < M and 0 <= y < N:
                if arr[x][y] == 0 and visited[x][y] != 1:
                    queue.append([x, y])
                    visited[x][y] = 1
                    cnt += 1
    areas.append(cnt)



M, N, K = list(map(int, input().split()))
arr = [[0]*N for _ in range(M)]
visited = [[0]*N for ___ in range(M)]
areas = []

# v1
# for __ in range(K):
#     a_j, b_i, c_j, d_i = list(map(int, input().split()))
#     b_i = (M-1)-b_i
#     c_j -= 1
#     d_i = M-d_i
#     for i in range(M):
#         for j in range(N):
#             if d_i <= i <= b_i and a_j <= j <= c_j:
#                 if arr[i][j] == 0:
#                     arr[i][j] = 1

# v2
for __ in range(K):
    a_j, b_i, c_j, d_i = list(map(int, input().split()))
    for i in range(b_i, d_i):
        for j in range(a_j, c_j):
            arr[i][j] = 1
print(arr)

for u in range(M):
    for v in range(N):
        if arr[u][v] == 0 and visited[u][v] != 1:
            bfs(u,v)

areas.sort()
print(len(areas))
print(*areas)
# for area in areas:
#     print(area, end=" ")