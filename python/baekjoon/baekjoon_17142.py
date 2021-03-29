# baekjoon_17142 연구소3

# v1
# import collections

# def combinations_virus(arr, r):
#     for c in range(len(arr)):
#         if r == 1:
#             yield [arr[c]]
#         else:
#             for next in combinations_virus(arr[c+1:], r-1):
#                 yield [arr[c]] + next
#
# def bfs(viruses):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     # lab_copy = [lab[i][:] for __ in range(N)]
#     visited = [[-1]*N for ___ in range(N)]
#     queue = collections.deque()
#
#     s_cnt = 0
#     time_cnt = 0
#
#     for virus in viruses:
#         v1, v2 = virus
#         queue.append([v1, v2])
#         s_cnt += 1
#         visited[v1][v2] = 0
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for k in range(4):
#             x = s_i + dx[k]
#             y = s_j + dy[k]
#             if 0 <= x < N and 0 <= y < N:
#                 if lab[x][y] != 1 and visited[x][y] == -1:
#                     s_cnt += 1
#                     if lab[x][y] == 0:
#                         # s_cnt += 1
#                         queue.append([x, y])
#                         visited[x][y] = visited[s_i][s_j] + 1
#                     if lab[x][y] == 2:
#                         # s_cnt += 1
#                         visited[x][y] = 0
#
#     for i2 in range(N):
#         for j2 in range(N):
#             if visited[i2][j2] > time_cnt:
#                 time_cnt = visited[i2][j2]
#
#     return s_cnt, time_cnt
#
#
# N, M = map(int, input().split())
#
# lab = [list(map(int, input().split())) for _ in range(N)]
#
# virus_list = []
# space = 0
# time = N*N
# res = 0
# for i in range(N):
#     for j in range(N):
#         if lab[i][j] == 2:
#             virus_list.append([i, j])
#         if lab[i][j] != 1:
#             space += 1
#
# for viruses in combinations_virus(virus_list, M):
#     cnt_tmp, time_tmp = bfs(viruses)
#     print(space, cnt_tmp)
#     if cnt_tmp == space:
#         time = min(time, time_tmp)
#         res = time
#     # elif cnt_tmp != space and time == N*N:
#     elif time == N*N:
#         res = -1
# print(res)


# v2

# import collections
#
# def combinations_virus(arr, r):
#     for c in range(len(arr)):
#         if r == 1:
#             yield [arr[c]]
#         else:
#             for next in combinations_virus(arr[c+1:], r-1):
#                 yield [arr[c]] + next
#
# def bfs(viruses):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     # lab_copy = [lab[i][:] for __ in range(N)]
#     visited = [[-1]*N for ___ in range(N)]
#     queue = collections.deque()
#
#     s_cnt = 0
#     time_cnt = 0
#
#     for virus in viruses:
#         v1, v2 = virus
#         queue.append([v1, v2])
#         s_cnt += 1
#         visited[v1][v2] = 0
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for k in range(4):
#             x = s_i + dx[k]
#             y = s_j + dy[k]
#             if 0 <= x < N and 0 <= y < N:
#                 if lab[x][y] != 1 and visited[x][y] == -1:
#                     s_cnt += 1
#                     if lab[x][y] == 0:
#                         queue.append([x, y])
#                         visited[x][y] = visited[s_i][s_j] + 1
#                     if lab[x][y] == 2 and lab[s_i][s_j] != 2:
#                         # queue.append([x, y])
#                         visited[x][y] = visited[s_i][s_j]
#                         # visited[x][y] = 0
#                     elif lab[x][y] == 2 and lab[s_i][s_j] == 2:
#                         queue.append([x, y])
#                         visited[x][y] = 0
#
#
#     for i2 in range(N):
#         for j2 in range(N):
#             if visited[i2][j2] > time_cnt:
#                 time_cnt = visited[i2][j2]
#
#     return s_cnt, time_cnt
#
#
# N, M = map(int, input().split())
#
# lab = [list(map(int, input().split())) for _ in range(N)]
#
# virus_list = []
# space = 0
# time = N*N
# res = 0
# for i in range(N):
#     for j in range(N):
#         if lab[i][j] == 2:
#             virus_list.append([i, j])
#         if lab[i][j] != 1:
#             space += 1
#
# for viruses in combinations_virus(virus_list, M):
#     cnt_tmp, time_tmp = bfs(viruses)
#     if cnt_tmp == space:
#         time = min(time, time_tmp)
#         res = time
#     # elif cnt_tmp != space and time == N*N:
#     elif time == N*N:
#         res = -1
# print(res)


# v3
# import collections
#
# def combinations_virus(arr, r):
#     for c in range(len(arr)):
#         if r == 1:
#             yield [arr[c]]
#         else:
#             for next in combinations_virus(arr[c+1:], r-1):
#                 yield [arr[c]] + next
#
# def bfs(viruses):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     # lab_copy = [lab[i][:] for __ in range(N)]
#     visited = [[-1]*N for ___ in range(N)]
#     visited2 = [[0]*N for _ in range(N)]
#     queue = collections.deque()
#     visited_tmp = 0
#     s_cnt = 0
#     time_cnt = 0
#     print(viruses)
#     for virus in viruses:
#         v1, v2 = virus
#         queue.append([v1, v2])
#         s_cnt += 1
#         visited[v1][v2] = 0
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for k in range(4):
#             x = s_i + dx[k]
#             y = s_j + dy[k]
#             if 0 <= x < N and 0 <= y < N:
#                 if lab[x][y] != 1 and visited[x][y] == -1:
#                     s_cnt += 1
#                     print("s_cnt," ,s_cnt)
#                     # 빈 칸에 바이러스가 옮겨질 때
#                     if lab[x][y] == 0:
#                         queue.append([x, y])
#                         visited[x][y] = visited[s_i][s_j] + 1
#                     # 빈칸을 통해 옮겨 온 바이러스에 의해 비활성 바이러스가 활성화될때
#                     if lab[s_i][s_j] == 0 and lab[x][y] == 2 and [x, y] not in viruses:
#                         queue.append([x, y])
#                         visited_tmp += 1
#                         visited[x][y] = visited[s_i][s_j]
#                     # 목록에 있는 바이러스가 비활성을 활성 시킬때
#                     if lab[x][y] == 2 and [s_i,s_j] in viruses:
#                         queue.append([x, y])
#                         visited_tmp += 1
#                         visited[x][y] = visited[s_i][s_j]
#
#                     # 리스트에 없던 바이러스가 활성화 되어 옮길때
#                     if lab[s_i][s_j] == 2 and [s_i, s_j] not in viruses:
#                         # queue.append([x, y])
#                         if lab[x][y] == 0:
#                             queue.append([x, y])
#                             visited[x][y] = visited[s_i][s_j] + visited_tmp
#                             visited_tmp = 0
#                         if lab[x][y] == 2:
#                             queue.append([x, y])
#                             visited_tmp += 1
#                             visited[x][y] = visited[s_i][s_j]
#                         # visited[x][y] = 0
#
#
#     for i2 in range(N):
#         for j2 in range(N):
#             if visited[i2][j2] > time_cnt:
#                 time_cnt = visited[i2][j2]
#
#     return s_cnt, time_cnt
#
#
# N, M = map(int, input().split())
#
# lab = [list(map(int, input().split())) for _ in range(N)]
#
# virus_list = []
# space = 0
# time = N*N
# res = 0
# for i in range(N):
#     for j in range(N):
#         if lab[i][j] == 2:
#             virus_list.append([i, j])
#         if lab[i][j] != 1:
#             space += 1
#
# for viruses in combinations_virus(virus_list, M):
#     cnt_tmp, time_tmp = bfs(viruses)
#     print(cnt_tmp, space)
#     if cnt_tmp == space:
#         time = min(time, time_tmp)
#         res = time
#     # elif cnt_tmp != space and time == N*N:
#     elif time == N*N:
#         res = -1
# print(res)


# v4
import collections

def combinations_virus(arr, r):
    for c in range(len(arr)):
        if r == 1:
            yield [arr[c]]
        else:
            for next in combinations_virus(arr[c+1:], r-1):
                yield [arr[c]] + next

def bfs(viruses):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    visited = [[-1]*N for ___ in range(N)]
    # visited_tmp2 = 0

    queue = collections.deque()
    s_cnt = 0
    time_cnt = 0

    for virus in viruses:
        # trg가 다른 곳에서 켜지고 바로 0을 만날때 혼동을 방지하기 위해서
        # 자기가 따라온 곳에서 trg가 켜진것인지 아니면 다른 곳에서 켜진 것인지 알기 위해 같이 넣어줌.
        v1, v2, virus_trg, visited_tmp = virus
        queue.append([v1, v2, 0, 0])
        s_cnt += 1
        visited[v1][v2] = 0

    while queue:
        s_i, s_j, virus_trg, visited_tmp = queue.popleft()
        for k in range(4):
            visited_tmp2 = visited_tmp
            x = s_i + dx[k]
            y = s_j + dy[k]
            if 0 <= x < N and 0 <= y < N:
                if lab[x][y] != 1 and visited[x][y] == -1:

                    # 0인데 virus_trg가 꺼져 있을때
                    if lab[x][y] == 0 and virus_trg == 0:
                        visited[x][y] = visited[s_i][s_j] + 1

                    # 0인데 virus_trg가 켜져 있을때
                    if lab[x][y] == 0 and virus_trg == 1:
                        visited_tmp += visited[s_i][s_j]
                        visited[x][y] = visited_tmp + 1
                        visited_tmp = 0
                        virus_trg = 0

                    # 2(비활성화 바이러스)를 만났을때
                    if lab[x][y] == 2:
                        virus_trg = 1
                        visited_tmp2 += 1
                        visited[x][y] = visited[s_i][s_j]
                    s_cnt += 1
                    queue.append([x, y, virus_trg, visited_tmp2])


    for i2 in range(N):
        for j2 in range(N):
            if visited[i2][j2] > time_cnt:
                time_cnt = visited[i2][j2]

    return s_cnt, time_cnt


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

virus_list = []
space = 0
time = N*N
res = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_list.append([i, j, 0, 0])
        if lab[i][j] != 1:
            space += 1

for viruses in combinations_virus(virus_list, M):
    cnt_tmp, time_tmp = bfs(viruses)

    if cnt_tmp == space:
        time = min(time, time_tmp)
        res = time
    elif time == N*N:
        res = -1
print(res)

