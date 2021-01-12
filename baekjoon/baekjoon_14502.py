# baekjoon_14502 연구소
import sys
import collections

def comb(safety_zones, r):
    for n in range(len(safety_zones)):
        if r == 1:
            yield [safety_zones[n]]
        else:
            for next in comb(safety_zones[n+1:], r-1):
                yield [safety_zones[n]] + next

def virus_bfs(arr_copy):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    cnt  = 0

    queue = collections.deque()
    for virus in viruses:
        queue.append(virus)

    while queue:
        v_x, v_y = queue.popleft()
        for c in range(4):
            x = v_x + dx[c]
            y = v_y + dy[c]
            if 0 <= x < N and 0<= y < M:
                if arr_copy[x][y] == 0:
                    arr_copy[x][y] = 2
                    queue.append([x,y])
    for u in range(N):
        for v in range(M):
            if arr_copy[u][v] == 0:
                cnt += 1
    return cnt



def setting_wall(safety_zone):
    w1, w2, w3 = safety_zone
    arr_copy = [arr[i][:] for i in range(N)]

    arr_copy[w1[0]][w1[1]] = 1
    arr_copy[w2[0]][w2[1]] = 1
    arr_copy[w3[0]][w3[1]] = 1

    return virus_bfs(arr_copy)


N, M = map(int, input().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

safety_zones = []
viruses = []
safety_max = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            safety_zones.append([i,j])
        if arr[i][j] == 2:
            viruses.append([i,j])


for safety_zone in comb(safety_zones, 3):
    res_tmp = setting_wall(safety_zone)
    if res_tmp > safety_max:
        safety_max = res_tmp

print(safety_max)
