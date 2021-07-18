# baekjoon_2887 행성 터널

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
# planets = [list(map(int, input().split())) for _ in range(N)]
# parents = [i for i in range(N)]
# edges = []
# res = 0
#
# for i in range(N):
#     for j in range(i+1, N):
#         x1, y1, z1 = planets[i]
#         x2, y2, z2 = planets[j]
#         distance = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
#         edges.append([i, j, distance])
#
# edges.sort(key=lambda x: x[2])
#
# for edge in edges:
#     a, b, cost = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a,b)
#         res += cost
#
# print(res)

# v2
# from itertools import combinations
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
# N = int(input())
# planets = []
# parents = [i for i in range(N)]
# edges = []
# res = 0
#
# for i in range(N):
#     planet = [i]
#     tmp = list(map(int, input().split()))
#     planet.extend(tmp)
#     planets.append(planet)
#
#
# for p1, p2 in combinations(planets, 2):
#     n1, x1, y1, z1 = p1
#     n2, x2, y2, z2 = p2
#     distance = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
#     edges.append([n1, n2, distance])
#
# edges.sort(key=lambda x: x[2])
#
# for edge in edges:
#     a, b, cost = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res += cost
#
# print(res)


# v3
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
# N = int(input())
# planets_x = []
# planets_y = []
# planets_z = []
#
#
# parents = [i for i in range(N)]
# edges = []
# res = 0
#
# for i in range(N):
#     x, y, z = list(map(int, input().split()))
#     planets_x.append([i, x])
#     planets_y.append([i, y])
#     planets_z.append([i, z])
#
# planets_x.sort(key=lambda x:x[1])
# planets_y.sort(key=lambda x:x[1])
# planets_z.sort(key=lambda x:x[1])
#
# for i in range(N-1):
#     n1, x1 = planets_x[i]
#     n2, x2 = planets_x[i+1]
#     distance = abs(x1-x2)
#     edges.append([n1,n2,distance])
#
# for i in range(N-1):
#     n1, y1 = planets_y[i]
#     n2, y2 = planets_y[i+1]
#     distance = abs(y1-y2)
#     edges.append([n1,n2,distance])
#
# for i in range(N-1):
#     n1, z1 = planets_z[i]
#     n2, z2 = planets_z[i+1]
#     distance = abs(z1-z2)
#     edges.append([n1,n2,distance])
#
# edges.sort(key=lambda x: x[2])
#
# for edge in edges:
#     a, b, cost = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res += cost
#
# print(res)

# v4
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
# N = int(input())
# planets = []
#
# parents = [i for i in range(N)]
# edges = []
# res = 0
#
# for i in range(N):
#     x, y, z = list(map(int, input().split()))
#     planets.append([x, y, z, i])
#
# for i in range(3):
#     planets.sort(key=lambda x:x[i])
#     for j in range(N-1):
#         distance = abs(planets[j][i]-planets[j+1][i])
#         edges.append([planets[j][3], planets[j+1][3], distance])
#
# edges.sort(key=lambda x: x[2])
#
# for edge in edges:
#     a, b, cost = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res += cost
#
# print(res)

# v5
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
# N = int(input())
# planets = []
#
# parents = [i for i in range(N)]
# edges = []
# res = 0
#
# for i in range(N):
#     x, y, z = list(map(int, input().split()))
#     planets.append([x, y, z, i])
#
# for i in range(3):
#     planets.sort(key=lambda x: x[i])
#     for j in range(N-1):
#         distance = abs(planets[j][i]-planets[j+1][i])
#         edges.append([distance, planets[j][3], planets[j+1][3]])
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res += cost
# print(res)

# v6
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
planets_x = []
planets_y = []
planets_z = []


parents = [i for i in range(N)]
edges = []
res = 0

for i in range(N):
    x, y, z = list(map(int, input().split()))
    planets_x.append([i, x])
    planets_y.append([i, y])
    planets_z.append([i, z])

planets_x.sort(key=lambda x:x[1])
planets_y.sort(key=lambda x:x[1])
planets_z.sort(key=lambda x:x[1])

for i in range(N-1):
    distance = abs(planets_x[i][1] - planets_x[i+1][1])
    edges.append([planets_x[i][0],planets_x[i+1][0],distance])


for i in range(N-1):
    distance = abs(planets_y[i][1] - planets_y[i+1][1])
    edges.append([planets_y[i][0], planets_y[i+1][0], distance])

for i in range(N-1):
    distance = abs(planets_z[i][1] - planets_z[i+1][1])
    edges.append([planets_z[i][0],planets_z[i+1][0],distance])

edges.sort(key=lambda x:x[2])

for edge in edges:
    a, b, cost = edge
    if finding_parents(parents, a) != finding_parents(parents, b):
        union_parents(a, b)
        res += cost

print(res)