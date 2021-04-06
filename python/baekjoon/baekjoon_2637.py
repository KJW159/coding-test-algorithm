# baekjoon_2637 장난감 조립
from collections import deque


N = int(input())
M = int(input())
adj_list = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
part_cnt = [[0]*(N+1) for _ in range(N+1)]



for _ in range(M):
    x, y, k = map(int, input().split())
    adj_list[y].append([x,k])
    indegree[x] += 1

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        part_cnt[i][i] = 1

while queue:
    parts = queue.popleft()

    for product in adj_list[parts]:
        indegree[product[0]] -= 1
        for j in range(1, N+1):
            part_cnt[product[0]][j] += part_cnt[parts][j]*product[1]
        if indegree[product[0]] == 0:
            queue.append(product[0])

for i in range(1, N+1):
    if part_cnt[N][i]:
        print("{} {}".format(i, part_cnt[N][i]))


