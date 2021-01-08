#baekjoon_2664 촌수 계산
import collections

def bfs(S, E):
    queue = collections.deque()
    cnt_s = 0
    queue.append([S, cnt_s])
    visited[S] = 1

    while queue:
        node, cnt = queue.popleft()
        if node == E:
            return cnt
        for curr, cnt_tmp in adj_list[node]:
            if visited[curr] == 0:
                cnt_tmp = cnt + 1
                queue.append([curr, cnt_tmp])
                visited[curr] = 1

    return -1

N = int(input())
S, E = map(int, input().split())
V = int(input())
adj_list =[[] for _ in range(N+1)]

visited = [0]*(N+1)
for __ in range(V):
    x, y = map(int, input().split())
    adj_list[x].append([y, 0])
    adj_list[y].append([x, 0])

res = bfs(S, E)
print(res)

