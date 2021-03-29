# baekjoon_16235 나무 재테크

# v1
# import math
#
# def spring():
#     dead = []
#     for i in range(N):
#         for j in range(N):
#             if trees[i][j]:
#                 trees[i][j].sort()
#                 lives = []
#                 for t in range(len(trees[i][j])):
#                     if (land[i][j] - trees[i][j][t]) >= 0:
#                         age = trees[i][j][t]
#                         land[i][j] -= age
#                         age += 1
#                         lives.append(age)
#                         continue
#                     dead.append([i,j,trees[i][j][t]])
#                 trees[i][j] = lives
#     return dead
#
#
# def summer(dead):
#     for tree_d in dead:
#         i, j, age = tree_d
#         land[i][j] += math.ceil(age / 2)
#
# def fall():
#     for i in range(N):
#         for j in range(N):
#             if trees[i][j]:
#                 for tree in trees[i][j]:
#                     if tree % 5 == 0:
#                         for c in range(8):
#                             nx = i + dx[c]
#                             ny = j + dy[c]
#                             if 0 <= nx < N and 0 <= ny < N:
#                                 trees[nx][ny].append(1)
#
# def winnter():
#     for i in range(N):
#         for j in range(N):
#             if A[i][j]:
#                 land[i][j] += A[i][j]
#
# N, M, K = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# land = [[5]*N for _ in range(N)]
# trees = [[[] for _ in range(N)] for __ in range(N)]
#
# dx = [-1,-1,-1,0,0,1,1,1]
# dy = [-1,0,1,-1,1,-1,0,1]
# res = 0
#
# for _ in range(M):
#     x,y,z = map(int, input().split())
#     trees[x-1][y-1].append(z)
#
#
# for k in range(K):
#     dead = spring()
#     summer(dead)
#     fall()
#     winnter()
#
# for i in range(N):
#     for j in range(N):
#         if trees[i][j]:
#             res += len(trees[i][j])
# print(res)


# v2
# def spring():
#     for i in range(N):
#         for j in range(N):
#             if trees[i][j]:
#                 trees[i][j].sort()
#                 for t in range(len(trees[i][j])):
#                     if (land[i][j] - trees[i][j][t]) >= 0:
#                         land[i][j] -= trees[i][j][t]
#                         trees[i][j][t] += 1
#                     else:
#                         for __ in range(t, len(trees[i][j])):
#                             land[i][j] += (trees[i][j].pop() // 2)
#                         break
#
#
# def fall():
#     for i in range(N):
#         for j in range(N):
#             if trees[i][j]:
#                 for tree in trees[i][j]:
#                     if tree % 5 == 0:
#                         for c in range(8):
#                             nx = i + dx[c]
#                             ny = j + dy[c]
#                             if 0 <= nx < N and 0 <= ny < N:
#                                 trees[nx][ny].append(1)
#
# def winnter():
#     for i in range(N):
#         for j in range(N):
#             if A[i][j]:
#                 land[i][j] += A[i][j]
#
# N, M, K = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# land = [[5]*N for _ in range(N)]
# trees = [[[] for _ in range(N)] for __ in range(N)]
#
# dx = [-1,-1,-1,0,0,1,1,1]
# dy = [-1,0,1,-1,1,-1,0,1]
# res = 0
#
# for _ in range(M):
#     x,y,z = map(int, input().split())
#     trees[x-1][y-1].append(z)
#
#
# for k in range(K):
#     spring()
#     fall()
#     winnter()
#
# for i in range(N):
#     for j in range(N):
#         if trees[i][j]:
#             res += len(trees[i][j])
# print(res)

# v3
# def spring():
#     dead = []
#     for i in range(N):
#         for j in range(N):
#             if trees[i][j]:
#                 trees[i][j].sort()
#                 lives = []
#                 for t in range(len(trees[i][j])):
#                     if (land[i][j] - trees[i][j][t]) >= 0:
#                         age = trees[i][j][t]
#                         land[i][j] -= age
#                         age += 1
#                         lives.append(age)
#                         continue
#                     dead.append([i,j,trees[i][j][t]])
#                 trees[i][j] = lives
#     return dead
#
#
# def summer(dead):
#     for tree_d in dead:
#         i, j, age = tree_d
#         land[i][j] += age // 2
#
# def fall():
#     for i in range(N):
#         for j in range(N):
#             if trees[i][j]:
#                 for tree in trees[i][j]:
#                     if tree % 5 == 0:
#                         for c in range(8):
#                             nx = i + dx[c]
#                             ny = j + dy[c]
#                             if 0 <= nx < N and 0 <= ny < N:
#                                 trees[nx][ny].append(1)
#
# def winnter():
#     for i in range(N):
#         for j in range(N):
#             if A[i][j]:
#                 land[i][j] += A[i][j]
#
# N, M, K = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# land = [[5]*N for _ in range(N)]
# trees = [[[] for _ in range(N)] for __ in range(N)]
#
# dx = [-1,-1,-1,0,0,1,1,1]
# dy = [-1,0,1,-1,1,-1,0,1]
# res = 0
#
# for _ in range(M):
#     x,y,z = map(int, input().split())
#     trees[x-1][y-1].append(z)
#
#
# for k in range(K):
#     dead = spring()
#     summer(dead)
#     fall()
#     winnter()
#
# for i in range(N):
#     for j in range(N):
#         if trees[i][j]:
#             res += len(trees[i][j])
# print(res)


# v4
# def spring():
#     dead = []
#     for i in range(N):
#         for j in range(N):
#             if trees[i][j]:
#                 trees[i][j].sort()
#                 lives = []
#                 for t in range(len(trees[i][j])):
#                     if (land[i][j] - trees[i][j][t]) >= 0:
#                         age = trees[i][j][t]
#                         land[i][j] -= age
#                         age += 1
#                         lives.append(age)
#                         continue
#                     dead.append([i,j,trees[i][j][t]])
#                 trees[i][j] = lives
#     return dead
#
#
# def summer(dead):
#     for tree_d in dead:
#         i, j, age = tree_d
#         land[i][j] += age // 2
#
# def fall():
#     for i in range(N):
#         for j in range(N):
#             if trees[i][j]:
#                 for tree in trees[i][j]:
#                     if tree % 5 == 0:
#                         for c in range(8):
#                             nx = i + dx[c]
#                             ny = j + dy[c]
#                             if 0 <= nx < N and 0 <= ny < N:
#                                 trees[nx][ny].append(1)
#             # winter
#             if A[i][j]:
#                 land[i][j] += A[i][j]
#
# N, M, K = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# land = [[5]*N for _ in range(N)]
# trees = [[[] for _ in range(N)] for __ in range(N)]
#
# dx = [-1,-1,-1,0,0,1,1,1]
# dy = [-1,0,1,-1,1,-1,0,1]
# res = 0
#
# for _ in range(M):
#     x,y,z = map(int, input().split())
#     trees[x-1][y-1].append(z)
#
#
# for k in range(K):
#     dead = spring()
#     summer(dead)
#     fall()
#
# for i in range(N):
#     for j in range(N):
#         if trees[i][j]:
#             res += len(trees[i][j])
# print(res)

# v5
def spring():
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                trees[i][j].sort()
                trees_num = len(trees[i][j])
                for t in range(trees_num):
                    if (land[i][j] - trees[i][j][t]) >= 0:
                        land[i][j] -= trees[i][j][t]
                        trees[i][j][t] += 1
                        continue
                    # summer
                    for _ in range(t, trees_num):
                        land[i][j] += trees[i][j].pop() // 2
                    break

def fall():
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                for tree in trees[i][j]:
                    if tree % 5 == 0:
                        for c in range(8):
                            nx = i + dx[c]
                            ny = j + dy[c]
                            if 0 <= nx < N and 0 <= ny < N:
                                trees[nx][ny].append(1)
            # winter
            if A[i][j]:
                land[i][j] += A[i][j]

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
land = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for __ in range(N)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
res = 0

for _ in range(M):
    x,y,z = map(int, input().split())
    trees[x-1][y-1].append(z)


for k in range(K):
    spring()
    fall()

for i in range(N):
    for j in range(N):
        if trees[i][j]:
            res += len(trees[i][j])
print(res)