# baekjoon_1389 케빈 베이컨의 6단계 법칙

import collections
import math

def bfs(start):
    visited = [0] * (N+1)
    queue = collections.deque()
    queue.append([start, 0])
    visited[start] = 1
    total_cnt = 0

    while queue:
        node, cnt_n = queue.popleft()
        for friend, cnt_f in adj_list[node]:
            if visited[friend] == 0:
                cnt_f = cnt_n + 1
                queue.append([friend, cnt_f])
                total_cnt += cnt_f
                visited[friend] = 1
    return total_cnt


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
relation = math.inf
res = 0
for __ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append([B,0])
    adj_list[B].append([A,0])

for i in range(1, N+1):
    tmp = bfs(i)
    if tmp < relation:
        relation = tmp
        res = i
    elif tmp == relation:
        if i < res:
            res = i
print(res)


