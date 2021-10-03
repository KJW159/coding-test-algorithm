# baekjoon_10799 쇠막대기

# v1처럼 닫을때마다 stack 에 남아있는 괄호를 더해주려고 하니 중보되는 곳이 있음.
# v2에서는 닫는 괄호를 만났을때 바로 전 괄호가 여는 괄호였는지 확인해서 레이저인지
# 아니면 쇠막대기가 끝난 건지 확인함.

# v1
# brackets = list(input())
# stack = []
# res = 0
# for bracket in brackets:
#     if bracket == '(':
#         stack.append('(')
#     else:
#         stack.pop()
#         res += len(stack)
# print(res)

# v2
import sys

input = sys.stdin.readline

brackets = list(input().strip())
stack = [brackets[0]]
res = 0
for i in range(1, len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if brackets[i-1] == '(':
            res += len(stack)
        else:
            res += 1
print(res)