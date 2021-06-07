# baekjoon_2056 작업

# v1
# from collections import deque
#
# def topology_sort(indegree_zero):
#     global res
#
#     queue = deque(indegree_zero)
#
#     while queue:
#         pre_work = queue.popleft()
#         for next_work in adj_list[pre_work]:
#             indegree[next_work] -= 1
#             if indegree[next_work] == 0:
#                 queue.append(next_work)
#                 working_time[next_work] += working_time[pre_work]
#                 res = max(res, working_time[next_work])
#
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# indegree = [0]*(N+1)
# indegree_zero = []
# working_time = [0]*(N+1)
# res = 0
# for i in range(1, N+1):
#     work_tmp = list(map(int, input().split()))
#     working_time[i] = work_tmp[0]
#     if work_tmp[1] == 0:
#         indegree_zero.append(i)
#         res = max(res, working_time[i])
#     else:
#         indegree[i] = work_tmp[1]
#         for j in range(2, len(work_tmp)):
#             adj_list[work_tmp[j]].append(i)
#
#
# topology_sort(indegree_zero)
# print(res)


# v2
from collections import deque

def topology_sort(indegree_zero):
    global res

    queue = deque(indegree_zero)

    while queue:
        pre_work = queue.popleft()
        for next_work in adj_list[pre_work]:
            indegree[next_work] -= 1
            time_tmp = working_time[next_work] + finished_time[pre_work]
            finished_time[next_work] = max(finished_time[next_work], time_tmp)
            if indegree[next_work] == 0:
                queue.append(next_work)
                res = max(res, finished_time[next_work])


N = int(input())
adj_list = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
indegree_zero = []
working_time = [0]*(N+1)
finished_time = [0]*(N+1)
res = 0
for i in range(1, N+1):
    work_tmp = list(map(int, input().split()))
    working_time[i] = work_tmp[0]
    if work_tmp[1] == 0:
        finished_time[i] = work_tmp[0]
        indegree_zero.append(i)
        res = max(res, working_time[i])
    else:
        indegree[i] = work_tmp[1]
        for j in range(2, len(work_tmp)):
            adj_list[work_tmp[j]].append(i)


topology_sort(indegree_zero)

print(res)
