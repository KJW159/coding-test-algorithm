# baekjoon_1325 효율적인 해킹

# v1
# import collections
#
# def bfs(comp):
#     visited = [0]*(N+1)
#     cnt = 0
#
#     queue = collections.deque()
#     queue.append(comp)
#     visited[comp] = 1
#
#     while queue:
#         comp1 = queue.popleft()
#         for comp2 in adj_list[comp1]:
#             if visited[comp2] == 0:
#                 queue.append(comp2)
#                 visited[comp2] = 1
#                 cnt += 1
#     return cnt
#
#
# N, M = map(int, input().split())
# adj_list = [ [] for _ in range(N+1)]
# hacking = [0]*(N+1)
# comp_number = []
# for __ in range(M):
#     n1, n2 = map(int, input().split())
#     adj_list[n2].append(n1)
#
# for i in range(1,N+1):
#     hacking_cnt = bfs(i)
#     hacking[i] = hacking_cnt
#
# max_num = max(hacking)
# for j in range(1,N+1):
#     if hacking[j] == max_num:
#         comp_number.append(j)
# comp_number.sort()
# for res in comp_number:
#     print(res, end=" ")


# v2
# import collections
#
# def bfs(comp):
#     visited = [0]*(N+1)
#     cnt = 0
#
#     queue = collections.deque()
#     queue.append(comp)
#     visited[comp] = 1
#
#     while queue:
#         comp1 = queue.popleft()
#         for comp2 in adj_list[comp1]:
#             if visited[comp2] == 0:
#                 queue.append(comp2)
#                 visited[comp2] = 1
#                 cnt += 1
#     return cnt
#
#
# N, M = map(int, input().split())
# adj_list = [ [] for _ in range(N+1)]
# hacking = [0]*(N+1)
# comp_number = []
# for __ in range(M):
#     n1, n2 = map(int, input().split())
#     adj_list[n2].append(n1)
#
# for i in range(1,N+1):
#     hacking_cnt = bfs(i)
#     hacking[i] = hacking_cnt
#
# max_num = max(hacking)
# for j in range(1,N+1):
#     if hacking[j] == max_num:
#         comp_number.append(j)
#
# for res in comp_number:
#     print(res, end=" ")

# v3
# import collections
#
# def bfs(comp):
#     visited = [0]*(N+1)
#     cnt = 0
#
#     queue = collections.deque()
#     queue.append(comp)
#     visited[comp] = 1
#
#     while queue:
#         comp1 = queue.popleft()
#         for comp2 in adj_list[comp1]:
#             if visited[comp2] == 0:
#                 queue.append(comp2)
#                 visited[comp2] = 1
#                 cnt += 1
#     return cnt
#
#
# N, M = map(int, input().split())
# adj_list = [ [] for _ in range(N+1)]
# hacking = [0]*(N+1)
# comp_number = []
# for __ in range(M):
#     n1, n2 = map(int, input().split())
#     adj_list[n2].append(n1)
#
#
# max_num = -1
# for i in range(1,N+1):
#     hacking_cnt = bfs(i)
#     if hacking_cnt > max_num:
#         comp_number = [i]
#         max_num = hacking_cnt
#     elif hacking_cnt == max_num:
#         comp_number.append(i)
#
# for res in comp_number:
#     print(res, end=" ")

# re-v1

def dfs(start):
    stack = []
    stack.append(start)
    visited[start] = 1
    connection = 0

    while stack:
        start = stack.pop()
        for node in adj_list[start]:
            if visited[node] == 0:
                stack.append(node)
                visited[node] = 1
                connection += 1
    return connection

N, M = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
max_cnt = 0
computers = []
for _ in range(M):
    i, j = map(int, input().split())
    adj_list[j].append(i)
for n in range(1, N+1):
    visited = [0] * (N+1)
    cnt = dfs(n)
    if cnt == max_cnt:
        computers.append(n)
    elif cnt > max_cnt:
        max_cnt = cnt
        computers = [n]
computers.sort()
print(*computers)