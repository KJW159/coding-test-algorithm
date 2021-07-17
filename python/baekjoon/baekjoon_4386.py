# baekjoon_4386 별자리 만들기

# v1
# from itertools import combinations
# import math
#
#
# def calculating_distance(x1,y1,x2,y2):
#     tmp = pow((x1-x2), 2) + pow((y1-y2),2)
#     distance = math.sqrt(tmp)
#     return distance
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
# n = int(input())
#
# parents = [0]*(n+1)
# stars = []
# edges = []
# res = 0
#
# for i in range(n):
#     star = [i+1]
#     position = list(map(float, input().split()))
#     star.extend(position)
#     stars.append(star)
#
# for s1, s2 in combinations(stars, 2):
#     num1, x1, y1 = s1
#     num2, x2, y2 = s2
#     distance = calculating_distance(x1,y1,x2,y2 )
#     edges.append([num1, num2, distance])
#
#
# for i in range(1, n+1):
#     parents[i] = i
#
# edges.sort(key=lambda x:x[2])
#
# for edge in edges:
#     a, b, cost = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a, b)
#         res += cost
#
# print("{:.2f}".format(res))


# v2
import math

def calculating_distance(x1,y1,x2,y2):
    tmp = pow((x1-x2), 2) + pow((y1-y2),2)
    distance = math.sqrt(tmp)
    return distance

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


n = int(input())

parents = [0]*(n+1)
edges = []
res = 0
stars = [list(map(float, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        distance = calculating_distance(x1,y1,x2,y2 )
        edges.append([i, j, distance])

for i in range(1, n+1):
    parents[i] = i

edges.sort(key=lambda x:x[2])

for edge in edges:
    a, b, cost = edge
    if finding_parents(parents, a) != finding_parents(parents, b):
        union_parents(a, b)
        res += cost

print("{:.2f}".format(res))




