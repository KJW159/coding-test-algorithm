# baekjoon_16234  인구이동

# v1
import collections


def bfs(s_i, s_j):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    union = []
    population = countries[s_i][s_j]
    queue = collections.deque()

    queue.append([s_i, s_j])
    visited[s_i][s_j] = 1
    union.append([s_i, s_j])
    move = False

    while queue:
        c_i, c_j = queue.popleft()

        for c in range(4):
            x = c_i + dx[c]
            y = c_j + dy[c]
            if 0 <= x < N and 0 <= y < N:
                if visited[x][y] == 0:
                    if L <= abs(countries[c_i][c_j]-countries[x][y]) <= R:
                        move = True
                        population += countries[x][y]
                        union.append([x,y])
                        queue.append([x,y])
                        visited[x][y] = 1

    union_population = population // len(union)

    for u1, u2 in union:
        countries[u1][u2] = union_population

    # if len(union)>0:
    #     move = True
    return move


N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]


cnt = 0

while True:
    visited = [[0] * N for __ in range(N)]
    trg = True
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                moves = bfs(i,j)
                if moves:
                    trg = False

    if trg:
        break
    cnt += 1
print(cnt)


# v2
# import collections
#
#
# def bfs(s_i, s_j):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#
#     union = []
#     population = countries[s_i][s_j]
#     queue = collections.deque()
#
#     queue.append([s_i, s_j])
#     visited[s_i][s_j] = 1
#     union.append([s_i, s_j])
#     move = False
#
#     while queue:
#         c_i, c_j = queue.popleft()
#
#         for c in range(4):
#             x = c_i + dx[c]
#             y = c_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == 0:
#                 if L <= abs(countries[c_i][c_j]-countries[x][y]) <= R:
#                     move = True
#                     population += countries[x][y]
#                     union.append([x,y])
#                     queue.append([x,y])
#                     visited[x][y] = 1
#
#     union_population = population // len(union)
#
#     for u1,u2 in union:
#         countries[u1][u2] = union_population
#
#     return move
#
# def check_population(i_x,j_y):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#     for k in range(4):
#         x = i_x + dx[k]
#         y = j_y + dy[k]
#         if 0 <= x < N and 0 <= y < N:
#             if L <= abs(countries[i_x][j_y] - countries[x][y]) <= R:
#                 return 0
#     return 1
#
# N, L, R = map(int, input().split())
# countries = [list(map(int, input().split())) for _ in range(N)]
#
#
# cnt = 0
#
# while True:
#     visited = [[0] * N for __ in range(N)]
#     trg = True
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 1 or check_population(i,j):
#                 continue
#             moves = bfs(i,j)
#             if moves:
#                 trg = False
#     if trg:
#         break
#     cnt += 1
# print(cnt)