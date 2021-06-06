# baekjoon_14567 선수 과목

# v1
from collections import deque
import sys

input = sys.stdin.readline


def topology_sort():
    queue = deque()
    semester_num = 1

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            semester[i] = semester_num

    while queue:
        pre_sub = queue.popleft()
        semester_num = semester[pre_sub] + 1

        for next_sub in adj_list[pre_sub]:
            indegree[next_sub] -= 1
            if indegree[next_sub] == 0:
                queue.append(next_sub)
                semester[next_sub] = semester_num


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
semester = [0]*(N+1)


for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    indegree[b] += 1

topology_sort()

print(*semester[1:])