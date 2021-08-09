# baekjoon_9020 골드바흐의 추측

# v1
# from math import sqrt
#
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = [1]*(N+1)
#     prime_a = 0
#     prime_b = 0
#     diff = N
#
#
#     for i in range(2, int(sqrt(N))+1):
#         if arr[i] == 1:
#             j = 2
#             while i*j <= N:
#                 arr[i*j] = 0
#                 j += 1
#
#     for i in range(2, N):
#         if arr[i] == 1:
#             num_a = i
#             num_b = N - num_a
#             if arr[num_b] == 1:
#                 diff_tmp = abs(num_a - num_b)
#                 if diff_tmp < diff:
#                     diff = diff_tmp
#                     if num_a < num_b:
#                         prime_a, prime_b = num_a, num_b
#                     else:
#                         prime_a, prime_b = num_b, num_a
#
#
#     print("{} {}".format(prime_a, prime_b))


# v2
# from math import sqrt
#
#
# T = int(input())
# nums = []
# max_num = 0
# for _ in range(T):
#     N = int(input())
#     if max_num < N:
#         max_num = N
#     nums.append(N)
#
#
# arr = [1]*(max_num+1)
# for i in range(2, int(sqrt(max_num)) + 1):
#     if arr[i] == 1:
#         j = 2
#         while i * j <= max_num:
#             arr[i * j] = 0
#             j += 1
#
# for num in nums:
#     prime_a = 0
#     prime_b = 0
#     diff = num
#     for i in range(2, num):
#
#         if arr[i] == 1:
#             num_a = i
#             num_b = num - num_a
#             if arr[num_b] == 1:
#                 diff_tmp = abs(num_a - num_b)
#                 if diff_tmp < diff:
#                     diff = diff_tmp
#                     if num_a < num_b:
#                         prime_a, prime_b = num_a, num_b
#                     else:
#                         prime_a, prime_b = num_b, num_a
#
#     print("{} {}".format(prime_a, prime_b))


# v3
from math import sqrt


T = int(input())
nums = []
max_num = 0
for _ in range(T):
    N = int(input())
    if max_num < N:
        max_num = N
    nums.append(N)


arr = [1]*(max_num+1)
for i in range(2, int(sqrt(max_num)) + 1):
    if arr[i] == 1:
        j = 2
        while i * j <= max_num:
            arr[i * j] = 0
            j += 1

for num in nums:
    prime_a = 0
    prime_b = 0
    diff = num
    for i in range(2, (num//2)+1):
        if arr[i] == 1:
            num_a = i
            num_b = num - num_a
            if arr[num_b] == 1:
                diff_tmp = abs(num_a - num_b)
                if diff_tmp < diff:
                    diff = diff_tmp
                    if num_a < num_b:
                        prime_a, prime_b = num_a, num_b
                    else:
                        prime_a, prime_b = num_b, num_a

    print("{} {}".format(prime_a, prime_b))
