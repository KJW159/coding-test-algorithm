# baekjoon_9461 파도반 수열

# v1 재귀

# def padovan_seq(N):
#     if N == 0:
#         return 0
#     if N == 1:
#         dp[1] = 1
#         return dp[1]
#     if N == 2:
#         dp[2] = 1
#         return dp[2]
#     if N >= 3:
#         if dp[N] > 0:
#             return dp[N]
#         else:
#             dp[N] = padovan_seq(N-3) + padovan_seq(N-2)
#             return dp[N]
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     dp = [0]*101
#     res = padovan_seq(N)
#     print(res)


# v2 for문

T = int(input())
for tc in range(T):
    N = int(input())
    dp = [0]*101
    dp[1] = 1
    dp[2] = 1
    for n in range(3, N+1):
        dp[n] = dp[n-3] + dp[n-2]

    print(dp[N])