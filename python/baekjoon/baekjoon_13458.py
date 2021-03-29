# baekjoon_13458 시험 감독

# v1
# import math
#
# N = int(input())
# A = list(map(int, input().split()))
# B, C = map(int, input().split())
# supervisor = 0
#
# for i in range(len(A)):
#     if A[i] <= B:
#         supervisor += 1
#         continue
#     supervisor += 1
#     sub_num = math.ceil((A[i] - B) / C)
#     supervisor += sub_num
# print(supervisor)

# v2
import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
supervisor = 0

for i in range(len(A)):
    supervisor += 1
    if A[i] <= B:
        continue

    sub_num = math.ceil((A[i] - B) / C)
    supervisor += sub_num
print(supervisor)
