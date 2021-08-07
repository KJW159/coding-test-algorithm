# baekjoon_2312 수 복원하기.


# v1
# from math import sqrt
#
# T = int(input())
#
# arr = [1]*100001
# for i in range(2, int(sqrt(100000))+1):
#     if arr[i]:
#         j = 2
#         while i * j < 100000:
#             if arr[i*j]:
#                 arr[i*j] = 0
#             j += 1
#
# for _ in range(T):
#     N = int(input())
#     nums = [0]*(N+1)
#     num = N
#     trg = False
#
#     while True:
#         if trg:
#             break
#         for i in range(2, N+1):
#             if arr[i] and (num % arr[i]) == 0:
#                 nums[i] += 1
#                 num = num // i
#                 if arr[num]:
#                     nums[num] += 1
#                     trg = True
#                 break
#     for i in range(2, N+1):
#         if nums[i] != 0:
#             print("{} {}".format(i, nums[i]))


# v2

from math import sqrt



T = int(input())

arr = [1]*100001
for i in range(2, int(sqrt(100000))+1):
    if arr[i]:
        j = 2
        while i * j < 100000:
            if arr[i*j]:
                arr[i*j] = 0
            j += 1

for _ in range(T):
    N = int(input())
    nums = [0]*(N+1)
    num = N
    trg = False

    while True:
        if trg:
            break
        for i in range(2, N+1):
            if arr[i] and (num % i) == 0:
                nums[i] += 1
                num = num // i
                if arr[num]:
                    nums[num] += 1
                    trg = True
                break
    for i in range(2, N+1):
        if nums[i] != 0:
            print("{} {}".format(i, nums[i]))