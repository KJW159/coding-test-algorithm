# baekjoon_4889 안정적인 문자열


# v1

# tc = 0
# while True:
#     tc += 1
#     brackets = list(input())
#     if brackets[0] == '-':
#         break
#     stack = []
#     res = 0
#     for bracket in brackets:
#         if bracket == '}' and stack:
#             stack.pop()
#         elif bracket == '}' and not stack:
#             res += 1
#         if bracket == '{':
#             stack.append('{')
#     num = len(stack)
#     if num % 2 == 0:
#         res += num//2
#     else:
#         res += num % 2
#     print("{}. {}".format(tc, res))


# v2
# tc = 0
# while True:
#     tc += 1
#     brackets = list(input())
#     if not brackets:
#         print("{}. 0".format(tc))
#         continue
#     if brackets[0] == '-':
#         break
#     stack = []
#     res = 0
#     for bracket in brackets:
#         if bracket == '}' and stack:
#             stack.pop()
#         elif bracket == '}' and not stack:
#             res += 1
#         if bracket == '{':
#             stack.append('{')
#     num = len(stack)
#     if num % 2 == 0:
#         res += num//2
#     else:
#         res += num % 2
#     print("{}. {}".format(tc, res))


# v3
tc = 0
while True:
    tc += 1
    brackets = list(input())
    if brackets[0] == '-':
        break
    stack = []
    res = 0
    for bracket in brackets:
        if bracket == '}' and stack:
            stack.pop()
        elif bracket == '}' and not stack:
            res += 1
            stack.append('{')
        if bracket == '{':
            stack.append('{')
    res += len(stack)//2
    print("{}. {}".format(tc, res))