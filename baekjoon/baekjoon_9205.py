# baekjoon_9205 맥주 마시면서 걸어가기
import collections

# v1

def bfs():
    queue = collections.deque()
    queue.append([home[0],home[1],20])
    visited.append(home)

    tmp = "sad"

    while queue:
        x, y, beer = queue.popleft()
        if x == festival[0] and y == festival[1]:
            tmp = "happy "
            return tmp
        else:
            for i_x, j_y in stores:
                if [i_x, j_y] not in visited:
                    dist = abs(i_x - x) + abs(j_y - y)
                    if (dist/50) <= beer:
                        queue.append([i_x, j_y, beer])
                        visited.append([i_x, j_y])
    return tmp


T = int(input())
for tc in range(T):
    N = int(input())

    home = list(map(int, input().split()))
    stores = []
    visited = []

    for _ in range(N):
        store = list(map(int, input().split()))
        stores.append(store)
    festival = list(map(int, input().split()))
    stores.append(festival)

    res = bfs()
    print(res)






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