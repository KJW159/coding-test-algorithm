# baekjoon_13418 학교 탐방하기.

# v1
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(parents,x,y):
#     p_x = parents[x]
#     p_y = parents[y]
#
#     if p_x < p_y:
#         parents[p_y] = p_x
#     else:
#         parents[p_x] = p_y
#
#
# def kruskal():
#     parents = [i for i in range(N+1)]
#     res_tmp = 0
#     cnt = 0
#
#     for edge in edges:
#         a, b, c = edge
#         if finding_parents(parents, a) != finding_parents(parents, b):
#             union_parents(parents, a, b)
#             res_tmp += 1
#             cnt += 1
#             if cnt >= N:
#                 break
#     return res_tmp
#
#
# N, M = map(int, input().split())
# edges = [list(map(int, input().split()))]
# edges_tmp = []
# res = [0,0]
# for _ in range(M):
#     edges_tmp.append(list(map(int, input().split())))
#
# for i in range(2):
#     if i == 0:
#         edges_tmp.sort(key=lambda x: x[2])
#     else:
#         edges_tmp.sort(key=lambda x: -x[2])
#     print(edges_tmp)
#     edges.extend(edges_tmp)
#     print(edges)
#     tmp = kruskal()
#     print(tmp)
#     res[i] = tmp**2
#
# print(abs(res[0]-res[1]))

# v2
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(parents,x,y):
#     p_x = parents[x]
#     p_y = parents[y]
#
#     if p_x < p_y:
#         parents[p_y] = p_x
#     else:
#         parents[p_x] = p_y
#
#
# def kruskal():
#     parents = [i for i in range(N+1)]
#     res_tmp = 0
#     cnt = 0
#
#     for edge in edges:
#         a, b, c = edge
#         if finding_parents(parents, a) != finding_parents(parents, b):
#             union_parents(parents, a, b)
#             if c == 0:
#                 res_tmp += 1
#             cnt += 1
#             if cnt >= N:
#                 break
#     return res_tmp
#
#
# N, M = map(int, input().split())
# edge_first = list(map(int, input().split()))
# edges_tmp = []
# res = [0,0]
# for _ in range(M):
#     edges_tmp.append(list(map(int, input().split())))
#
# for i in range(2):
#     edges = []
#     edges.append(edge_first)
#     if i == 0:
#         edges_tmp.sort(key=lambda x: x[2])
#     else:
#         edges_tmp.sort(key=lambda x: -x[2])
#     edges.extend(edges_tmp)
#     tmp = kruskal()
#     res[i] = tmp**2
#
# print(abs(res[0]-res[1]))


# v3
import sys

input = sys.stdin.readline


def finding_parents(parents, x):
    if parents[x] != x:
        parents[x] = finding_parents(parents, parents[x])
    return parents[x]

def union_parents(parents,x,y):
    p_x = parents[x]
    p_y = parents[y]

    if p_x < p_y:
        parents[p_y] = p_x
    else:
        parents[p_x] = p_y


def kruskal():
    parents = [i for i in range(N+1)]
    res_tmp = 0
    cnt = 0

    for edge in edges:
        a, b, c = edge
        if finding_parents(parents, a) != finding_parents(parents, b):
            union_parents(parents, a, b)
            if c == 0:
                res_tmp += 1
            cnt += 1
            if cnt >= N:
                break
    return res_tmp


N, M = map(int, input().split())
edge_first = list(map(int, input().split()))
edges_tmp = []
res = [0,0]
for _ in range(M):
    edges_tmp.append(list(map(int, input().split())))

for i in range(2):
    edges = []
    edges.append(edge_first)
    if i == 0:
        edges_tmp.sort(key=lambda x: x[2])
    else:
        edges_tmp.sort(key=lambda x: -x[2])
    edges.extend(edges_tmp)
    tmp = kruskal()
    res[i] = tmp**2

print(abs(res[0]-res[1]))










