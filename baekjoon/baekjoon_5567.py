# baekjoon_5567 결혼식



# v1
# import collections

# def bfs():
#     queue = collections.deque()
#     queue.append([1,0])
#     visited[1] = 1
#     invited = 0
#
#     while queue:
#         node, cnt_n = queue.popleft()
#         if cnt_n == 3:
#             return invited
#         for friend, cnt_f in adj_list[node]:
#             if visited[friend] == 0:
#                 cnt_f = cnt_n + 1
#                 queue.append([friend, cnt_f])
#                 visited[friend] = 1
#                 if cnt_f == 2 or cnt_f ==1:
#                     invited += 1
#
#
# N = int(input())
# M = int(input())
# adj_list = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# for __ in range(M):
#     f1, f2 = map(int, input().split())
#     adj_list[f1].append([f2, 0])
#     adj_list[f2].append([f1, 0])
#
# res = bfs()
# print(res)


# v2
import collections

def bfs():
    queue = collections.deque()
    queue.append([1,0])
    visited[1] = 1
    invited = 0

    while queue:
        node, cnt_n = queue.popleft()
        for friend, cnt_f in adj_list[node]:
            if visited[friend] == 0:
                cnt_f = cnt_n + 1
                if cnt_f < 2:
                    queue.append([friend, cnt_f])
                visited[friend] = 1
                invited += 1
    return invited


N = int(input())
M = int(input())
adj_list = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for __ in range(M):
    f1, f2 = map(int, input().split())
    adj_list[f1].append([f2, 0])
    adj_list[f2].append([f1, 0])

res = bfs()
print(res)
