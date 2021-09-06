# baekjoon_14267 회사 문화1

# v1
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     queue.append(1)
#     visited[1] = 1
#
#     while queue:
#         cur_node = queue.popleft()
#         for next_node in adj_list[cur_node]:
#             if visited[next_node] == 0:
#                 praise[next_node] += praise[cur_node]
#                 queue.append(next_node)
#                 visited[next_node] = 1
#
#
#
# N, M = map(int, input().split())
# adj_list = [[] for _ in range(N+1)]
#
# boss_num = list(map(int, input().split()))
# visited = [0]*(N+1)
# praise = [0]*(N+1)
#
# for i in range(1, N):
#     adj_list[boss_num[i]].append(i+1)
#
# for _ in range(M):
#     i, w = map(int, input().split())
#     praise[i] = w
#
# bfs()
#
# for i in range(1, N+1):
#     print("{}".format(praise[i]), end=" ")


# v2
from collections import deque


def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        cur_node = queue.popleft()
        for next_node in adj_list[cur_node]:
            if visited[next_node] == 0:
                praise[next_node] += praise[cur_node]
                queue.append(next_node)
                visited[next_node] = 1



N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

boss_num = list(map(int, input().split()))
visited = [0]*(N+1)
praise = [0]*(N+1)

for i in range(1, N):
    adj_list[boss_num[i]].append(i+1)

for _ in range(M):
    i, w = map(int, input().split())
    praise[i] += w

bfs()

for i in range(1, N+1):
    print("{}".format(praise[i]), end=" ")
