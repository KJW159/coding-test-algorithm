# baekjoon_1260
import collections

def dfs(graph, start_v):
    visited = []
    stack = []
    stack.append(start_v)

    while stack:
        node_s = stack.pop()
        if node_s not in visited:
            visited.append(node_s)
            stack_tmp = []
            for node_tmp in graph:
                if node_tmp[0] == node_s and node_tmp[1] not in stack_tmp:
                    stack_tmp.append(node_tmp[1])
                elif node_tmp[1] == node_s and node_tmp[0] not in stack_tmp:
                    stack_tmp.append(node_tmp[0])
            stack_tmp.sort(reverse=True)
            for n in stack_tmp:
                stack.append(n)
    return visited


def bfs(graph, start_v):
    visited = []
    queue = collections.deque()
    queue.append(start_v)

    while queue:
        node_s = queue.popleft()
        if node_s not in visited:
            visited.append(node_s)
            queue_tmp = []
            for node_tmp in graph:
                if node_tmp[0] == node_s and node_tmp[1] not in queue_tmp:
                    queue_tmp.append(node_tmp[1])
                elif node_tmp[1] == node_s and node_tmp[0] not in queue_tmp:
                    queue_tmp.append(node_tmp[0])
            queue_tmp.sort()
            for n in queue_tmp:
                queue.append(n)
    return visited


N, M, start_v = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(M)]
dfs_visited = dfs(graph, start_v)
bfs_visited = bfs(graph, start_v)
print(*dfs_visited)
print(*bfs_visited)
