# baekjoon_6118 숨바꼭질



# v1
from collections import defaultdict, deque

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 0

    while queue:
        cur_node = queue.popleft()
        for next_node in adj_list[cur_node]:
            if visited[next_node] == -1:
                queue.append(next_node)
                dist = visited[cur_node] + 1
                visited[next_node] = dist
                nodes[dist].append(next_node)



N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


nodes = defaultdict(list)

bfs()

ordered_key = sorted(nodes.keys(), reverse=True)
ordered_list = sorted(nodes[ordered_key[0]])

print("{} {} {}".format(ordered_list[0], ordered_key[0], len(ordered_list)))