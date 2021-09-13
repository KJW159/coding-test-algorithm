# baekjoon_5549 행성탐사


# v1
# 정글(J) 0, 바다(O) 1, 얼음(I) 2

import sys

input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())

arr = [list(input()) for _ in range(M)]
prefix_sum = [[[0,0,0] for _ in range(N+1)] for __ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        if arr[i-1][j-1] == 'J':
            c_tmp = 0
        elif arr[i-1][j-1] == 'O':
            c_tmp = 1
        elif arr[i-1][j-1] == 'I':
            c_tmp = 2

        for c in range(3):
            num_tmp = 0
            if c_tmp == c:
                num_tmp = 1
            prefix_sum[i][j][c] = prefix_sum[i-1][j][c] + prefix_sum[i][j-1][c] - prefix_sum[i-1][j-1][c] + num_tmp


for _ in range(K):
    a, b, c, d = map(int, input().split())
    res = []
    for k in range(3):
        res.append(prefix_sum[c][d][k] - prefix_sum[c][b-1][k] - prefix_sum[a-1][d][k] + prefix_sum[a-1][b-1][k])
    print(*res)




