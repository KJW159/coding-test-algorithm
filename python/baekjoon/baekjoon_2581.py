# baekjoon_2581 소수


# v1
# from math import sqrt
#
#
# def finding_prime_num(num):
#     for i in range(2, int(sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True
#
#
# M = int(input())
# N = int(input())
#
# res = 0
# min_prime_num = 0
#
# for i in range(M, N+1):
#     if finding_prime_num(i) and i != 1:
#         if res == 0:
#             min_prime_num = i
#         res += i
#
# if res == 0:
#     print(-1)
# else:
#     print(res)
#     print(min_prime_num)


# v2
from math import sqrt


def findind_prime_num():

    for i in range(2, int(sqrt(N))+1):
        if arr[i]:
            j = 2
            while i*j <= N:
                arr[i*j] = False
                j += 1

M = int(input())
N = int(input())

res = 0
min_prime_num = 0

arr = [True for _ in range(N+1)]
findind_prime_num()


for num in range(M, N+1):
    if num == 1:
        continue
    if arr[num]:
        if res == 0:
            min_prime_num = num
        res += num

if res == 0:
    print(-1)
else:
    print(res)
    print(min_prime_num)
