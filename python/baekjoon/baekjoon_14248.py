# baekjoon_14248 점프 점프


# v1
from collections import deque

def bfs(start_rock):
    queue = deque()
    queue.append(start_rock)
    visited[start_rock] = 1

    cnt = 1

    while queue:
        cur_rock = queue.popleft()
        left_rock = cur_rock - jump_dist[cur_rock]
        right_rock = cur_rock + jump_dist[cur_rock]

        if 1 <= left_rock <= N and visited[left_rock] == 0:
            queue.append(left_rock)
            visited[left_rock] = 1
            cnt += 1
        if 1 <= right_rock <= N and visited[right_rock] == 0:
            queue.append(right_rock)
            visited[right_rock] = 1
            cnt += 1
    return cnt


N = int(input())
jump_dist = [0]+list(map(int, input().split()))
start_rock = int(input())
visited = [0]*(N+1)


res = bfs(start_rock)
print(res)