import collections

def bfs():
    cnt = 0
    queue = collections.deque()
    for i in range(1, N+1):
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1
            cnt += 1
            while queue:
                curr_node = queue.popleft()
                for j in adj_list[curr_node]:
                    if visited[j] == 0:
                        queue.append(j)
                        visited[j] = 1
    return cnt


N, M = list(map(int, input().split()))
adj_list = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
for __ in range(M):
    u, v = list(map(int, input().split()))
    adj_list[u].append(v)
    adj_list[v].append(u)
res = bfs()
print(res)