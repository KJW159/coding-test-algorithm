# baekjoon_1978 소수 찾기

# v1
# import math
#
# def finding_prime_number(max_nume):
#
#     for i in range(2, int(math.sqrt(max_num))+1):
#         if arr[i]:
#             j = 2
#             while i*j <= max_num:
#                 if arr[i*j]:
#                     arr[i*j] = False
#                 j += 1
#
#
# N = int(input())
# nums = list(map(int, input().split()))
# max_num = max(nums)
# res = 0
# arr = [True for i in range(max_num+1)]
#
# finding_prime_number(max_num)
#
# for num in nums:
#     if arr[num] and num != 1:
#         res += 1
# print(res)

# v2
from math import *

def finding_prime_number(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True



N = int(input())
nums = list(map(int, input().split()))
res = 0
for num in nums:
    if finding_prime_number(num):
        res += 1

print(res)

