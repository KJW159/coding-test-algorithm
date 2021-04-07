# baekjoon_1197 최소 스패닝 트리


# v1

# def find_parents(parents, a):
#     if parents[a] != a:
#         parents[a] = find_parents(parents, parents[a])
#     return parents[a]
#
# def union_parents(parents, a,b):
#     a = find_parents(parents, a)
#     b = find_parents(parents, b)
#     if a < b:
#         parents[b] = a
#     else:
#         parents[a] = b
#
# V, E = map(int, input().split())
# parents = [0]*(V+1)
# edges =[]
# res = 0
#
# for _ in range(E):
#     a,b,c, = map(int, input().split())
#     edges.append([c,a,b])
#
# for i in range(1, V+1):
#     parents[i] = i
#
# edges.sort()
#
# for edge in edges:
#     c, a, b = edge
#     if find_parents(parents, a) != find_parents(parents, b):
#         union_parents(parents, a, b)
#         res += c
#
# print(res)

# v2
def find_parents(a):
    if parents[a] != a:
        parents[a] = find_parents(parents[a])
    return parents[a]

def union_parents(a,b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

V, E = map(int, input().split())
parents = [0]*(V+1)
edges =[]
res = 0

for _ in range(E):
    a,b,c, = map(int, input().split())
    edges.append([c,a,b])

for i in range(1, V+1):
    parents[i] = i

edges.sort()

for edge in edges:
    c, a, b = edge
    if find_parents(a) != find_parents(b):
        union_parents(a, b)
        res += c

print(res)
