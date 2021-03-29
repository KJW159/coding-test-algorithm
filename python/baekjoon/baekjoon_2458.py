# baekjoon_2458 키 순서


# v1
# def dfs(start):
#     stack = [start]
#     visited[start] = 1
#
#     while stack:
#         node = stack.pop()
#         for tall in adj_list[node]:
#             if visited[tall] == 0:
#                 stack.append(tall)
#                 visited[tall] = 1
#
#
# def dfs2(small, start):
#     visited_tmp = visited[:]
#     stack = [small]
#     visited_tmp[small] = 1
#
#     while stack:
#         node_s = stack.pop()
#         if node_s == start or visited[node_s] == 1:
#             visited[small] = 1
#             return
#         for n in adj_list[node_s]:
#             if visited_tmp[n] == 0:
#                 stack.append(n)
#                 visited_tmp[n] = 1
#
# N, M = map(int, input().split())
#
# adj_list = [[] for _ in range(N+1)]
#
# for _ in range(M):
#     i, j = map(int, input().split())
#     adj_list[i].append(j)
#
# res = 0
#
# for start in range(1, N+1):
#     ch_cnt = 0
#     visited = [0]*(N+1)
#     dfs(start)
#     visited[start] = 0
#     for small in range(1, N+1):
#         if visited[small] == 0 and small != start:
#             dfs2(small, start)
#     for ch in visited[1:]:
#         if ch == 1:
#             ch_cnt += 1
#     if ch_cnt == N-1:
#         res += 1
# print(res)



#v2

N, M = map(int, input().split())
visited = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    visited[a][b] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if visited[i][k] == 1 and visited[k][j] == 1:
                visited[i][j] = 1
res = 0
for n1 in range(1, N+1):
    cnt = 0
    for n2 in range(1, N+1):
        cnt += (visited[n1][n2] + visited[n2][n1])
    if cnt == N-1:
        res += 1
print(res)
