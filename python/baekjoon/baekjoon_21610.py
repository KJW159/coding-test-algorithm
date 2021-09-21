# baekjoon_21610 마법사 상어와 비바라기
# v1
# def moving_clouds(di, si, clouds):
#     for i in range(4):
#         x, y = clouds[i]
#         nx = (x + dx[di]*si) % N
#         ny = (y + dy[di]*si) % N
#         arr[nx][ny] += 1
#         clouds[i] = [nx, ny]
#     for i in range(4):
#         cnt = 0
#         x, y = clouds[i]
#         for j in range(2, 9, 2):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[nx][ny] > 0:
#                     cnt += 1
#         arr[x][y] += cnt
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] >= 2 and [i, j] not in clouds:
#                 arr[i][j] -= 2
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# # clouds = [[N-1,0], [N-1,1], [N-2,0], [N-2,1]]
# # ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 순서대로 1번부터 8번임
# dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
#
# for _ in range(M):
#     di, si = map(int, input().split())
#     clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
#     moving_clouds(di, si, clouds)
#     print(arr)
# res = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] >= 1:
#             res += arr[i][j]
# print(res)



# v2
# import sys
#
# input = sys.stdin.readline
#
# def moving_clouds(di, si, clouds):
#     rained = []
#     for x,y in clouds:
#         nx = (x + dx[di]*si) % N
#         ny = (y + dy[di]*si) % N
#         arr[nx][ny] += 1
#         rained.append([nx, ny])
#     for x, y in rained:
#         cnt = 0
#         for j in range(2, 9, 2):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[nx][ny] > 0:
#                     cnt += 1
#         arr[x][y] += cnt
#
#     clouds = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] >= 2 and [i, j] not in rained:
#                 arr[i][j] -= 2
#                 clouds.append([i,j])
#     return clouds
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# clouds = [[N-1,0], [N-1,1], [N-2,0], [N-2,1]]
# # ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 순서대로 1번부터 8번임
# dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
#
# for _ in range(M):
#     di, si = map(int, input().split())
#     clouds = moving_clouds(di, si, clouds)
# res = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] >= 1:
#             res += arr[i][j]
# print(res)


# v3
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# clouds = [[N-1,0], [N-1,1], [N-2,0], [N-2,1]]
# # ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 순서대로 1번부터 8번임
# dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
#
# for _ in range(M):
#     di, si = map(int, input().split())
#     rained = []
#     visited = [[0]*N for _ in range(N)]
#     for x, y in clouds:
#         nx = (x + dx[di]*si) % N
#         ny = (y + dy[di]*si) % N
#         arr[nx][ny] += 1
#         rained.append([nx, ny])
#         visited[nx][ny] = 1
#     for x, y in rained:
#         cnt = 0
#         for j in range(2, 9, 2):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[nx][ny] > 0:
#                     cnt += 1
#         arr[x][y] += cnt
#     clouds = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] >= 2 and visited[i][j] == 0:
#                 arr[i][j] -= 2
#                 clouds.append([i,j])
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] >= 1:
#             res += arr[i][j]
# print(res)


# v4
def moving_clouds(di, si, clouds):
    rained = []
    visited = [[0]*N for _ in range(N)]
    for x,y in clouds:
        nx = (x + dx[di]*si) % N
        ny = (y + dy[di]*si) % N
        arr[nx][ny] += 1
        rained.append([nx, ny])
        visited[nx][ny] = 1
    for x, y in rained:
        cnt = 0
        for j in range(2, 9, 2):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > 0:
                    cnt += 1
        arr[x][y] += cnt
    clouds = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and visited[i][j] == 0:
                arr[i][j] -= 2
                clouds.append([i,j])
    return clouds

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

clouds = [[N-1,0], [N-1,1], [N-2,0], [N-2,1]]
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 순서대로 1번부터 8번임
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    di, si = map(int, input().split())
    clouds = moving_clouds(di, si, clouds)
res = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] >= 1:
            res += arr[i][j]
print(res)