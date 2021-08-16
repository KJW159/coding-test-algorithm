# baekjoon_11497 통나무 건너뛰기


# v1
# import math
#
#
# def permutations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in permutations1(arr[:i]+arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     logs = list(map(int, input().split()))
#     res = math.inf
#     for log_per in permutations1(logs, N):
#         jump_level = 0
#         for i in range(N-1):
#             level_tmp1 = abs(log_per[i-1]-log_per[i])
#             level_tmp2 = abs(log_per[i+1]-log_per[i])
#             jump_level = max(jump_level, level_tmp1, level_tmp2)
#         if jump_level < res:
#             res = jump_level
#     print(res)


# v2
# import math
#
#
# def permutations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in permutations1(arr[:i]+arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     logs = list(map(int, input().split()))
#     res = math.inf
#     for log_per in permutations1(logs, N):
#         jump_level = 0
#         for i in range(N):
#             level_tmp1 = abs(log_per[i-1]-log_per[i])
#             jump_level = max(jump_level, level_tmp1)
#         if jump_level < res:
#             res = jump_level
#     print(res)



# v3
# import math, sys
#
# input = sys.stdin.readline
#
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     logs = list(map(int, input().split()))
#     res = math.inf
#
#     for i in range(N):
#         jump_level = 0
#         for j in range(N):
#             if i == j:
#                 continue
#             jump_level = max(jump_level, abs(logs[i]-logs[j]))
#         if jump_level < res:
#             res = jump_level
#     print(res)


# v4
T = int(input())
for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    res = 0

    for i in range(2, N):
        res = max(res, abs(logs[i]-logs[i-2]))
    print(res)