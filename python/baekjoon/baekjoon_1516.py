# baekjoon_1516 게임 개발



# v1
# from collections import deque
#
# def topology_sort():
#     queue = deque()
#     for i in range(1, N+1):
#         if indegree[i] == 0:
#             queue.append(i)
#
#     while queue:
#         now_num = queue.popleft()
#         for next_num in adj_list[now_num]:
#             indegree[next_num] -= 1
#             if indegree[next_num] == 0:
#                 queue.append(next_num)
#                 building_time[next_num] += building_time[now_num]
#
#
# N = int(input())
# building_time = [0]*(N+1)
# indegree = [0]*(N+1)
# adj_list =[[] for _ in range(N+1)]
#
# for i in range(1, N+1):
#     input_tmp = list(map(int, input().split()))
#     building_time[i] = input_tmp[0]
#     for j in range(1, len(input_tmp)):
#         if input_tmp[j] == -1:
#             break
#         adj_list[input_tmp[j]].append(i)
#         indegree[i] += 1
#
# topology_sort()
# for i in range(1, N+1):
#     print(building_time[i])


# v2
# from collections import deque
# import math
#
# def topology_sort():
#     queue = deque()
#     for i in range(1, N+1):
#         if indegree[i] == 0:
#             queue.append(i)
#
#     while queue:
#         now_num = queue.popleft()
#         for next_num in adj_list[now_num]:
#             indegree[next_num] -= 1
#             if indegree[next_num] == 0:
#                 queue.append(next_num)
#                 building_time[next_num] += building_time[now_num]
#
#
# N = int(input())
# initial_time = [0]*(N+1)
# building_time = [math.inf]*(N+1)
# indegree = [0]*(N+1)
# adj_list =[[] for _ in range(N+1)]
#
# for i in range(1, N+1):
#     input_tmp = list(map(int, input().split()))
#     initial_time[i] = input_tmp[0]
#     for j in range(1, len(input_tmp)):
#         if input_tmp[j] == -1:
#             break
#         adj_list[input_tmp[j]].append(i)
#         indegree[i] += 1
#
# topology_sort()
# for i in range(1, N+1):
#     print(building_time[i])


# v3
from collections import deque

def topology_sort():
    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            building_time[i] = initial_time[i]

    while queue:
        now_num = queue.popleft()
        for next_num in adj_list[now_num]:
            indegree[next_num] -= 1
            building_time[next_num] = max(building_time[next_num], building_time[now_num]+initial_time[next_num])
            if indegree[next_num] == 0:
                queue.append(next_num)

N = int(input())
initial_time = [0]*(N+1)
building_time = [0]*(N+1)
indegree = [0]*(N+1)
adj_list =[[] for _ in range(N+1)]

for i in range(1, N+1):
    input_tmp = list(map(int, input().split()))
    initial_time[i] = input_tmp[0]
    for j in range(1, len(input_tmp)):
        if input_tmp[j] == -1:
            break
        adj_list[input_tmp[j]].append(i)
        indegree[i] += 1

topology_sort()

for i in range(1, N+1):
    print(building_time[i])