# baekjoon_6593 상범 빌딩


# v1
# from collections import deque
#
# # 상, 하, 서, 북, 동, 남
# # dz, dx, dy
# dzdxdy = [[1,0,0],[-1,0,0],[0,0,-1],[0,-1,0],[0,0,1],[0,1,0]]
#
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start[0]][start[1]][start[2]] = 0
#
#     while queue:
#         s_k, s_i, s_j = queue.popleft()
#         for c in range(6):
#             k = s_k + dzdxdy[c][0]
#             x = s_i + dzdxdy[c][1]
#             y = s_j + dzdxdy[c][2]
#             if 0 <= k < L and 0 <= x < R and 0 <= y < C:
#                 if visited[k][x][y] == -1 and building[k][x][y] != "#":
#                     queue.append([k, x, y])
#                     visited[k][x][y] = visited[s_k][s_i][s_j] + 1
#                     if building[k][x][y] == "E":
#                         return visited[k][x][y]
#     return -1
#
#
# while True:
#     L, R, C = map(int, input().split())
#     if L == 0 and R == 0 and C == 0:
#         break
#     building = [[] for _ in range(L)]
#     start = []
#     end = []
#     visited = [[[-1]*C for _ in range(R)] for __ in range(L)]
#
#     for k in range(L):
#         for i in range(R+1):
#             tmp = list(input())
#             if not tmp:
#                 continue
#             building[k].append(tmp)
#             for j in range(C):
#                 if tmp[j] == "S":
#                     start = [i, j, k]
#                 if tmp[j] == "E":
#                     end = [i, j, k]
#
#     res = bfs(start)
#     if res == -1:
#         print("Trapped!")
#     else:
#         print("Escaped in {} minute(s).".format(res))

# v2
from collections import deque

# 상, 하, 서, 북, 동, 남
# dz, dx, dy
dzdxdy = [[1,0,0],[-1,0,0],[0,0,-1],[0,-1,0],[0,0,1],[0,1,0]]


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]][start[2]] = 0

    while queue:
        s_k, s_i, s_j = queue.popleft()
        for c in range(6):
            k = s_k + dzdxdy[c][0]
            x = s_i + dzdxdy[c][1]
            y = s_j + dzdxdy[c][2]
            if 0 <= k < L and 0 <= x < R and 0 <= y < C:
                if visited[k][x][y] == -1 and building[k][x][y] != "#":
                    queue.append([k, x, y])
                    visited[k][x][y] = visited[s_k][s_i][s_j] + 1
                    if building[k][x][y] == "E":
                        return visited[k][x][y]
    return -1


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    building = [[] for _ in range(L)]
    start = []
    end = []
    visited = [[[-1]*C for _ in range(R)] for __ in range(L)]

    for k in range(L):
        for i in range(R+1):
            tmp = list(input())
            if not tmp:
                continue
            building[k].append(tmp)
            for j in range(C):
                if tmp[j] == "S":
                    start = [k, i, j]
                if tmp[j] == "E":
                    end = [k, i, j]

    res = bfs(start)
    if res == -1:
        print("Trapped!")
    else:
        print("Escaped in {} minute(s).".format(res))