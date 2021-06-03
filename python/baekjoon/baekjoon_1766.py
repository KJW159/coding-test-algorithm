# baekjoon_1766 문제집



# v1
# import heapq
#
# def topology_sort():
#     pq = []
#     for i in range(1, N+1):
#         if indegree[i] == 0:
#             heapq.heappush(pq, i)
#
#     while pq:
#         problem_num = heapq.heappop(pq)
#         res.append(problem_num)
#
#         for next_num in adj_list[problem_num]:
#             indegree[next_num] -= 1
#             if indegree[next_num] == 0:
#                 heapq.heappush(pq, next_num)
#
# N, M = map(int, input().split())
#
# adj_list = [[] for _ in range(N+1)]
# indegree = [0]*(N+1)
# res = []
#
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#     indegree[b] += 1
#
# topology_sort()
#
# print(*res)

# v2
import heapq

def topology_sort():
    pq = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(pq, i)

    while pq:
        problem_num = heapq.heappop(pq)
        print(problem_num, end=" ")

        for next_num in adj_list[problem_num]:
            indegree[next_num] -= 1
            if indegree[next_num] == 0:
                heapq.heappush(pq, next_num)

N, M = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    indegree[b] += 1

topology_sort()