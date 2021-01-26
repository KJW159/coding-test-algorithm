# baekjoon_1600 말이 되고픈 원숭이

import collections

def bfs(start, end, K):
    # 말
    hdx = [-1, -2, -2, -1, 1, 2, 2, 1]
    hdy = [-2, -1, 1, 2, 2, 1, -1, -2]
    # 원숭이
    mdx = [0,-1,0,1]
    mdy = [-1,0,1,0]

    queue = collections.deque()
    queue.append([start[0], start[1], 0])
    for i in range(K+1):
        visited[i][start[0]][start[1]] = 0
    res_tmp = -1

    while queue:
        s_i, s_j, k_cnt = queue.popleft()
        if s_i == end[1] and s_j == end[0]:
            res_tmp = visited[k_cnt][s_i][s_j]
            break

        if k_cnt+1 <= K:
            for h in range(8):
                hx = s_i + hdx[h]
                hy = s_j + hdy[h]
                if 0 <= hx < H and 0 <= hy < W:
                    if visited[k_cnt+1][hx][hy] == -1 and arr[hx][hy] == 0:
                        queue.append([hx, hy, k_cnt+1])
                        visited[k_cnt+1][hx][hy] = visited[k_cnt][s_i][s_j] + 1

        for m in range(4):
            mx = s_i + mdx[m]
            my = s_j + mdy[m]
            if 0 <= mx < H and 0 <= my < W:
                if visited[k_cnt][mx][my] == -1 and arr[mx][my] == 0:
                    queue.append([mx, my, k_cnt])
                    visited[k_cnt][mx][my] = visited[k_cnt][s_i][s_j] + 1
    return res_tmp


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
start = [0,0]
end = [W-1, H-1]
# index 는 K의 횟수
visited = [[[-1] * W for __ in range(H)] for ___ in range(K+1)]
res = bfs(start, end, K)
print(res)