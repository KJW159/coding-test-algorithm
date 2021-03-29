#swea_2814 최장 경로
# v1
# def dfs(node, cnt):
#     visited[node] = 1
#
#     for n in adj_list[node]:
#         if visited[n] == 0:
#             cnt += 1
#             cnt = dfs(n, cnt)
#     return cnt
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     adj_list = [[] for _ in range(N+1)]
#     visited = [0]*(N+1)
#     res = 0
#     for _ in range(M):
#         i, j = map(int, input().split())
#         adj_list[i].append(j)
#         adj_list[j].append(i)
#     for node in range(1, N+1):
#         cnt_tmp = dfs(node, 1)
#         res = max(res, cnt_tmp)
#
#     print("#{} {}".format(tc, res))



# v2
# def dfs(node, cnt):
#
#     for n in adj_list[node]:
#         if visited[n] == 0:
#             visited[n] = cnt+1
#             cnt = dfs(n, visited[n])
#     return cnt
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     adj_list = [[] for _ in range(N+1)]
#     res = 0
#     for _ in range(M):
#         i, j = map(int, input().split())
#         adj_list[i].append(j)
#         adj_list[j].append(i)
#     for node in range(1, N+1):
#         visited = [0] * (N + 1)
#         visited[node] = 1
#         cnt_tmp = dfs(node, 1)
#         res = max(res, cnt_tmp)
#
#     print("#{} {}".format(tc, res))


# v3

def dfs(node, cnt):
    visited[node] = 1
    global res
    res = max(res, cnt)

    for n in adj_list[node]:
        if visited[n] == 0:
            dfs(n, cnt+1)
            # visited[n] = 0

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    res = 0
    for _ in range(M):
        i, j = map(int, input().split())
        adj_list[i].append(j)
        adj_list[j].append(i)
    for node in range(1, N + 1):
        visited = [0] * (N + 1)
        dfs(node, 1)
    print("#{} {}".format(tc, res))
