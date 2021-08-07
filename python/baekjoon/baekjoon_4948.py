# baekjoon_4948 베르트랑 공준


# v1
# import sys, math
#
# input = sys.stdin.readline
#
# while True:
#     N = int(input())
#     if not N:
#         break
#     arr = [True for i in range((2*N)+1)]
#
#     res = 0
#     for i in range(2, int(math.sqrt(2*N))+1):
#         if arr[i]:
#             j = 2
#             while i * j <= 2*N:
#                 if arr[i*j]:
#                     arr[i*j] = False
#                 j += 1
#     for i in range(N+1, (2*N)+1):
#         if arr[i] and i != 1:
#             res += 1
#     print(res)


# v2
# import sys, math
#
# input = sys.stdin.readline
#
# arr = [True for i in range((2 * 123456) + 1)]
# for i in range(2, int(math.sqrt(2 * 123456)) + 1):
#     if arr[i]:
#         j = 2
#         while i * j <= 2 * 123456:
#             if arr[i * j]:
#                 arr[i * j] = False
#             j += 1
#
# while True:
#     N = int(input())
#     if not N:
#         break
#     res = 0
#
#     for i in range(N+1, (2*N)+1):
#         if arr[i] and i != 1:
#             res += 1
#     print(res)


# v3
import sys, math

input = sys.stdin.readline

arr = [True for i in range((2 * 123456) + 1)]
for i in range(2, int(math.sqrt(2 * 123456)) + 1):
    if arr[i]:
        j = 2
        while i * j <= 2 * 123456:
            if arr[i * j]:
                arr[i * j] = False
            j += 1

while True:
    N = int(input())
    if not N:
        break
    res = 0

    for i in range(N + 1, (2 * N) + 1):
        if arr[i]:
            res += 1
    print(res)