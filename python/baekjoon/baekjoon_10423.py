# baekjoon_10423 전기가 부족해

# 조건
# 모든 도시에 전기를 공급하면서 케이블 설치 비용을 최소화 해야함.
# N개의 도시가 있고, M 개의 케이블 정도, K개의 발전소가 있는 도시
# 케이블이 연결되어 있는 도시에는 발전소가 하나만 존재해야함.
# 발전소가 설치된 도시는 케이블로 연결되지 않아도 됌.


# 풀이
# 최종적으로는 루트가 발전소가 있는 도시여야함.
# union 함수에서 단순히 작은 게 아니여야함.


# parents를 만듬. 발전소가 있는 도시는 절대 안 받겨야함.
# edges에 넣고 정렬하고 for문 돌려서 edge 꺼냄.
# finding parents 함수는 그대로 진행.
# 부모가 발전소가 있는 도시면 return? 아니면 작은 것으로 해보자.
# v1으로 하니깐 부모가 발전소 있는 도시인데 그 도시가 다른 경우에도 합쳐버림.
# 따라서 두개의 부모가 모두 발전소가 아닌 경우에 합치는 걸로 v2를 만듬.

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