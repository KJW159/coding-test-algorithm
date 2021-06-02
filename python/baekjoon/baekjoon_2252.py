# baekjoon_2252 줄 세우기



from collections import deque

def topology_sort():
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        s_n = queue.popleft()
        res.append(s_n)
        for node in adj_list[s_n]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)



N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
res = []
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    indegree[b] += 1

topology_sort()
print(*res)