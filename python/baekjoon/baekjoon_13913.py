# baekjoon_13913 숨바꼭질 4

#v1
# import collections
#
# def bfs(N, K):
#     queue = collections.deque()
#     queue.append([N, 0, [N]])
#     visited[N] = 1
#
#     while queue:
#         position, time, travel = queue.popleft()
#         if position == K and travel not in ways[time]:
#             ways[time].append(travel)
#             return time, travel
#         if position*2 <= 100000 and visited[position*2] == 0:
#             travel_tmp1 = travel[:]
#             travel_tmp1.append(position*2)
#             visited[position*2] = 1
#             queue.append([position*2, time+1, travel_tmp1])
#         if position+1 <= 100000 and visited[position+1] == 0:
#             travel_tmp2 = travel[:]
#             travel_tmp2.append(position+1)
#             visited[position+1] = 1
#             queue.append([position+1, time+1, travel_tmp2])
#         if position-1 >= 0 and visited[position-1] == 0:
#             travel_tmp3 = travel[:]
#             travel_tmp3.append(position-1)
#             visited[position-1] = 1
#             queue.append([position-1, time+1, travel_tmp3])
#
#     return -1, -1
#
#
# N, K = map(int, input().split())
# ways = collections.defaultdict(list)
# for tc in range(2):
#     visited = [0]*100001
#     res_time, res_travel = bfs(N, K)
#     if res_time != -1 and res_travel != -1:
#         print(res_time)
#         for i in res_travel:
#             print(i, end=" ")
#     else:
#         print(-1)
#     print()


# v2 시간초과
# import collections
#
# def bfs(N, K):
#     queue = collections.deque()
#     queue.append([N, 0, [N]])
#     visited[N] = 1
#
#     while queue:
#         position, time, travel = queue.popleft()
#         if position == K:
#             return time, travel
#         if position * 2 <= 100000 and visited[position * 2] == 0:
#             travel_tmp1 = travel[:]
#             travel_tmp1.append(position * 2)
#             visited[position * 2] = 1
#             queue.append([position * 2, time + 1, travel_tmp1])
#         if position + 1 <= 100000 and visited[position + 1] == 0:
#             travel_tmp2 = travel[:]
#             travel_tmp2.append(position + 1)
#             visited[position + 1] = 1
#             queue.append([position + 1, time + 1, travel_tmp2])
#         if position - 1 >= 0 and visited[position - 1] == 0:
#             travel_tmp3 = travel[:]
#             travel_tmp3.append(position - 1)
#             visited[position - 1] = 1
#             queue.append([position - 1, time + 1, travel_tmp3])
#
#
#
# N, K = map(int, input().split())
# visited = [0] * 100001
# res_time, res_travel = bfs(N, K)
# print(res_time)
# for i in res_travel:
#     print(i, end=" ")

# v3
# import collections
#
# def bfs(N, K):
#     queue = collections.deque()
#     queue.append([N, 0, [N]])
#     visited[N] = 1
#
#     while queue:
#         position, time, travel = queue.popleft()
#         travel_tmp = travel[:]
#         if position == K:
#             return time, travel
#         if position * 2 <= 100000 and visited[position * 2] == 0:
#             travel_tmp.append(position * 2)
#             visited[position * 2] = 1
#             queue.append([position * 2, time + 1, travel_tmp[:]])
#             travel_tmp.pop()
#         if position + 1 <= 100000 and visited[position + 1] == 0:
#             travel_tmp.append(position + 1)
#             visited[position + 1] = 1
#             queue.append([position + 1, time + 1, travel_tmp[:]])
#             travel_tmp.pop()
#         if position - 1 >= 0 and visited[position - 1] == 0:
#             travel_tmp.append(position - 1)
#             visited[position - 1] = 1
#             queue.append([position - 1, time + 1, travel_tmp[:]])
#             travel_tmp.pop()
#
#
# N, K = map(int, input().split())
# visited = [0] * 100001
# res_time, res_travel = bfs(N, K)
# print(res_time)
# for i in res_travel:
#     print(i, end=" ")

# v4
import collections

def travel(position, time):
    nodes_tmp = []
    past_p = position

    for __ in range(time+1):
        nodes_tmp.append(past_p)
        past_p = visited[past_p]
    return nodes_tmp

def bfs(N, K):
    queue = collections.deque()
    queue.append([N, 0])
    visited[N] = N

    while queue:
        position, time = queue.popleft()
        if position == K:
            nodes = travel(position, time)
            return time, nodes
        if position * 2 <= 100000 and visited[position * 2] == -1:
            visited[position * 2] = position
            queue.append([position * 2, time + 1])
        if position + 1 <= 100000 and visited[position + 1] == -1:
            visited[position + 1] = position
            queue.append([position + 1, time + 1])
        if position - 1 >= 0 and visited[position - 1] == -1:
            visited[position - 1] = position
            queue.append([position - 1, time + 1])


N, K = map(int, input().split())
visited = [-1] * 100001
res_time, res_position = bfs(N, K)
print(res_time)
res_position.reverse()
for i in res_position:
    print(i, end=" ")