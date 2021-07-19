# baekjoon_6497 전력난

# v1
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(x, y):
#     p_x = parents[x]
#     p_y = parents[y]
#     if p_x < p_y:
#         parents[p_y] = p_x
#     else:
#         parents[p_x] = p_y
#
#
# m, n = map(int, input().split())
# parents = [i for i in range(m)]
# edges = []
# res = 0
# while True:
#     edge = list(map(int, input().split()))
#     if len(edge) == 2:
#         break
#     edges.append([edge[2], edge[0], edge[1]])
#     res += edge[2]
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res -= cost
#
# print(res)


# v2
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(x, y):
#     p_x = parents[x]
#     p_y = parents[y]
#     if p_x < p_y:
#         parents[p_y] = p_x
#     else:
#         parents[p_x] = p_y
#
#
# m, n = map(int, input().split())
# parents = [i for i in range(m)]
# edges = []
# res = 0
# while True:
#     edge = list(map(int, input().split()))
#     if len(edge) == 2:
#         break
#     if edge[2] <= 0:
#         continue
#     edges.append([edge[2], edge[0], edge[1]])
#     res += edge[2]
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res -= cost
#
# print(res)

# v3
# import sys
#
# input = sys.stdin.readline
#
#
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(x, y):
#     p_x = parents[x]
#     p_y = parents[y]
#     if p_x < p_y:
#         parents[p_y] = p_x
#     else:
#         parents[p_x] = p_y
#
#
# while True:
#     m, n = map(int, input().split())
#     if m == 0 and n == 0:
#         break
#     parents = [i for i in range(m)]
#     edges = []
#     res = 0
#     for _ in range(n):
#         edge = list(map(int, input().split()))
#         edges.append([edge[2], edge[0], edge[1]])
#         res += edge[2]
#     edges.sort()
#
#     for edge in edges:
#         cost, a, b = edge
#         if finding_parents(parents, a) != finding_parents(parents, b):
#             union_parents(a, b)
#             res -= cost
#     print(res)

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


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parents = [i for i in range(m)]
    edges = []
    res = 0
    for _ in range(n):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        a, b, cost = edge
        if finding_parents(parents, a) != finding_parents(parents, b):
            union_parents(a, b)
        else:
            res += cost
    print(res)