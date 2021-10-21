# swea_1247 최적 경로

# v1

def dfs(cnt, x, y, distance):
    global res
    if distance > res:
        return
    if cnt == N:
        dist_tmp = distance + abs(x-home[0]) + abs(y-home[1])
        if dist_tmp < res:
            res = dist_tmp
        return

    for i in range(N):
        if visited[i] == 0:
            dist_tmp = abs(x-position[i][0]) + abs(y-position[i][1])
            visited[i] = 1
            dfs(cnt+1, position[i][0], position[i][1], distance+dist_tmp)
            visited[i] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    position_tmp = list(map(int, input().split()))
    company = [position_tmp[0], position_tmp[1]]
    home = [position_tmp[2], position_tmp[3]]
    res = 987654321
    position = []
    for i in range(4, len(position_tmp)-1, 2):
        position.append([position_tmp[i], position_tmp[i+1]])

    visited = [0]*N
    dfs(0, company[0], company[1], 0)
    print("#{} {}".format(t, res))