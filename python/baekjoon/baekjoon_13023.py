# baekjoon_13023 ABCDE

# v1
# def dfs():
#     stack = [0]
#     visited[0] = 1
#     cnt = 1
#
#     while stack:
#         pre_man = stack.pop()
#         for next_man in adj_list[pre_man]:
#             if visited[next_man] == 0:
#                 stack.append(next_man)
#                 visited[next_man] = 1
#                 cnt += 1
#     if cnt == N:
#         return True
#     else:
#         return False
#
# N, M = map(int, input().split())
# adj_list = [[] for _ in range(N)]
# visited = [0]*N
# res = 0
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#     adj_list[b].append(a)
#
#
# if dfs():
#     res = 1
#
# print(res)

# v2
# def dfs(pre_man, cnt):
#         global res
#         if cnt == 5:
#             res = 1
#             return True
#         for next_man in adj_list[pre_man]:
#             if visited[next_man] == 0:
#                 visited[next_man] = 1
#                 dfs(next_man, cnt+1)
#                 visited[next_man] = 0
#
# N, M = map(int, input().split())
# adj_list = [[] for _ in range(N)]
# visited = [0]*N
# res = 0
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#     adj_list[b].append(a)
#
#
# for i in range(N):
#     if visited[i] == 0:
#         visited[i] = 1
#         dfs(i, 1)
#         visited[i] = 0
#
# print(res)

# v3
import sys

input = sys.stdin.readline


def dfs(pre_man, cnt):
    global res
    if cnt == 5:
        res = 1
        return True
    for next_man in adj_list[pre_man]:
        if visited[next_man] == 0:
            visited[next_man] = 1
            dfs(next_man, cnt + 1)
            visited[next_man] = 0


N, M = map(int, input().split())
adj_list = [[] for _ in range(N)]
visited = [0] * N
res = 0

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(N):
    if visited[i] == 0:
        visited[i] = 1
        dfs(i, 1)
        if res == 1:
            break
        visited[i] = 0

print(res)



