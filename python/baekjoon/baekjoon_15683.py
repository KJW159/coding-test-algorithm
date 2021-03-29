# baekjoon_15683 감시

# 좌, 상, 우 ,하
dx = [0,-1,0,1]
dy = [-1,0,1,0]

directions = [[],[[0],[1],[2],[3]],
             [[0,2],[1,3]],
             [[1,2],[2,3],[0,3],[0,1]],
             [[1,2,3],[0,2,3],[0,1,3],[0,1,2]],
             [[0,1,2,3]]
             ]
def checking(cctv, arr_tmp, direction):
    s_i, s_j, cctv_num = cctv
    for d in direction:
        x = s_i
        y = s_j
        while True:
            x += dx[d]
            y += dy[d]
            if 0 <= x < N and 0 <= y < M:
                if arr_tmp[x][y] == 6:
                    break
                elif arr_tmp[x][y] == 0:
                    arr_tmp[x][y] = '#'
            else:
                break

def dfs(arr, cnt):
    global res
    if cnt == len(cctvs):
        space = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    space += 1
        res = min(res, space)
        return
    else:
        # arr_tmp = [arr[i][:] for i in range(N)]
        cctv = cctvs[cnt]
        for direction in directions[cctv[2]]:
            arr_tmp = [arr[i][:] for i in range(N)]
            checking(cctv, arr_tmp, direction)
            dfs(arr_tmp, cnt+1)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            cctvs.append([i,j,arr[i][j]])

res = N*M
dfs(arr, 0)
print(res)