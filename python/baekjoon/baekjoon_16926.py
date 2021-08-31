# baekjoon_16926 배열 돌리기1

# v1
# def rotating_arr():
#     for k in range(0, N // 2):
#         start_tmp = arr[k][k]
#         for j1 in range(k, M - k - 1):
#             arr[k][j1] = arr[k][j1 + 1]
#         for i1 in range(k, N - 1 - k):
#             arr[i1][M - 1 - k] = arr[i1 + 1][M - 1 - k]
#         for j2 in range(M - 1 - k, k, -1):
#             arr[N - 1 - k][j2] = arr[N - 1 - k][j2 - 1]
#         for i2 in range(N - 2 - k, k, -1):
#             arr[i2 + 1][k] = arr[i2][k]
#         arr[k + 1][k] = start_tmp
#
#
# N, M, R = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# for _ in range(R):
#     rotating_arr()
# for i in range(N):
#     print(*arr[i])


# v2
def rotating_arr():

    for k in range(0, min(N,M)//2):
        start_tmp = arr[k][k]
        for j1 in range(k, M-k-1):
            arr[k][j1] = arr[k][j1+1]
        for i1 in range(k, N-1-k):
            arr[i1][M-1-k] = arr[i1+1][M-1-k]
        for j2 in range(M-1-k, k, -1):
            arr[N-1-k][j2] = arr[N-1-k][j2-1]
        for i2 in range(N-2-k, k, -1):
            arr[i2+1][k] = arr[i2][k]
        arr[k+1][k] = start_tmp


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    rotating_arr()
for i in range(N):
    print(*arr[i])