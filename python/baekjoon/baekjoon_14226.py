# baekjoon_14226 이모티콘

# v1
# from collections import deque
#
# def bfs(end):
#     queue = deque()
#     queue.append([1,0,0])
#
#     while queue:
#         screen, clipboard, cnt = queue.popleft()
#         if screen == end:
#             return cnt
#         # 화면 -> 클립 보드 목사
#         clipboard_tmp = screen
#         queue.append([screen, clipboard_tmp, cnt+1])
#         # 클립 보드 -> 화면
#         if clipboard != 0:
#             screen_tmp = screen
#             screen_tmp += clipboard
#             queue.append([screen_tmp, clipboard, cnt+1])
#         # 화면에서 삭제
#         if screen != 0:
#             screen_tmp = screen
#             screen_tmp -= 1
#             queue.append([screen_tmp, clipboard, cnt+1])
#
#
# S = int(input())
#
# res = bfs(S)
# print(res)


# v2
# from collections import deque
# import math
#
#
# def bfs(end):
#     queue = deque()
#     queue.append([1,0])
#     visited[1] = 0
#
#     while queue:
#         screen, clipboard = queue.popleft()
#         if screen == end:
#             return visited[screen]
#         # 화면 -> 클립 보드 목사
#         # 어떻게 화면에서 클립보드로 복사될때 +1을 해주지.
#         clipboard_tmp = screen
#         queue.append([screen, clipboard_tmp])
#         visited[screen] += 1
#         # 클립 보드 -> 화면
#         if clipboard != 0:
#             screen_tmp = screen
#             screen_tmp += clipboard
#             if visited[screen_tmp] > visited[screen]+1:
#                 queue.append([screen_tmp, clipboard])
#                 visited[screen_tmp] = visited[screen]+1
#         # 화면에서 삭제
#         if screen != 0:
#             screen_tmp = screen
#             screen_tmp -= 1
#             if visited[screen_tmp] > visited[screen]+1:
#                 queue.append([screen_tmp, clipboard])
#                 visited[screen_tmp] = visited[screen]+1
#
#
# S = int(input())
#
# INF = math.inf
#
# visited = [INF]*(1001)
# res = bfs(S)
# print(res)



# v3
from collections import deque
import math


def bfs(S):
    queue = deque()
    queue.append([1, 0])
    visited[1][0] = 0

    while queue:
        screen, clipboard = queue.popleft()
        # 화면 -> 클립 보드 목사
        if visited[screen][screen] == -1:
            queue.append([screen, screen])
            visited[screen][screen] = visited[screen][clipboard] + 1
        # 클립 보드 -> 화면
        if (screen+clipboard) <= S:
            if clipboard != 0 and visited[screen+clipboard][clipboard] == -1:
                queue.append([screen+clipboard, clipboard])
                visited[screen+clipboard][clipboard] = visited[screen][clipboard] + 1
        # 화면에서 삭제
        if (screen-1) >= 0 and visited[screen-1][clipboard] == -1:
            queue.append([screen-1, clipboard])
            visited[screen-1][clipboard] = visited[screen][clipboard]+1


S = int(input())

res = math.inf
visited = [[-1]*(S+1) for _ in range(S+1)]
bfs(S)

for i in range(S+1):
    if visited[S][i] != -1 and res > visited[S][i]:
        res = visited[S][i]

print(res)