# baekjoon_16953 A -> B


# v1
from collections import deque

def bfs(A, B):
    queue = deque()

    queue.append([A*2, 1])
    queue.append([int(str(A)+'1'), 1])

    while queue:
        num, cnt = queue.popleft()
        if num == B:
            return cnt
        if num < B:
            queue.append([num*2, cnt+1])
            queue.append([int(str(num)+'1'), cnt+1])
    return -1


A, B = map(int, input().split())
res = bfs(A, B)

if res != -1:
    print(res+1)
else:
    print(-1)