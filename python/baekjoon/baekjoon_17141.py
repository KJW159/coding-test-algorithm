# baekjoon_17141 연구소2

# v1
# import math, collections
#
# def combinations_viruses(arr, r):
#     for c in range(len(arr)):
#         if r == 1:
#             yield [arr[c]]
#         else:
#             for next in combinations_viruses(arr[c+1:], r-1):
#                 yield [arr[c]] + next
#
#
# def bfs(virus):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#     lab_copy = [lab[i][:] for i in range(N)]
#     time = 0
#
#     # 필요 하나?
#     for i in range(N):
#         for j in range(N):
#             if lab_copy[i][j] == 2:
#                 lab_copy[i][j] = 0
#
#     visited = [[0]*N for _ in range(N)]
#     queue = collections.deque()
#
#     for v in virus:
#         v1, v2 = v
#         queue.append([v1,v2])
#         lab_copy[v1][v2] = 2
#         visited[v1][v2] = 1
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for k in range(4):
#             x = s_i + dx[k]
#             y = s_j + dy[k]
#             if 0 <= x < N and 0 <= y < N:
#                 if lab_copy[x][y] == 0 and visited[x][y] == 0:
#                     queue.append([x,y])
#                     lab_copy[x][y] = 2
#                     visited[x][y] = visited[s_i][s_j] + 1
#     # trg == True 면 빈칸이 있음.
#     trg = False
#     for i2 in range(N):
#         if trg:
#             break
#         for j2 in range(N):
#             if lab_copy[i2][j2] == 0:
#                 trg = True
#                 break
#
#     if not trg:
#         for i2 in range(N):
#             for j2 in range(N):
#                 if visited[i2][j2] > time:
#                     time = visited[i2][j2]
#     else:
#         time = math.inf
#
#     return time
#
#
# N, M = map(int, input().split())
#
# lab = [list(map(int, input().split())) for _ in range(N)]
# INF = math.inf
# min_time = INF
# viruses_tmp = []
#
# for i in range(N):
#     for j in range(N):
#         if lab[i][j] == 2:
#             viruses_tmp.append([i, j])
#
# viruses_comb = []
#
# for comb in combinations_viruses(viruses_tmp, M):
#     viruses_comb.append(comb)
#
#
# for virus in viruses_comb:
#     time = bfs(virus)
#     if time < min_time:
#         min_time = time
#
# if min_time == INF:
#     print(-1)
# else:
#     print(min_time-1)

# v2
import math, collections

def combinations_viruses(arr, r):
    for c in range(len(arr)):
        if r == 1:
            yield [arr[c]]
        else:
            for next in combinations_viruses(arr[c+1:], r-1):
                yield [arr[c]] + next


def bfs(virus):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    lab_copy = [lab[i][:] for i in range(N)]
    time = 0

    visited = [[0]*N for _ in range(N)]
    queue = collections.deque()

    for v in virus:
        v1, v2 = v
        queue.append([v1,v2])
        lab_copy[v1][v2] = 2
        visited[v1][v2] = 1

    while queue:
        s_i, s_j = queue.popleft()
        for k in range(4):
            x = s_i + dx[k]
            y = s_j + dy[k]
            if 0 <= x < N and 0 <= y < N:
                if lab_copy[x][y] != 1 and visited[x][y] == 0:
                    queue.append([x,y])
                    lab_copy[x][y] = 2
                    visited[x][y] = visited[s_i][s_j] + 1
    # trg == True 면 빈칸이 있음.
    trg = False
    for i2 in range(N):
        if trg:
            break
        for j2 in range(N):
            if lab_copy[i2][j2] == 0:
                trg = True
                break

    if not trg:
        for i2 in range(N):
            for j2 in range(N):
                if visited[i2][j2] > time:
                    time = visited[i2][j2]
    else:
        time = math.inf

    return time


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]
INF = math.inf
min_time = INF
viruses_tmp = []

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            viruses_tmp.append([i, j])

viruses_comb = []

for comb in combinations_viruses(viruses_tmp, M):
    viruses_comb.append(comb)


for virus in viruses_comb:
    time = bfs(virus)
    if time < min_time:
        min_time = time

if min_time == INF:
    print(-1)
else:
    print(min_time-1)