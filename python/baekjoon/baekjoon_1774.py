# baekjoon_1774 우주신과의 교감.

# v1
# import math
#
#
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
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
# N, M = map(int, input().split())
# res = 0
# edges = []
# parents = [i for i in range(N+1)]
#
# planets = []
# for i in range(1, N+1):
#     x, y = map(int, input().split())
#     planets.append([i, x, y])
#
# for i in range(N):
#     for j in range(i+1, N):
#         distance = math.sqrt(math.pow(planets[i][1]-planets[j][1],2) + math.pow(planets[i][2]-planets[j][2],2))
#         edges.append([planets[i][0], planets[j][0], distance])
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     if a < b:
#         parents[b] = a
#     else:
#         parents[a] = b
#
# edges.sort(key=lambda x: x[2])
# for edge in edges:
#     a, b, distance = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res += distance
#
# print("{:.2f}".format(res))




# v2
# import math
#
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
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
# N, M = map(int, input().split())
# res = 0
# edges = []
# parents = [i for i in range(N+1)]
#
# planets = []
# for i in range(1, N+1):
#     x, y = map(int, input().split())
#     planets.append([i, x, y])
#
# for i in range(N):
#     for j in range(i+1, N):
#         distance = math.sqrt(math.pow(planets[i][1]-planets[j][1],2) + math.pow(planets[i][2]-planets[j][2],2))
#         edges.append([planets[i][0], planets[j][0], distance])
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#
# edges.sort(key=lambda x: x[2])
# for edge in edges:
#     a, b, distance = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res += distance
#
# print("{:.2f}".format(res))


# v3
import math

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
res = 0
edges = []
parents = [i for i in range(N+1)]

planets = []
for i in range(1, N+1):
    x, y = map(int, input().split())
    planets.append([i, x, y])

for i in range(N):
    for j in range(i+1, N):
        distance = math.sqrt(math.pow(planets[i][1]-planets[j][1],2) + math.pow(planets[i][2]-planets[j][2],2))
        edges.append([planets[i][0], planets[j][0], distance])

for _ in range(M):
    a, b = map(int, input().split())
    if finding_parents(parents, a) != finding_parents(parents, b):
        union_parents(a, b)

edges.sort(key=lambda x: x[2])
for edge in edges:
    a, b, distance = edge
    if finding_parents(parents, a) != finding_parents(parents, b):
        union_parents(a, b)
        res += distance

print("{:.2f}".format(res))



