# 프로그래머스 - 두 정수 사이의 합

# v1
# def solution(a, b):
#     res = 0
#     if a == b:
#         res = a
#     else:
#         if a > b:
#             tmp = a
#             a = b
#             b = tmp
#         for i in range(a,b+1):
#             res += i
#     return res

# v2
def solution(a, b):
    res = 0
    if a == b:
        res = a
    else:
        if a > b:
            a,b = b, a
        for i in range(a,b+1):
            res += i
    return res