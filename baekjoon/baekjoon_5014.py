# baekjoon_5014 스타트링크
import collections


F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)

queue = collections.deque()
queue.append([S, 0])
visited[S] = 1
res = "use the stairs"

while queue:
    floor, step = queue.popleft()
    if floor == G:
        res = step
        break
    floor1 = floor + U
    if floor1 <= F and visited[floor1] == 0:
        queue.append([floor1, step+1])
        visited[floor1] = 1
    floor2 = floor - D
    if floor2 >= 1 and visited[floor2] == 0:
        queue.append([floor2, step+1])
        visited[floor2] = 1

print(res)