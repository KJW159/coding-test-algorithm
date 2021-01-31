# baekjoon_12851 숨바꼭질2

# v1
# from collections import deque
# import math
#
#
# N, K = map(int, input().split())
# visited = [0]*100001
# visited_cnt = 0
# step_min = math.inf
# queue = deque()
# queue.append([N,0])
# visited[N] = 1
#
# while queue:
#     position, step = queue.popleft()
#     if position == K:
#         if step_min > step:
#             step_min = step
#             visited_cnt = 1
#         elif step_min == step:
#             visited_cnt += 1
#     if step_min < step:
#         break
#     if position*2 <= 100000 and visited[position*2] == 0:
#         queue.append([position*2, step+1])
#         if position*2 != K:
#             visited[position*2] = 1
#     if position+1 <= 100000 and visited[position+1] == 0:
#         queue.append([position+1, step+1])
#         if position+1 != K:
#             visited[position+1] = 1
#     if position-1 >= 0 and visited[position-1] == 0:
#         queue.append([position-1, step+1])
#         if position-1 != K:
#             visited[position-1] = 1
#
# print(step_min)
# print(visited_cnt)

#v2
# from collections import deque
# import math
#
#
# N, K = map(int, input().split())
# visited = [[0]*100001 for _ in range(3)]
# visited_cnt = 0
# step_min = math.inf
# queue = deque()
# queue.append([N,0])
# for i in range(3):
#     visited[i][N] = 1
#
# while queue:
#     position, step = queue.popleft()
#     if position == K:
#         if step_min > step:
#             step_min = step
#             visited_cnt = 1
#         elif step_min == step:
#             visited_cnt += 1
#     if step_min < step:
#         break
#     if position*2 <= 100000 and visited[0][position*2] == 0:
#         queue.append([position*2, step+1])
#         if position*2 != K:
#             visited[0][position*2] = 1
#     if position+1 <= 100000 and visited[1][position+1] == 0:
#         queue.append([position+1, step+1])
#         if position+1 != K:
#             visited[1][position+1] = 1
#     if position-1 >= 0 and visited[2][position-1] == 0:
#         queue.append([position-1, step+1])
#         if position-1 != K:
#             visited[2][position-1] = 1
#
# print(step_min)
# print(visited_cnt)

from collections import deque
import math


N, K = map(int, input().split())
visited = [0]*100001
visited_cnt = 0
step_min = math.inf
queue = deque()
queue.append([N,0])
visited[N] = 1

while queue:
    position, step = queue.popleft()
    if position == K:
        if step_min > step:
            step_min = step
            visited_cnt = 1
        elif step_min == step:
            visited_cnt += 1
    if step_min < step:
        break
    if position*2 <= 100000:
        if visited[position*2] == 0 or visited[position*2] == step+1:
            queue.append([position*2, step+1])
            visited[position*2] = step + 1
    if position+1 <= 100000:
        if visited[position+1] == 0 or visited[position+1] == step+1:
            queue.append([position+1, step+1])
            visited[position+1] = step + 1
    if position-1 >= 0:
        if visited[position-1] == 0 or visited[position-1] == step+1:
            queue.append([position-1, step+1])
            visited[position-1] = step + 1

print(step_min)
print(visited_cnt)



