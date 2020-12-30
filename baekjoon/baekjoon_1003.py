# baekjoon_1003 피보나치 함수

# v1
# def fibonacci(N):
#     if N == 0:
#         cnt[0] += 1
#         return 0
#     elif N == 1:
#         cnt[1] += 1
#         return 1
#     else:
#         return fibonacci(N-1) + fibonacci(N-2)

# v2
# def fibonacci(N):
#     if N == 0:
#         cnt[0] += 1
#         return 0
#     elif N == 1:
#         cnt[1] += 1
#         return 1
#     elif dp[N] != 0:
#         return dp[N]
#     else:
#         dp[N] = fibonacci(N - 1) + fibonacci(N - 2)
#         return dp[N]

# v3
#
# T = int(input())
#
# for tc in range(T):
#     N = int(input())
#     cnt = [1,0]
#     tmp = 0
#     for i in range(N):
#         tmp = cnt[1]
#         cnt[1] = cnt[0]+cnt[1]
#         cnt[0] = tmp
#     print("{} {}".format(cnt[0], cnt[1]))

# v4
def cal_num(N):
    if N == 0 or N == 1:
        return
    if N >= 2:
        for n in range(2, N+1):
            zero_cnt.append(zero_cnt[n-2] + zero_cnt[n-1])
            one_cnt.append(one_cnt[n-2] + one_cnt[n-1])
        return

T = int(input())

for tc in range(T):
    zero_cnt = [1,0]
    one_cnt = [0,1]
    N = int(input())
    cal_num(N)
    print("{} {}".format(zero_cnt[N], one_cnt[N]))





