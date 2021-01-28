# baekjoon_17135 캐슬 디펜스
from collections import deque

def combinations1(arr, r):
    for i in range(len(arr)):
        if r== 1:
            yield [arr[i]]
        else:
            for next in combinations1(arr[i+1:], r-1):
                yield [arr[i]] + next


def kill(archers, arr_copy, M,N):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    queue = deque()

    for n in range(len(N)):
        queue.append(archers)
        archer1, archer2, archer3 = archers
        visited = [[[0] * M for _ in range(N)] for __ in range(3)]
        visited[archer1[0]][archer1[1]] = 1
        visited[archer2[0]][archer2[1]] = 1
        visited[archer3[0]][archer3[1]] = 1

        while queue:
            archer1, archer2, archer3 = queue.popleft()
            for c in range(4):
                x =







N, M, D = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


archers_position = [(N,i) for i in range(M)]

for archers in combinations1(archers_position, 3):
    arr_copy =[arr[k][:] for k in range(N)]
    kill(archers, arr_copy,M,N)