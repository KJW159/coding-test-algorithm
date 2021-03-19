# baekjoon_16637 괄호 추가하기
import math

def dfs(idx, res_tmp):
    global res
    if idx == len(operators):
        res = max(res, int(res_tmp))
        return

    first_op = str(eval(res_tmp + operators[idx] + nums[idx+1]))
    dfs(idx+1, first_op)

    if idx + 1 < len(operators):
        second_op = str(eval(nums[idx+1] + operators[idx+1] + nums[idx + 2]))
        second_op = str(eval(res_tmp + operators[idx] + second_op))

        dfs(idx+2, second_op)

N = int(input())
expression = input()
nums, operators = [], []
res = -math.inf

for e in expression:
    if e.isdigit():
        nums.append(e)
    else:
        operators.append(e)

dfs(0, nums[0])

print(res)