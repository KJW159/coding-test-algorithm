# baekjoon_12761 돌다리

# v1

from collections import deque


A, B, N, M = map(int, input().split())
visited = [-1] * 100001
queue = deque()
queue.append(N)
visited[N] = 0

while queue:
    cur_pos = queue.popleft()
    if cur_pos == M:
        print(visited[cur_pos])
        break
    if 0 <= cur_pos-1 < 100001 and visited[cur_pos-1] == -1:
        queue.append(cur_pos-1)
        visited[cur_pos-1] = visited[cur_pos] + 1
    if 0 <= cur_pos+1 < 100001 and visited[cur_pos+1] == -1:
        queue.append(cur_pos+1)
        visited[cur_pos+1] = visited[cur_pos] + 1
    if 0 <= cur_pos-A < 100001 and visited[cur_pos-A] == -1:
        queue.append(cur_pos-A)
        visited[cur_pos-A] = visited[cur_pos] + 1
    if 0 <= cur_pos+A < 100001 and visited[cur_pos+A] == -1:
        queue.append(cur_pos+A)
        visited[cur_pos+A] = visited[cur_pos] + 1
    if 0 <= cur_pos-B < 100001 and visited[cur_pos-B] == -1:
        queue.append(cur_pos-B)
        visited[cur_pos - B] = visited[cur_pos] + 1
    if 0 <= cur_pos+B < 100001 and visited[cur_pos+B] == -1:
        queue.append(cur_pos+B)
        visited[cur_pos+B] = visited[cur_pos] + 1
    if 0 <= cur_pos*A < 100001 and visited[cur_pos*A] == -1:
        queue.append(cur_pos*A)
        visited[cur_pos*A] = visited[cur_pos] + 1
    if 0 <= cur_pos*B < 100001 and visited[cur_pos*B] == -1:
        queue.append(cur_pos*B)
        visited[cur_pos*B] = visited[cur_pos] + 1
