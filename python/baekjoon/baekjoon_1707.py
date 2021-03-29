# baekjoon_1707 이분 그래프
import collections

# v1
# def bipartite_bfs(node_first):
#     queue = collections.deque()
#     visited1 = []
#     visited2 = []
#
#     queue.append(node_first[0])
#     visited1.append(node_first[0])
#
#     while queue:
#         node_start = queue.popleft()
#         for node in graph:
#             if node[0] == node_start:
#                 if node[0] in visited2 and node[1] not in visited1:
#                     queue.append(node[1])
#                     visited1.append(node[1])
#                 elif node[0] in visited1 and node[1] not in visited2:
#                     queue.append(node[1])
#                     visited2.append(node[1])
#                 else:
#                     res_tmp = 0
#                     return res_tmp
#
#             if node[1] == node_start:
#                 if node[1] in visited2 and node[0] not in visited1:
#                     queue.append(node[0])
#                     visited1.append(node[0])
#                 elif node[1] in visited1 and node[0] not in visited2:
#                     queue.append(node[0])
#                     visited2.append(node[0])
#                 else:
#                     res_tmp = 0
#                     return res_tmp


#v2
def bipartite_bfs(node_first):
    queue = collections.deque()
    visited1 = []
    visited2 = []

    queue.append(node_first[0])
    visited1.append(node_first[0])

    while queue:
        node_start = queue.popleft()
        for node in graph:
            if node[0] == node_start and node[1] not in visited1 and node[1] not in visited2:
                if node[0] in visited2:
                    queue.append(node[1])
                    visited1.append(node[1])
                elif node[0] in visited1:
                    queue.append(node[1])
                    visited2.append(node[1])

            elif node[1] == node_start and node[0] not in visited1 and node[0] not in visited2:
                if node[1] in visited2:
                    queue.append(node[0])
                    visited1.append(node[0])
                elif node[1] in visited1:
                    queue.append(node[0])
                    visited2.append(node[0])

            if node[0] == node_start and node[0] in visited1 and node[1] in visited1:
                res_tmp = 0
                return res_tmp
            if node[0] == node_start and node[0] in visited2 and node[1] in visited2:
                res_tmp = 0
                return res_tmp
            if node[1] == node_start and node[1] in visited1 and node[0] in visited1:
                res_tmp = 0
                return res_tmp
            if node[1] == node_start and node[1] in visited2 and node[0] in visited2:
                res_tmp = 0
                return res_tmp
    return 1

T = int(input())
for tc in range(T):
    V, E = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(E)]
    res = bipartite_bfs(graph[0])
    if res == 0:
        print("NO")
    if res == 1:
        print("YES")