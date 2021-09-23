# baekjoon_12904 A와 B

# v1
# from collections import deque
#
# def bfs(s):
#     queue = deque()
#     queue.append(s)
#
#     while queue:
#         cur_str = queue.popleft()
#         if len(cur_str) > len(T):
#             return 0
#         changed = cur_str + 'A'
#         if changed == T:
#             return 1
#         queue.append(changed)
#         changed = cur_str[::-1] + 'B'
#         if changed == T:
#             return 1
#         queue.append(changed)
#     return 0
#
# S = input()
# T = input()
#
# print(bfs(S))


# v2
# from collections import deque, defaultdict
#
# def bfs(s):
#     queue = deque()
#     queue.append(s)
#
#     while queue:
#         cur_str = queue.popleft()
#         if len(cur_str) > len(T):
#             return 0
#         if cur_str == T:
#             return 1
#         changed1 = cur_str + 'A'
#         changed2 = cur_str[::-1] + 'B'
#         if visited[changed1] == 0:
#             queue.append(changed1)
#             visited[changed1] = 1
#         if visited[changed2] == 0:
#             queue.append(changed2)
#             visited[changed2] = 1
#     return 0
#
#
# S = input()
# T = input()
# visited = defaultdict(int)
# print(bfs(S))


# v3
# from collections import deque, defaultdict
#
# def bfs(s):
#     queue = deque()
#     queue.append(s)
#
#     while queue:
#         cur_str = queue.popleft()
#         if len(cur_str) > len(T):
#             return 0
#         changed1 = cur_str + 'A'
#         changed2 = cur_str[::-1] + 'B'
#         if visited[changed1] == 0:
#             if changed1 == T:
#                 return 1
#             queue.append(changed1)
#             visited[changed1] = 1
#         if visited[changed2] == 0:
#             if changed2 == T:
#                 return 1
#             queue.append(changed2)
#             visited[changed2] = 1
#     return 0
#
#
# S = input()
# T = input()
# visited = defaultdict(int)
# print(bfs(S))


# v4
S = list(input())
T = list(input())

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)
