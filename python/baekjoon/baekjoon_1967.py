# baekjoon_1967 트리의 지름

# baekjoon_1967 트리의 지름

# v1 - 메모리 초과
# import sys
# sys.setrecursionlimit(1000000)
#
#
# def dfs(start_node, distance):
#     for node, w in adj[start_node]:
#         if distance[node] == 0:
#             distance[node] = distance[start_node] + w
#             dfs(node, distance)
#
#
# N = int(input())
# adj = [[] for _ in range(N+1)]
#
# for _ in range(N-1):
#     a,b,c = map(int, input().split())
#     adj[a].append([b,c])
#     adj[b].append([a,c])
#
# # 루트에서 가장 먼 노드 찾기
# distance1 = [0]*(N+1)
# dfs(1,distance1)
# max_distance_node = distance1.index(max(distance1))
#
# # 가장 먼 노드에서 먼 노드까지의 거리 찾기
# distance2 = [0]*(N+1)
# dfs(max_distance_node, distance2)
# res = max(distance2)
# print(res)

# v2
# import sys
# sys.setrecursionlimit(100000)
#
#
# def dfs(start_node, distance, version):
#     if version == 1:
#         distance[1] = 0
#
#     for node, w in adj[start_node]:
#         if distance[node] == 0:
#             distance[node] = distance[start_node] + w
#             dfs(node, distance)
#
#
# N = int(input())
# adj = [[] for _ in range(N+1)]
#
# for _ in range(N-1):
#     a,b,c = map(int, input().split())
#     adj[a].append([b,c])
#     adj[b].append([a,c])
#
# # 루트에서 가장 먼 노드 찾기
# distance1 = [0]*(N+1)
# dfs(1,distance1,1)
# max_distance_node = distance1.index(max(distance1))
#
# # 가장 먼 노드에서 먼 노드까지의 거리 찾기
# distance2 = [0]*(N+1)
# dfs(max_distance_node, distance2,2)
# res = max(distance2)
# print(res)

# v3
# import sys
# sys.setrecursionlimit(100000)
#
#
# def dfs(start_node, distance):
#
#     for node, w in adj[start_node]:
#         if distance[node] == 0:
#             distance[node] = distance[start_node] + w
#             dfs(node, distance)
#
#
# N = int(input())
# adj = [[] for _ in range(N+1)]
#
# for _ in range(N-1):
#     a,b,c = map(int, input().split())
#     adj[a].append([b,c])
#     adj[b].append([a,c])
#
# # 루트에서 가장 먼 노드 찾기
# distance1 = [0]*(N+1)
# dfs(1,distance1)
# max_distance_node = distance1.index(max(distance1))
#
# # 가장 먼 노드에서 먼 노드까지의 거리 찾기
# distance2 = [0]*(N+1)
# dfs(max_distance_node, distance2)
# res = max(distance2)
# print(res)


# v4
import sys
sys.setrecursionlimit(100000)


def dfs(start_node, distance, root):

    for node, w in adj[start_node]:
        if distance[node] == 0:
            # 맨 처음에 시작한 노드 재방문 방지
            if node != root:
                distance[node] = distance[start_node] + w
                dfs(node, distance, root)


N = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c = map(int, input().split())
    adj[a].append([b,c])
    adj[b].append([a,c])

# 루트에서 가장 먼 노드 찾기
distance1 = [0]*(N+1)
dfs(1,distance1,1)
max_distance_node = distance1.index(max(distance1))

# 가장 먼 노드에서 먼 노드까지의 거리 찾기
distance2 = [0]*(N+1)
dfs(max_distance_node, distance2, max_distance_node)
res = max(distance2)
print(res)