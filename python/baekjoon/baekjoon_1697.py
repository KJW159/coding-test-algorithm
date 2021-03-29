# baekjoon_1697 숨바꼭질

import collections


def bfs(N, K):
    step = 0
    queue = collections.deque()
    queue.append([N, step])
    visited[N] = 1

    while queue:
        position, step = queue.popleft()
        if position == K:
            break
        if position-1 >= 0 and visited[position-1] == 0:
            queue.append([position-1, step+1])
            visited[position-1] = 1
        if position+1 <= 100000 and visited[position+1] == 0:
            queue.append([position+1, step+1])
            visited[position+1] = 1
        if position*2 <= 100000 and visited[position*2] == 0:
            queue.append([position*2, step+1])
            visited[position*2] = 1
    return step


N, K = list(map(int, input().split()))
visited = [0]*100001
res = bfs(N, K)
print(res)