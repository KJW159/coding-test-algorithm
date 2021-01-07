# baekjoon_11725
import sys


# v2
# def dfs(node_e):
#     stack = []
#     visited = [0] * (N + 1)
#
#     stack.append(1)
#     visited[1] = 1
#     parents = 0
#
#     while stack:
#         node = stack.pop()
#         if node == node_e:
#             return parents
#         elif node in adj_list[node_e]:
#             parents = node
#         for curr in adj_list[node]:
#             if visited[curr] == 0:
#                 stack.append(curr)
#                 visited[curr] = 1
#
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# result = [0]*(N+1)
# tmp = 0
# for __ in range(N-1):
#     n1, n2 = map(int, sys.stdin.readline().split())
#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)
#
# for i in range(2, N+1):
#     tmp = dfs(i)
#     result[i] = tmp
#
# for ans in result[2:]:
#     print(ans)


# v3
import collections

def bfs(node_e):
    queue = collections.deque()
    visited = [0] * (N + 1)

    queue.append(1)
    visited[1] = 1
    parents = 0

    while queue:
        node = queue.popleft()
        if node == node_e:
            return parents
        elif node in adj_list[node_e]:
            parents = node
        for curr in adj_list[node]:
            if visited[curr] == 0:
                queue.append(curr)
                visited[curr] = 1


N = int(input())
adj_list = [[] for _ in range(N+1)]
res = 0
for __ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

for i in range(2, N+1):
    res = bfs(i)
    print(res)
