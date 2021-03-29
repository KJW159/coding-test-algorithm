# baekjoon_20058 마법사 상어와 파이어스톰

# v1
# def melting(s_i, s_j, K):
#     cnt = 0
#     trg = False
#     for c in range(4):
#         nx = s_i + dx[c]
#         ny = s_j + dy[c]
#         if 0 <= nx < K and 0 <= ny < K:
#             if arr[nx][ny]:
#                 cnt += 1
#         if cnt == 3:
#             trg = True
#             break
#     return trg
#
# def finding_ice(s_i, s_j, K):
#     stack = []
#     visited[s_i][s_j] = 1
#     stack.append([s_i,s_j])
#     cnt_tmp = 1
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             nx = s_i + dx[c]
#             ny = s_j + dy[c]
#             if 0 <= nx < K and 0 <= ny < K:
#                 if visited[nx][ny] == 0 and arr[nx][ny] !=0:
#                     cnt_tmp += 1
#                     stack.append([nx,ny])
#                     visited[nx][ny] = 1
#     return cnt_tmp
#
#
#
# N, Q = map(int, input().split())
# K = 2**N
# arr = [list(map(int, input().split())) for _ in range(K)]
# steps = list(map(int, input().split()))
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# visited = [[0]*K for _ in range(K)]
#
# for L in steps:
#     p = 2**L
#     for x in range(0,K,p):
#         for y in range(0,K,p):
#             tmp = [arr[i][y:y+p] for i in range(x,x+p)]
#             for i in range(p):
#                 for j in range(p):
#                     arr[x+j][y+p-1-i] = tmp[i][j]
#
#     melting_ice = []
#     for i in range(K):
#         for j in range(K):
#             if not melting(i,j,K):
#                 melting_ice.append([i,j])
#
#     for i_x, i_y in melting_ice:
#         if arr[i_x][i_y]:
#             arr[i_x][i_y] -= 1
#
# total_ice = 0
# area = 0
# for i in range(K):
#     for j in range(K):
#         total_ice += arr[i][j]
#         if visited[i][j] == 0 and arr[i][j] !=0:
#             area = max(area, finding_ice(i,j,K))
# print(total_ice)
# print(area)


# v2
from collections import deque

def melting(s_i, s_j, K):
    cnt = 0
    trg = False
    for c in range(4):
        nx = s_i + dx[c]
        ny = s_j + dy[c]
        if 0 <= nx < K and 0 <= ny < K:
            if arr[nx][ny]:
                cnt += 1
        if cnt == 3:
            trg = True
            break
    return trg

def finding_ice(s_i, s_j, K):
    queue = deque()
    visited[s_i][s_j] = 1
    queue.append([s_i,s_j])
    cnt_tmp = 1
    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            nx = s_i + dx[c]
            ny = s_j + dy[c]
            if 0 <= nx < K and 0 <= ny < K:
                if visited[nx][ny] == 0 and arr[nx][ny] !=0:
                    cnt_tmp += 1
                    queue.append([nx,ny])
                    visited[nx][ny] = 1
    return cnt_tmp



N, Q = map(int, input().split())
K = 2**N
arr = [list(map(int, input().split())) for _ in range(K)]
steps = list(map(int, input().split()))

dx = [0,-1,0,1]
dy = [-1,0,1,0]
visited = [[0]*K for _ in range(K)]

for L in steps:
    p = 2**L
    for x in range(0,K,p):
        for y in range(0,K,p):
            tmp = [arr[i][y:y+p] for i in range(x,x+p)]
            for i in range(p):
                for j in range(p):
                    arr[x+j][y+p-1-i] = tmp[i][j]

    melting_ice = []
    for i in range(K):
        for j in range(K):
            if not melting(i,j,K):
                melting_ice.append([i,j])

    for i_x, i_y in melting_ice:
        if arr[i_x][i_y]:
            arr[i_x][i_y] -= 1

total_ice = 0
area = 0
for i in range(K):
    for j in range(K):
        total_ice += arr[i][j]
        if visited[i][j] == 0 and arr[i][j]:
            area = max(area, finding_ice(i,j,K))
print(total_ice)
print(area)

