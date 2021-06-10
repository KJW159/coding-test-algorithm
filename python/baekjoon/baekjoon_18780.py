# baekjoon_18780 Timeline

# 조건

# N개의 세션을 M일동안 진행함.
# C개의 공간에 a,b,x 를 저장해놓음. a 다음 b 세션이 진행되고 a는 x일 동안 진행됌.
# 각 단계는 S일 보다 빠르게 일어나지 않음
# 각 세션이 끝나는 최소 일수를 구해라
# N, M, C 가 주어짐
# 다음줄에는 S에 관한게 주어짐


# 풀이

# 필요한 것
    # indegree
    # day 기록 -> 처음에 S를 받음.
    # adj_list 에는 다음 세션이랑 걸리는 일수 같이 넣어줌.
# 1. 처음에 전입차수가 0이면 큐에 넣는데 이때 day를 S로 갱신해줌.
# 2. 이전 세션의 day + 걸리는 일수를 더하고 다음 세션의 day에 있는 것보다 크면 갱신함.


# v1
# from collections import deque
#
#
# def topology_sort():
#     queue = deque()
#
#     for i in range(1, N+1):
#         if indegree[i] == 0:
#             queue.append(i)
#
#     while queue:
#         pre_s = queue.popleft()
#         for next_s, next_days in adj_list[pre_s]:
#             indegree[next_s] -= 1
#             if indegree[next_s] == 0:
#                 queue.append(next_s)
#                 date[next_s] = max(date[next_s], date[pre_s]+next_days)
#
# N, M, C = map(int, input().split())
# date = [0]+list(map(int, input().split()))
# adj_list = [[] for _ in range(N+1)]
# indegree = [0]*(N+1)
#
#
# for _ in range(C):
#     a, b, x = map(int, input().split())
#     adj_list[a].append([b,x])
#     indegree[b] += 1
#
# topology_sort()
#
# for i in range(1, N+1):
#     print(date[i])


# v2

from collections import deque


def topology_sort():
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        pre_s = queue.popleft()
        for next_s, next_days in adj_list[pre_s]:
            indegree[next_s] -= 1
            date[next_s] = max(date[next_s], date[pre_s]+next_days)
            if indegree[next_s] == 0:
                queue.append(next_s)

N, M, C = map(int, input().split())
date = [0]+list(map(int, input().split()))
adj_list = [[] for _ in range(N+1)]
indegree = [0]*(N+1)


for _ in range(C):
    a, b, x = map(int, input().split())
    adj_list[a].append([b,x])
    indegree[b] += 1

topology_sort()

for i in range(1, N+1):
    print(date[i])
