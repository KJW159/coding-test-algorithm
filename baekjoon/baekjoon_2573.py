# baekjoon_2573 빙산

# v1
# import collections

# def melting(i, j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#     ocean = 0
#
#     for c in range(4):
#         x = i + dx[c]
#         y = j + dy[c]
#         if arr[x][y] == 0:
#             ocean += 1
#     melting_ice.append([i,j,ocean])
#     # arr[i][j] -= ocean
#     # if arr[i][j] < 0:
#     #     arr[i][j] = 0
#     return
#
#
# def bfs(s_i, s_j):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     queue = collections.deque()
#     queue.append([s_i, s_j])
#     visited[s_i][s_j] = 1
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for k in range(4):
#             x = s_i + dx[k]
#             y = s_j + dy[k]
#             if arr[x][y] != 0 and visited[x][y] == 0:
#                 queue.append([x, y])
#                 visited[x][y] = 1
#     return
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# years = 0
# res = 0
# while True:
#     melting_ice = []
#     for i1 in range(1, N-1):
#         for j1 in range(1, M-1):
#             if arr[i1][j1] != 0:
#                 melting(i1, j1)
#     for i3, j3, melting_level in melting_ice:
#         arr[i3][j3] -= melting_level
#         if arr[i3][j3] < 0:
#             arr[i3][j3] = 0
#
#     years += 1
#     ice_group = 0
#     trg = True
#     visited = [[0]*M for __ in range(N)]
#     for i2 in range(1, N-1):
#         for j2 in range(1, M-1):
#             if arr[i2][j2] != 0 and visited[i2][j2] == 0:
#                 bfs(i2, j2)
#                 ice_group += 1
#                 trg = False
#     if trg and ice_group == 0:
#         res = 0
#         break
#     elif ice_group >= 2:
#         res = years
#         break
# print(res)


# v2
import collections

def melting(i, j):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    ocean = 0

    for c in range(4):
        x = i + dx[c]
        y = j + dy[c]
        if arr[x][y] == 0:
            ocean += 1
    melting_ice.append([i,j,ocean])
    return


def bfs(s_i, s_j):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    queue = collections.deque()
    queue.append([s_i, s_j])
    visited[s_i][s_j] = 1

    while queue:
        s_i, s_j = queue.popleft()
        for k in range(4):
            x = s_i + dx[k]
            y = s_j + dy[k]
            if arr[x][y] != 0 and visited[x][y] == 0:
                queue.append([x, y])
                visited[x][y] = 1
    return


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

years = 0
res = 0
while True:
    melting_ice = []
    for i1 in range(1, N-1):
        for j1 in range(1, M-1):
            if arr[i1][j1] != 0:
                melting(i1, j1)
    for i3, j3, melting_level in melting_ice:
        arr[i3][j3] -= melting_level
        if arr[i3][j3] < 0:
            arr[i3][j3] = 0

    years += 1
    ice_group = 0
    trg = False
    visited = [[0]*M for __ in range(N)]
    for i2 in range(1, N-1):
        if trg:
            break
        for j2 in range(1, M-1):
            if arr[i2][j2] != 0 and visited[i2][j2] == 0:
                bfs(i2, j2)
                ice_group += 1
                if ice_group >= 2:
                    trg = True
                    break
    if trg == False and ice_group == 0:
        res = 0
        break
    elif trg:
        res = years
        break
print(res)
