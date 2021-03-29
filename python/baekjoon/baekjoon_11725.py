# baekjoon_11725

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
# import collections
#
# def bfs(node_e):
#     queue = collections.deque()
#     visited = [0] * (N + 1)
#
#     queue.append(1)
#     visited[1] = 1
#     parents = 0
#
#     while queue:
#         node = queue.popleft()
#         if node == node_e:
#             return parents
#         elif node in adj_list[node_e]:
#             parents = node
#         for curr in adj_list[node]:
#             if visited[curr] == 0:
#                 queue.append(curr)
#                 visited[curr] = 1
#
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# res = 0
# for __ in range(N-1):
#     n1, n2 = map(int, sys.stdin.readline().split())
#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)
#
# for i in range(2, N+1):
#     res = bfs(i)
#     print(res)


# v4
# import collections
# import sys
#
# def bfs(node_e):
#     queue = collections.deque()
#     visited = [0] * (N + 1)
#
#     queue.append([1, 0])
#     visited[1] = 1
#
#     while queue:
#         node, depth_n = queue.popleft()
#         for curr, depth_c in adj_list[node]:
#             if visited[curr] == 0:
#                 depth_c = depth_n + 1
#                 if curr == node_e and depth_c > depth_n:
#                     return node
#                 queue.append([curr, depth_c])
#                 visited[curr] = 1
#
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# res = 0
# for __ in range(N-1):
#     n1, n2 = map(int, sys.stdin.readline().split())
#     adj_list[n1].append([n2, 0])
#     adj_list[n2].append([n1, 0])
#
# for i in range(2, N+1):
#     res = bfs(i)
#     print(res)


#v5
# import collections
# import sys
#
# def bfs(node_e):
#     queue = collections.deque()
#     visited = [0] * (N + 1)
#
#     queue.append(1)
#     visited[1] = 1
#
#     while queue:
#         node = queue.popleft()
#         for curr in adj_list[node]:
#             if curr == node_e:
#                 return node
#             if visited[curr] == 0:
#                 queue.append(curr)
#                 visited[curr] = 1
#
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# res = 0
# for __ in range(N-1):
#     n1, n2 = map(int, sys.stdin.readline().split())
#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)
#
# for i in range(2, N+1):
#     res = bfs(i)
#     print(res)

# v6
# import collections
# import sys
#
# def bfs(node_e):
#     queue = collections.deque()
#     queue.append(1)
#
#     while queue:
#         node = queue.popleft()
#         for curr in adj_list[node]:
#             if curr == node_e:
#                 return node
#             queue.append(curr)
#
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# res = 0
# for __ in range(N-1):
#     n1, n2 = map(int, sys.stdin.readline().split())
#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)
#
# for i in range(2, N+1):
#     res = bfs(i)
#     print(res)

# v7
import collections
import sys

# def bfs():
#     queue = collections.deque()
#     queue.append(1)
#
#     visited = [0] * (N + 1)
#     visited[1] = 1
#
#     while queue:
#         node = queue.popleft()
#         for curr in adj_list[node]:
#             if visited[curr] == 0:
#                 parents[curr] = node
#                 queue.append(curr)
#                 visited[curr] = 1
#
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# res = 0
# parents = [0]*(N+1)
#
# for __ in range(N-1):
#     n1, n2 = map(int, sys.stdin.readline().split())
#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)
#
# bfs()
#
# for i in range(2, N+1):
#     print(parents[i])

# re-v1
# from collections import deque
#
# def finding_parents():
#     queue = deque()
#     queue.append(1)
#     parents[1] = 1
#     while queue:
#         node = queue.popleft()
#         for child in adj_list[node]:
#             if parents[child] == 0:
#                 parents[child] = node
#                 queue.append(child)
#
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
#
# parents = [0]*(N+1)
# for _ in range(N-1):
#     u, v = map(int, input().split())
#     adj_list[u].append(v)
#     adj_list[v].append(u)
#
# finding_parents()
#
# # for p in parents[2:]:
# #     print(p)
#
# for i in range(2,N+1):
#     print(parents[i])

# re-v2
def finding_parents_dfs():
    stack = []
    stack.append(1)
    parents[1] = 1
    while stack:
        node = stack.pop()
        for child in adj_list[node]:
            if parents[child] == 0:
                stack.append(child)
                parents[child] = node


N = int(input())
adj_list = [[] for _ in range(N+1)]

parents = [0]*(N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

finding_parents_dfs()

for i in range(2,N+1):
    print(parents[i])