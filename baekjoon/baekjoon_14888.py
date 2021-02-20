# baekjonn_14888 연산자 끼워넣기
# import math
#
# def permutations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in permutations1(arr[:i]+arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
# N = int(input())
# nums = list(map(int, input().split()))
# operator_num = list(map(int, input().split()))
# res_max = - math.inf
# res_min = math.inf
#
# # 덧셈 0, 뺄셈 1, 곱셈 2, 나눗셈 3
# idx = 0
# operators = []
# for op_num in operator_num:
#     for i in range(op_num):
#         operators.append(idx)
#     idx += 1
#
#
# for op_group in permutations1(operators, N-1):
#     num1 = nums[0]
#     for i in range(N-1):
#         op = op_group[i]
#         num2 = nums[i+1]
#         if op == 0:
#             tmp = num1+num2
#         elif op == 1:
#             tmp = num1-num2
#         elif op == 2:
#             tmp = num1 * num2
#         else:
#             if num1 > 0:
#                 tmp = num1 // num2
#             if num1 < 0:
#                 tmp = -(abs(num1) // num2)
#         num1 = tmp
#     res_max = max(res_max, num1)
#     res_min = min(res_min, num1)
# print(res_max)
# print(res_min)

# v2
import math
import itertools


N = int(input())
nums = list(map(int, input().split()))
operator_num = list(map(int, input().split()))
res_max = - math.inf
res_min = math.inf

# 덧셈 0, 뺄셈 1, 곱셈 2, 나눗셈 3
idx = 0
operators = []
candidates = set()

for op_num in operator_num:
    for i in range(op_num):
        operators.append(idx)
    idx += 1

op_group_tmp = itertools.permutations(operators, N-1)
for op_tmp in op_group_tmp:
    candidates.add(op_tmp)

for op_group in candidates:
    num1 = nums[0]
    for i in range(N-1):
        op = op_group[i]
        num2 = nums[i+1]
        if op == 0:
            tmp = num1+num2
        elif op == 1:
            tmp = num1-num2
        elif op == 2:
            tmp = num1 * num2
        else:
            if num1 > 0:
                tmp = num1 // num2
            if num1 < 0:
                tmp = -(abs(num1) // num2)
        num1 = tmp
    res_max = max(res_max, num1)
    res_min = min(res_min, num1)
print(res_max)
print(res_min)