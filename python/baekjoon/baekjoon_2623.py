# baekjoon_2623 음악 프로그램

from collections import deque

def checking_cycle(here):
    if visited[here]:
        if visited[here] == -1:
            return True
        return False

    visited[here] = -1
    for node in adj_list[here]:
        if checking_cycle(node):
            return True
    visited[here] = 1
    return False

def topology_sort():
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        singer_num = queue.popleft()
        res.append(singer_num)

        for next_singer in adj_list[singer_num]:
            indegree[next_singer] -= 1
            if indegree[next_singer] == 0:
                queue.append(next_singer)

N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited = [0]*(N+1)
indegree = [0]*(N+1)

for _ in range(M):
    singer_tmp = list(map(int, input().split()))
    for i in range(1, singer_tmp[0]):
        adj_list[singer_tmp[i]].append(singer_tmp[i+1])
        indegree[singer_tmp[i+1]] += 1
res = []
trg = False
for i in range(1, N+1):
    if checking_cycle(i):
        trg = True
        res = [0]
        break
if not trg:
    topology_sort()

for singer in res:
    print(singer)



