# baekjoon_2146 다리 만들기

# v2
# from collections import deque
# import math, sys
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# def marking_island(m_i, m_j, marking_num):
#     queue_m = deque()
#     queue_m.append([m_i, m_j])
#     visited_marking[m_i][m_j] = 1
#     arr[m_i][m_j] = marking_num
#
#     while queue_m:
#         m_i, m_j = queue_m.popleft()
#         for m in range(4):
#             m_x = m_i + dx[m]
#             m_y = m_j + dy[m]
#             if 0 <= m_x < N and 0 <= m_y < N:
#                 if arr[m_x][m_y] != 0 and visited_marking[m_x][m_y] == 0:
#                     queue_m.append([m_x, m_y])
#                     visited_marking[m_x][m_y] = 1
#                     arr[m_x][m_y] = marking_num
#
#
# def finding_coast(f_i, f_j):
#     queue_f = deque()
#     queue_f.append([f_i, f_j])
#     visited_coast[f_i][f_j] = 1
#
#     while queue_f:
#         f_i, f_j = queue_f.popleft()
#         for f in range(4):
#             f_x = f_i + dx[f]
#             f_y = f_j + dy[f]
#             if 0 <= f_x < N and 0 <= f_y < N and visited_coast[f_x][f_y] == 0:
#                 if arr[f_x][f_y] == 0:
#                     queue_f.append([f_x, f_y])
#                     visited_coast[f_x][f_y] = 1
#                 if arr[f_x][f_y] >= 1:
#                     coast.append([f_x, f_y, arr[f_x][f_y]])
#                     visited_coast[f_x][f_y] = 1
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
#
# def finding_bridge(land1, land2):
#     land1_i, land1_j, land1_num = land1
#     land2_i, land2_j, land2_num = land2
#     visited = [[-1] * N for ___ in range(N)]
#
#     queue_b = deque()
#     queue_b.append([land1_i, land1_j])
#     visited[land1_i][land1_j] = 0
#
#
#     while queue_b:
#         s_i, s_j = queue_b.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == -1:
#                 if arr[x][y] == 0:
#                     queue_b.append([x, y])
#                     visited[x][y] = visited[s_i][s_j] + 1
#                 if x == land2_i and y == land2_j:
#                     return visited[s_i][s_j]
#     return math.inf
#
#
# N = int(input())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# visited_marking = [[0]*N for __ in range(N)]
# visited_coast = [[0]*N for __ in range(N)]
#
# marking_num = 0
# coast = []
# bridge_min = math.inf
# for i in range(N):
#     for j in range(N):
#         if visited_marking[i][j] == 0 and arr[i][j] == 1:
#             marking_num += 1
#             marking_island(i,j, marking_num)
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 0 and visited_coast[i][j] == 0:
#             finding_coast(i,j)
#
#
# for land1, land2 in combinations1(coast, 2):
#     if land1[2] == land2[2]:
#         continue
#     else:
#         bridge = finding_bridge(land1, land2)
#         if bridge < bridge_min:
#             bridge_min = bridge
# print(bridge_min)

# v3
# from collections import deque
# import math, sys
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# def marking_island(m_i, m_j, marking_num):
#     queue.append([m_i, m_j])
#     visited_marking[m_i][m_j] = 1
#     arr[m_i][m_j] = marking_num
#
#     while queue:
#         m_i, m_j = queue.popleft()
#         for m in range(4):
#             m_x = m_i + dx[m]
#             m_y = m_j + dy[m]
#             if 0 <= m_x < N and 0 <= m_y < N:
#                 if arr[m_x][m_y] != 0 and visited_marking[m_x][m_y] == 0:
#                     queue.append([m_x, m_y])
#                     visited_marking[m_x][m_y] = 1
#                     arr[m_x][m_y] = marking_num
#
#
# def finding_coast(f_i, f_j):
#     queue = deque()
#     queue.append([f_i, f_j])
#     visited_coast[f_i][f_j] = 1
#
#     while queue:
#         f_i, f_j = queue.popleft()
#         for f in range(4):
#             f_x = f_i + dx[f]
#             f_y = f_j + dy[f]
#             if 0 <= f_x < N and 0 <= f_y < N and visited_coast[f_x][f_y] == 0:
#                 if arr[f_x][f_y] == 0:
#                     queue.append([f_x, f_y])
#                     visited_coast[f_x][f_y] = 1
#                 if arr[f_x][f_y] >= 1:
#                     coast.append([f_x, f_y, arr[f_x][f_y]])
#                     visited_coast[f_x][f_y] = 1
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
#
# def finding_bridge(land1, land2):
#     land1_i, land1_j, land1_num = land1
#     land2_i, land2_j, land2_num = land2
#     visited = [[-1] * N for ___ in range(N)]
#
#     queue = deque()
#     queue.append([land1_i, land1_j])
#     visited[land1_i][land1_j] = 0
#
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == -1:
#                 if arr[x][y] == 0:
#                     queue.append([x, y])
#                     visited[x][y] = visited[s_i][s_j] + 1
#                 if x == land2_i and y == land2_j:
#                     return visited[s_i][s_j]
#     return math.inf
#
#
# N = int(input())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# visited_marking = [[0]*N for __ in range(N)]
# visited_coast = [[0]*N for __ in range(N)]
#
# marking_num = 0
# coast = []
# bridge_min = math.inf
# lands = []
# queue = deque()
#
# for i in range(N):
#     for j in range(N):
#         if visited_marking[i][j] == 0 and arr[i][j] == 1:
#             marking_num += 1
#             marking_island(i,j, marking_num)
#             queue.clear()
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 0 and visited_coast[i][j] == 0:
#             finding_coast(i,j)
#             queue.clear()
#
# for land1, land2 in combinations1(coast, 2):
#     if land1[2] == land2[2]:
#         continue
#     else:
#         lands.append([land1, land2])
#
# for land1, land2 in lands:
#     bridge = finding_bridge(land1, land2)
#     queue.clear()
#     if bridge < bridge_min:
#         bridge_min = bridge
# print(bridge_min)

# v4
# from collections import deque
# import math, sys
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# def marking_island(m_i, m_j, marking_num):
#     queue.append([m_i, m_j])
#     visited2[m_i][m_j] = 1
#     arr[m_i][m_j] = marking_num
#
#     while queue:
#         m_i, m_j = queue.popleft()
#         for m in range(4):
#             m_x = m_i + dx[m]
#             m_y = m_j + dy[m]
#             if 0 <= m_x < N and 0 <= m_y < N:
#                 if arr[m_x][m_y] != 0 and visited2[m_x][m_y] == 0:
#                     queue.append([m_x, m_y])
#                     visited2[m_x][m_y] = 1
#                     arr[m_x][m_y] = marking_num
#     queue.clear()
#
#
# def finding_coast(f_i, f_j):
#     queue = deque()
#     queue.append([f_i, f_j])
#     visited2[f_i][f_j] = 1
#
#     while queue:
#         f_i, f_j = queue.popleft()
#         for f in range(4):
#             f_x = f_i + dx[f]
#             f_y = f_j + dy[f]
#             if 0 <= f_x < N and 0 <= f_y < N and visited2[f_x][f_y] == 0:
#                 if arr[f_x][f_y] == 0:
#                     queue.append([f_x, f_y])
#                     visited2[f_x][f_y] = 1
#                 if arr[f_x][f_y] >= 1:
#                     coast.append([f_x, f_y, arr[f_x][f_y]])
#                     visited2[f_x][f_y] = 1
#     queue.clear()
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
#
# def finding_bridge(land1, land2, bridge_min):
#     land1_i, land1_j, land1_num = land1
#     land2_i, land2_j, land2_num = land2
#
#
#     queue.append([land1_i, land1_j])
#     visited[land1_i][land1_j] = 0
#     far = True
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == -1:
#                 if arr[x][y] == 0:
#                     queue.append([x, y])
#                     visited[x][y] = visited[s_i][s_j] + 1
#                     if visited[x][y] > bridge_min:
#                         queue.clear()
#                         return far, math.inf
#                 if x == land2_i and y == land2_j:
#                     far = False
#                     queue.clear()
#                     return far, visited[s_i][s_j]
#     queue.clear()
#     return far, math.inf
#
#
# N = int(input())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# # visited_coast = [[0]*N for __ in range(N)]
# marking_num = 0
# coast = []
# bridge_min = math.inf
# queue = deque()
# lands = []
# trg = False
# visited2 = [[0]*N for __ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if visited2[i][j] == 0 and arr[i][j] == 1:
#             marking_num += 1
#             marking_island(i,j, marking_num)
#
# visited2 = [[0]*N for __ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 0 and visited2[i][j] == 0:
#             finding_coast(i,j)
#
#
# for land1, land2 in combinations1(coast, 2):
#     if land1[2] == land2[2]:
#         continue
#     else:
#         lands.append([land1, land2])
#
# for land1, land2 in lands:
#     visited = [[-1] * N for ___ in range(N)]
#     trg, bridge = finding_bridge(land1, land2, bridge_min)
#     if trg:
#         continue
#     else:
#         if bridge < bridge_min:
#             bridge_min = bridge
# print(bridge_min)


# v5
# from collections import deque
# import math, sys
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# def finding_coast(f_i, f_j, marking_num):
#     queue = deque()
#     queue.append([f_i, f_j])
#     visited2[f_i][f_j] = 1
#
#     while queue:
#         f_i, f_j = queue.popleft()
#         for f in range(4):
#             f_x = f_i + dx[f]
#             f_y = f_j + dy[f]
#             if 0 <= f_x < N and 0 <= f_y < N and visited2[f_x][f_y] == 0:
#                 if arr[f_x][f_y] == 0:
#                     coast.append([f_i, f_j, marking_num])
#                 if arr[f_x][f_y] >= 1:
#                     visited2[f_x][f_y] = 1
#                     queue.append([f_x, f_y])
#     queue.clear()
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 if arr[i][2] == next[0][2]:
#                     continue
#                 else:
#                     yield [arr[i]] + next
#
#
# def finding_bridge(land1, land2, bridge_min):
#     land1_i, land1_j, land1_num = land1
#     land2_i, land2_j, land2_num = land2
#     visited = [[-1] * N for ___ in range(N)]
#
#     queue.append([land1_i, land1_j])
#     visited[land1_i][land1_j] = 0
#     far = True
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == -1:
#                 if arr[x][y] == 0:
#                     visited[x][y] = visited[s_i][s_j] + 1
#                     queue.append([x, y])
#                     if visited[x][y] > bridge_min:
#                         queue.clear()
#                         return far, math.inf
#                 if x == land2_i and y == land2_j:
#                     far = False
#                     queue.clear()
#                     return far, visited[s_i][s_j]
#     queue.clear()
#     return far, math.inf
#
#
# N = int(input())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# coast = []
# bridge_min = math.inf
# queue = deque()
# lands = []
# trg = False
#
# visited2 = [[0]*N for __ in range(N)]
# marking_num = 0
# for i in range(N):
#     for j in range(N):
#         if visited2[i][j] == 0 and arr[i][j] == 1:
#             marking_num += 1
#             finding_coast(i,j, marking_num)
#
# for land1, land2 in combinations1(coast, 2):
#     trg, bridge = finding_bridge(land1, land2, bridge_min)
#     if trg:
#         continue
#     else:
#         if bridge < bridge_min:
#             bridge_min = bridge
# print(bridge_min)

# v6
from collections import deque, defaultdict
import math, sys

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def finding_coast(f_i, f_j, marking_num):
    queue_c = deque()
    queue_c.append([f_i, f_j])
    visited2[f_i][f_j] = 1

    while queue_c:
        f_i, f_j = queue_c.popleft()
        for f in range(4):
            f_x = f_i + dx[f]
            f_y = f_j + dy[f]
            if 0 <= f_x < N and 0 <= f_y < N and visited2[f_x][f_y] == 0:
                if arr[f_x][f_y] == 0 and [f_i, f_j] not in coast[marking_num]:
                    coast[marking_num].append([f_i, f_j])
                    # visited2[f_x][f_y] = 1
                if arr[f_x][f_y] == 1:
                    visited2[f_x][f_y] = 1
                    queue_c.append([f_x, f_y])


def finding_bridge(island_num):
    visited = [[-1] * N for ___ in range(N)]
    queue_b = deque()
    for land in coast[island_num]:
        queue_b.append(land)
        visited[land[0]][land[1]] = 0
    bridge = math.inf

    while queue_b:
        s_i, s_j = queue_b.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < N and visited[x][y] == -1:
                if arr[x][y] == 0:
                    visited[x][y] = visited[s_i][s_j] + 1
                    queue_b.append([x, y])
                if arr[x][y] == 1 and [x,y] not in coast[island_num] and visited[s_i][s_j] != 0:
                    bridge = min(visited[s_i][s_j], bridge)
    return bridge

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

coast = defaultdict(list)
bridge_min = math.inf
lands = []

visited2 = [[0]*N for __ in range(N)]
marking_num = 0
for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0 and arr[i][j] == 1:
            marking_num += 1
            finding_coast(i,j, marking_num)

for island_num in range(1, marking_num+1):
    bridge = finding_bridge(island_num)
    if bridge < bridge_min:
        bridge_min = bridge

print(bridge_min)

