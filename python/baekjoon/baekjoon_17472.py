# baekjoon_17472 다리만들기 2

# v1
# from collections import defaultdict, deque
#
# def finding_coast(i,j,island_num):
#     queue = deque()
#     queue.append([i,j])
#     visited1[i][j] = 1
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         arr[s_i][s_j] = island_num
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M and visited1[x][y] == 0:
#                 if arr[x][y] == 0 and [s_i, s_j] not in coasts[island_num]:
#                     coasts[island_num].append([s_i, s_j])
#                     visited1[s_i][s_j] = 1
#
#                 # if arr[s_i][s_j] == 1 and arr[x][y] == 1:
#                 if arr[x][y] == 1:
#                     queue.append([x, y])
#                     visited1[x][y] = 1
#
# def finding_bridge(coast, island_start):
#     c_i, c_j = coast
#     for c in range(4):
#         x = c_i + dx[c]
#         y = c_j + dy[c]
#         if 0 <= x < N and 0 <= y < M and arr[x][y] == 0:
#             stack = []
#             cnt = 1
#             stack.append([x,y])
#             start_tmp = 0
#             end_tmp = 0
#             while stack:
#                 s_i, s_j = stack.pop()
#                 nx = s_i + dx[c]
#                 ny = s_j + dy[c]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if arr[nx][ny] == 0:
#                         cnt +=1
#                         stack.append([nx, ny])
#                     if arr[nx][ny] != 0 and cnt > 1:
#                         if arr[nx][ny] > island_start:
#                             start_tmp = island_start
#                             end_tmp = arr[nx][ny]
#                         elif arr[nx][ny] < island_start:
#                             start_tmp = arr[nx][ny]
#                             end_tmp = island_start
#                         if bridges[(start_tmp, end_tmp)] == 0:
#                             bridges[(start_tmp, end_tmp)] = cnt
#                         else:
#                             bridges[(start_tmp, end_tmp)] = min(bridges[(start_tmp, end_tmp)], cnt)
#                         break
#
#
# def finding_parents(x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents[x])
#     return parents[x]
#
# def union_parents(a, b):
#     a = finding_parents(a)
#     b = finding_parents(b)
#     if a < b:
#         parents[b] = a
#     else:
#         parents[a] = b
#
# N, M = map(int, input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
#
# # 섬 번호 세기기와 해변가 찾기
# coasts = defaultdict(list)
# island_num = 0
# visited1 = [[0]*M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1 and visited1[i][j] == 0:
#             island_num += 1
#             finding_coast(i,j,island_num)
#
# # 다리 찾기
# bridges = defaultdict(int)
# for key in coasts:
#     for coast in coasts[key]:
#         finding_bridge(coast, key)
#
# # mst
# edges = []
# for key in bridges:
#     edges.append([bridges[key], key[0], key[1]])
# edges.sort()
#
# parents = [0]*(island_num + 1)
#
# for i in range(1, island_num+1):
#     parents[i] = i
#
# # c 길이, a 섬1, b 섬2
# res = 0
# visited_cnt = 0
# for edge in edges:
#     c, a, b = edge
#     if finding_parents(a) != finding_parents(b):
#         union_parents(a, b)
#         res += c
#         visited_cnt += 1
#
# if visited_cnt == island_num-1:
#     print(res)
# else:
#     print(-1)


# v2
# from collections import defaultdict, deque
#
# def finding_coast(i,j,island_num):
#     queue = deque()
#     queue.append([i,j])
#     visited1[i][j] = 1
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         arr[s_i][s_j] = island_num
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M and visited1[x][y] == 0:
#                 if arr[x][y] == 0 and [s_i, s_j] not in coasts[island_num]:
#                     coasts[island_num].append([s_i, s_j])
#                     visited1[s_i][s_j] = 1
#
#                 # if arr[s_i][s_j] == 1 and arr[x][y] == 1:
#                 if arr[x][y] == 1:
#                     queue.append([x, y])
#                     visited1[x][y] = 1
#
# def finding_bridge(coast, island_start):
#     c_i, c_j = coast
#     for c in range(4):
#         x = c_i + dx[c]
#         y = c_j + dy[c]
#         if 0 <= x < N and 0 <= y < M and arr[x][y] == 0:
#             stack = []
#             cnt = 1
#             stack.append([x,y])
#             start_tmp = 0
#             end_tmp = 0
#             while stack:
#                 s_i, s_j = stack.pop()
#                 nx = s_i + dx[c]
#                 ny = s_j + dy[c]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if arr[nx][ny] == 0:
#                         cnt +=1
#                         stack.append([nx, ny])
#                     if arr[nx][ny] != 0 and cnt > 1:
#                         if arr[nx][ny] > island_start:
#                             start_tmp = island_start
#                             end_tmp = arr[nx][ny]
#                         elif arr[nx][ny] < island_start:
#                             start_tmp = arr[nx][ny]
#                             end_tmp = island_start
#                         if bridges[(start_tmp, end_tmp)] == 0:
#                             bridges[(start_tmp, end_tmp)] = cnt
#                         else:
#                             bridges[(start_tmp, end_tmp)] = min(bridges[(start_tmp, end_tmp)], cnt)
#                         break
#
#
# def finding_parents(x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents[x])
#     return parents[x]
#
# def union_parents(a, b):
#     a = finding_parents(a)
#     b = finding_parents(b)
#     if a < b:
#         parents[b] = a
#     else:
#         parents[a] = b
#
# N, M = map(int, input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
#
# # 섬 번호 세기기와 해변가 찾기
# coasts = defaultdict(list)
# island_num = 0
# visited1 = [[0]*M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1 and visited1[i][j] == 0:
#             island_num += 1
#             finding_coast(i,j,island_num)
#
# # 다리 찾기
# bridges = defaultdict(int)
# for key in coasts:
#     for coast in coasts[key]:
#         finding_bridge(coast, key)
#
# # mst
# edges = []
# for key in bridges:
#     edges.append([bridges[key], key[0], key[1]])
# edges.sort()
#
# parents = [0]*(island_num + 1)
#
# for i in range(1, island_num+1):
#     parents[i] = i
#
# # c 길이, a 섬1, b 섬2
# res = 0
# visited_cnt = 0
# for edge in edges:
#     c, a, b = edge
#     if finding_parents(a) != finding_parents(b):
#         union_parents(a, b)
#         res += c
#         visited_cnt += 1
#
#
# for i in range(1, island_num+1):
#     if finding_parents(i) != 1:
#         res = -1
#         break
# print(res)

# v3
from collections import defaultdict, deque

def finding_coast(i,j,island_num):
    queue = deque()
    queue.append([i,j])
    visited1[i][j] = 1

    while queue:
        s_i, s_j = queue.popleft()
        arr[s_i][s_j] = island_num
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M and visited1[x][y] == 0:
                if arr[x][y] == 0 and [s_i, s_j] not in coasts[island_num]:
                    coasts[island_num].append([s_i, s_j])
                    visited1[s_i][s_j] = 1

                # if arr[s_i][s_j] == 1 and arr[x][y] == 1:
                if arr[s_i][s_j] != 0 and arr[x][y] == 1:
                # if arr[x][y] == 1:
                    queue.append([x, y])
                    visited1[x][y] = 1

def finding_bridge(coast, island_start):
    c_i, c_j = coast
    for c in range(4):
        x = c_i + dx[c]
        y = c_j + dy[c]
        if 0 <= x < N and 0 <= y < M and arr[x][y] == 0:
            stack = []
            cnt = 1
            stack.append([x,y])
            start_tmp = 0
            end_tmp = 0
            while stack:
                s_i, s_j = stack.pop()
                nx = s_i + dx[c]
                ny = s_j + dy[c]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] == 0:
                        cnt +=1
                        stack.append([nx, ny])
                    if arr[nx][ny] != 0 and cnt > 1:
                        if arr[nx][ny] > island_start:
                            start_tmp = island_start
                            end_tmp = arr[nx][ny]
                        elif arr[nx][ny] < island_start:
                            start_tmp = arr[nx][ny]
                            end_tmp = island_start
                        if bridges[(start_tmp, end_tmp)] == 0:
                            bridges[(start_tmp, end_tmp)] = cnt
                        else:
                            bridges[(start_tmp, end_tmp)] = min(bridges[(start_tmp, end_tmp)], cnt)
                        break


def finding_parents(x):
    if parents[x] != x:
        parents[x] = finding_parents(parents[x])
    return parents[x]

def union_parents(a, b):
    a = finding_parents(a)
    b = finding_parents(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]


# 섬 번호 세기기와 해변가 찾기
coasts = defaultdict(list)
island_num = 0
visited1 = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited1[i][j] == 0:
            island_num += 1
            finding_coast(i,j,island_num)

# 다리 찾기
bridges = defaultdict(int)
for key in coasts:
    for coast in coasts[key]:
        finding_bridge(coast, key)

# mst
edges = []
for key in bridges:
    edges.append([bridges[key], key[0], key[1]])
edges.sort()

parents = [0]*(island_num + 1)

for i in range(1, island_num+1):
    parents[i] = i

# c 길이, a 섬1, b 섬2
res = 0
visited_cnt = 0
for edge in edges:
    c, a, b = edge
    if finding_parents(a) != finding_parents(b):
        union_parents(a, b)
        res += c
        visited_cnt += 1


for i in range(1, island_num+1):
    if finding_parents(i) != 1:
        res = -1
        break
print(res)

