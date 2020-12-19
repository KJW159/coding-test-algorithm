# baekjoon_2606 바이러스

import collections

# v1 - 시간초과 나옴.
# def bfs(graph, start_c):
#     visited = []
#     queue = collections.deque()
#     queue.append(start_c)
#     cnt = 0
#     while queue:
#         comp = queue.popleft()
#         if comp not in visited:
#             visited.append(comp)
#             if comp != 1:
#                 cnt += 1
#         for net in graph:
#             if net[0] == comp:
#                 queue.append(net[1])
#     return cnt

# v2 - 시간 초과
# import collections
# import sys
# read = sys.stdin.readline
#
# def bfs(graph, start_c):
#     visited = []
#     visited.append(start_c)
#     queue = collections.deque()
#     queue.append(start_c)
#     cnt = 0
#     while queue:
#         comp = queue.popleft()
#         for net in graph:
#             if net[0] == comp:
#                 queue.append(net[1])
#         if comp not in visited:
#             visited.append(comp)
#             cnt += 1
#     return cnt


# v3 - 시간초과는 해결됌. 하지만 틀리는 케이스가 있음.
import collections
import sys
read = sys.stdin.readline

def bfs(graph, start_c):
    queue = collections.deque()
    queue.append(start_c)

    visited = []
    visited.append(start_c)
    cnt = 0
    while queue:
        comp = queue.popleft()
        for net in graph:
            if net[0] == comp and net[1] not in visited:
                queue.append(net[1])
                visited.append(net[1])
                cnt += 1
            if net[1] == comp and net[0] not in visited:
                queue.append(net[0])
                visited.append(net[0])
                cnt += 1
    return cnt

T = int(read())
N = int(read())
graph = [list(map(int, read().split())) for _ in range(N)]

start_c = 1
result = bfs(graph, start_c)
print(result)