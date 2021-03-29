# baekjoon_9205 맥주 마시면서 걸어가기
# import collections
#
# v1
#
# def bfs():
#     queue = collections.deque()
#     queue.append([home[0],home[1],20])
#     visited.append(home)
#
#     tmp = "sad"
#
#     while queue:
#         x, y, beer = queue.popleft()
#         if x == festival[0] and y == festival[1]:
#             tmp = "happy "
#             return tmp
#         else:
#             for i_x, j_y in stores:
#                 if [i_x, j_y] not in visited:
#                     dist = abs(i_x - x) + abs(j_y - y)
#                     if (dist/50) <= beer:
#                         queue.append([i_x, j_y, beer])
#                         visited.append([i_x, j_y])
#     return tmp
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#
#     home = list(map(int, input().split()))
#     stores = []
#     visited = []
#
#     for _ in range(N):
#         store = list(map(int, input().split()))
#         stores.append(store)
#     festival = list(map(int, input().split()))
#     stores.append(festival)
#
#     res = bfs()
#     print(res)






# v2
# def bfs():
#     queue = collections.deque()
#     queue.append([home[0],home[1],20])
#     visited.append([home[0],home[1],20])
#
#     tmp = "sad"
#
#     while queue:
#         x, y, beer = queue.popleft()
#         if x == festival[0] and y == festival[1]:
#             tmp = "happy "
#             return tmp
#         else:
#             for i_x, j_y in stores:
#                 if [i_x, j_y, 20] not in visited:
#                     dist = abs(i_x - x) + abs(j_y - y)
#                     if (dist/50) <= beer:
#                         queue.append([i_x, j_y, beer])
#                         visited.append([i_x, j_y, beer])
#     return tmp
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#
#     home = list(map(int, input().split()))
#     stores = []
#     visited = []
#
#     for _ in range(N):
#         store = list(map(int, input().split()))
#         stores.append(store)
#     festival = list(map(int, input().split()))
#     stores.append(festival)
#
#     res = bfs()
#     print(res)


# re-v1
# from collections import deque
#
# def bfs(start, destination):
#     queue = deque()
#     queue.append(start)
#     visited.append(start)
#     d_i, d_j = destination
#     tmp = 'sad'
#     while queue:
#         s_i, s_j = queue.popleft()
#         dist = abs(d_i-s_i) + abs(d_j-s_j)
#
#         if dist//50 <= 20:
#             tmp = 'happy'
#             break
#         else:
#             if store:
#                 s_x, s_y = store.pop(0)
#                 dist2 = abs(s_x - s_i) + abs(s_y - s_j)
#                 if dist2 // 50 <= 20:
#                     queue.append([s_x, s_y])
#                     visited.append([s_x, s_y])
#     return tmp
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     visited = []
#     store = []
#     start = list(map(int, input().split()))
#     for _ in range(N):
#         i, j = map(int, input().split())
#         store.append([i,j])
#     destination = list(map(int, input().split()))
#     res = bfs(start, destination)
#     print(res)

# re-v2
from collections import deque

def bfs(start, destination):
    queue = deque()
    queue.append(start)
    visited.append(start)
    d_i, d_j = destination
    tmp = 'sad'
    while queue:
        s_i, s_j = queue.popleft()
        dist = abs(d_i-s_i) + abs(d_j-s_j)

        if dist/50 <= 20:
            tmp = 'happy'
            break
        else:
            for s_x, s_y in store:
                if [s_x, s_y] not in visited and (abs(s_x - s_i) + abs(s_y - s_j)) / 50 <=20:
                    queue.append([s_x, s_y])
                    visited.append([s_x, s_y])
    return tmp

T = int(input())
for tc in range(T):
    N = int(input())
    visited = []
    store = []
    start = list(map(int, input().split()))
    for _ in range(N):
        i, j = map(int, input().split())
        store.append([i,j])
    destination = list(map(int, input().split()))
    res = bfs(start, destination)
    print(res)