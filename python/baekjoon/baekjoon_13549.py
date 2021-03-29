# baekjoon_13549 숨바꼭질 3
import collections

def bfs(N,K):
    time = 0
    queue = collections.deque()
    queue.append([N, time])
    visited[N] = 1

    while queue:
        position, time = queue.popleft()
        if position == K:
            return time
        if position*2 <= 100000 and visited[position*2] == 0:
            queue.append([position*2, time])
            visited[position*2] = 1
        if position-1 >= 0 and visited[position-1] == 0:
            queue.append([position-1, time+1])
            visited[position-1] = 1
        if position+1 <= 100000 and visited[position+1] == 0:
            queue.append([position+1, time+1])
            visited[position+1] = 1


N, K = map(int, input().split())

visited = [0]*100001
res = bfs(N,K)
print(res)