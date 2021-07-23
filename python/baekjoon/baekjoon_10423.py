# baekjoon_10423 전기가 부족해

# v1
# def finding_parents(parents, x):
#     if parents[x] != x:
#         parents[x] = finding_parents(parents, parents[x])
#     return parents[x]
#
# def union_parents(x, y):
#     p_x = parents[x]
#     p_y = parents[y]
#     if power_stations[p_x] == 1 and power_stations[p_y] == 0:
#         parents[p_y] = p_x
#     elif power_stations[p_x] == 0 and power_stations[p_y] == 1:
#         parents[p_x] = p_y
#     elif power_stations[p_x] == 0 and power_stations[p_y] == 0:
#         if p_x < p_y:
#             parents[p_y] = p_x
#         else:
#             parents[p_x] = p_y
#     else:
#         return
#
#
# N, M, K = map(int, input().split())
# power_stations = [0]*(N+1)
# power_tmp = list(map(int, input().split()))
# parents = [i for i in range(N+1)]
# edges = []
# res = 0
#
# for station_num in power_tmp:
#     power_stations[station_num] = 1
#
# for _ in range(M):
#     u, v, w = map(int, input().split())
#     edges.append([w, u, v])
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if finding_parents(parents, a) != finding_parents(parents, b):
#         union_parents(a,b)
#         res += cost
# print(parents)
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
#     if power_stations[p_x] == 1 and power_stations[p_y] == 0:
#         parents[p_y] = p_x
#     elif power_stations[p_x] == 0 and power_stations[p_y] == 1:
#         parents[p_x] = p_y
#     elif power_stations[p_x] == 0 and power_stations[p_y] == 0:
#         if p_x < p_y:
#             parents[p_y] = p_x
#         else:
#             parents[p_x] = p_y
#     else:
#         return
#
#
# N, M, K = map(int, input().split())
# power_stations = [0]*(N+1)
# power_tmp = list(map(int, input().split()))
# parents = [i for i in range(N+1)]
# edges = []
# res = 0
#
# for station_num in power_tmp:
#     power_stations[station_num] = 1
#
# for _ in range(M):
#     u, v, w = map(int, input().split())
#     edges.append([w, u, v])
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     p_a = finding_parents(parents, a)
#     p_b = finding_parents(parents, b)
#     if p_a != p_b:
#         if power_stations[p_a] != 1 or power_stations[p_b] != 1:
#             union_parents(a,b)
#             res += cost
# print(res)

# v3
def finding_parents(parents, x):
    if parents[x] != x:
        parents[x] = finding_parents(parents, parents[x])
    return parents[x]

def union_parents(x, y):
    p_x = parents[x]
    p_y = parents[y]
    if power_stations[p_x] == 1 and power_stations[p_y] == 0:
        parents[p_y] = p_x
    elif power_stations[p_x] == 0 and power_stations[p_y] == 1:
        parents[p_x] = p_y
    elif power_stations[p_x] == 0 and power_stations[p_y] == 0:
        if p_x < p_y:
            parents[p_y] = p_x
        else:
            parents[p_x] = p_y
    else:
        return


N, M, K = map(int, input().split())
power_stations = [0]*(N+1)
power_tmp = list(map(int, input().split()))
parents = [i for i in range(N+1)]
edges = []
res = 0
edge_cnt = 0


for station_num in power_tmp:
    power_stations[station_num] = 1

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append([w, u, v])

edges.sort()

for edge in edges:
    cost, a, b = edge
    p_a = finding_parents(parents, a)
    p_b = finding_parents(parents, b)
    if p_a != p_b:
        if power_stations[p_a] != 1 or power_stations[p_b] != 1:
            union_parents(a,b)
            res += cost
            edge_cnt += 1
            if edge_cnt >= (N-K):
                break
print(res)