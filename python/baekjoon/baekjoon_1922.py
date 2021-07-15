# baekjoon_1922 네트워크 연결

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
# N = int(input())
# M = int(input())
#
# res = 0
# parents = [0]*(N+1)
# edges = []
#
# for i in range(1, N+1):
#     parents[i] = i
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     if a != b:
#         edges.append([c,a,b])
#
# edges.sort()
#
# for edge in edges:
#     c, a, b = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a ,b)
#         res += c
#
# print(res)

# v2
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


N = int(input())
M = int(input())

res = 0
parents = [0]*(N+1)
edges = []

for i in range(1, N+1):
    parents[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    if a != b:
        edges.append([c,a,b])

edges.sort()

for edge in edges:
    c, a, b = edge
    if finding_parents(parents, a) != finding_parents(parents, b):
        union_parents(a ,b)
        res += c

print(res)