# baekjoon_1647 도시 분할 계획

# v1
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(x, y):
#     p_x = parents[x]
#     p_y = parents[y]
#
#     if p_x < p_y:
#         parents[p_y] = p_x
#     else:
#         parents[p_x] = p_y
#
# def kruskal():
#     edges.sort()
#     last_cost = 0
#     res_tmp = 0
#
#     for edge in edges:
#         c, a, b = edge
#         if finding_parents(parents, a) != finding_parents(parents, b):
#             union_parents(a, b)
#             res_tmp += c
#             last_cost = c
#
#     res_tmp -= last_cost
#     return res_tmp
#
#
#
# N, M = map(int, input().split())
# parents = [0]*(N+1)
# edges = []
#
# for i in range(1, N+1):
#     parents[i] = i
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     edges.append([c,a,b])
#
# res = kruskal()
# print(res)


# v2
# import sys
#
# input = sys.stdin.readline
#
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(x, y):
#     p_x = parents[x]
#     p_y = parents[y]
#
#     if p_x < p_y:
#         parents[p_y] = p_x
#     else:
#         parents[p_x] = p_y
#
# def kruskal():
#     edges.sort()
#     last_cost = 0
#     res_tmp = 0
#
#     for edge in edges:
#         c, a, b = edge
#         if finding_parents(parents, a) != finding_parents(parents, b):
#             union_parents(a, b)
#             res_tmp += c
#             last_cost = c
#
#     res_tmp -= last_cost
#     return res_tmp
#
#
#
# N, M = map(int, input().split())
# parents = [0]*(N+1)
# edges = []
#
# for i in range(1, N+1):
#     parents[i] = i
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     edges.append([c,a,b])
#
# res = kruskal()
# print(res)

# v3
# import sys
#
# input = sys.stdin.readline
#
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(x, y):
#     p_x = parents[x]
#     p_y = parents[y]
#
#     if p_x < p_y:
#         parents[p_y] = p_x
#     else:
#         parents[p_x] = p_y
#
# def kruskal():
#     edges.sort()
#     road_nums = 0
#     res_tmp = 0
#
#     for edge in edges:
#         c, a, b = edge
#         if finding_parents(parents, a) != finding_parents(parents, b):
#             union_parents(a, b)
#             res_tmp += c
#             road_nums += 1
#             if road_nums == N-2:
#                 return res_tmp
#
#     return res_tmp
#
#
# N, M = map(int, input().split())
# parents = [0]*(N+1)
# edges = []
#
# for i in range(1, N+1):
#     parents[i] = i
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     edges.append([c,a,b])
#
# res = kruskal()
# print(res)


# v4
import sys

input = sys.stdin.readline

def finding_parents(parents, x):
    if parents[x] != x:
        parents[x] = finding_parents(parents, parents[x])
    return parents[x]

def union_parents(x, y):
    p_x = parents[x]
    p_y = parents[y]

    if p_x < p_y:
        parents[p_y] = p_x
    else:
        parents[p_x] = p_y

N, M = map(int, input().split())
parents = [0]*(N+1)
edges = []

for i in range(1, N+1):
    parents[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([c,a,b])

edges.sort()
road_nums = 0
res = 0

for edge in edges:
    c, a, b = edge
    if finding_parents(parents, a) != finding_parents(parents, b):
        union_parents(a, b)
        res += c
        road_nums += 1
        if road_nums == N-2:
            break

print(res)