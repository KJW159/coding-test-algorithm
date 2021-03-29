# baekjoon_17779 게리맨더링2

#v1
# import math
#
# def marking_five(x,y,d1,d2, arr_tmp):
#     for i in range(x, x+d1+1):
#         for j in range(y, y-d1-1, -1):
#             arr_tmp[i][j] = 5
#     for i in range(x, x+d2+1):
#         for j in range(y, y+d2+1):
#             arr_tmp[i][j] = 5
#     for i in range(x+d1, x+d1+d2+1):
#         for j in range(y-d1, y-d1+d2+1):
#             arr_tmp[i][j] = 5
#     for i in range(x+d2, x+d1+d2):
#         for j in range(y+d2, y+d2-d1-1, -1):
#             arr_tmp[i][j] = 5
#
#
# def checking_area(x,y,d1,d2):
#     global res
#     people_num = [0]*(N+1)
#     arr_tmp = [[0]*N for _ in range(N)]
#     marking_five(x,y,d1,d2, arr_tmp)
#     for i in range(N):
#         for j in range(N):
#             if 0 <= i < x+d1 and 0 <= j <= y:
#                 if arr_tmp[i][j] == 5:
#                     break
#                 arr_tmp[i][j] = 1
#             if 0 <= i <= x+d2 and y < j < N:
#                 if arr_tmp[i][j] == 5:
#                     break
#                 arr_tmp[i][j] = 2
#             if x+d1 <= i < N and 0 <= j < y-d1+d2:
#                 if arr_tmp[i][j] == 5:
#                     break
#                 arr_tmp[i][j] = 3
#             if x+d2 < i < N and y-d1+d2 <= j < N:
#                 if arr_tmp[i][j] == 5:
#                     break
#                 arr_tmp[i][j] = 4
#     print(arr_tmp)
#     for i in range(N):
#         for j in range(N):
#             if arr_tmp[i][j] == 0 or arr_tmp[i][j] == 5:
#                 people_num[5] += arr[i][j]
#             else:
#                 people_num[arr_tmp[i][j]] += arr[i][j]
#     people_min = min(people_num)
#     people_max = max(people_num)
#     res = min(res, abs(people_max-people_min))
#
#
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# res = math.inf
# for x in range(N):
#     for y in range(N):
#         for d1 in range(N):
#             for d2 in range(N):
#                 if 0 <= x < x+d1+d2 < N and 0 <= y-d1 < y < y+d2 < N:
#                         checking_area(x,y,d1,d2)
# print(res)


# v2
# import math
#
# def marking_five(x,y,d1,d2, arr_tmp):
#     for i in range(d1+1):
#         arr_tmp[x+i][x-i] = 5
#         arr_tmp[x + d2 + i][y + d2 - i] = 5
#     for i in range(d2+1):
#         arr_tmp[x+i][y+i] = 5
#         arr_tmp[x + d1 + i][y - d1 + i] = 5
#
#
# def checking_area(x,y,d1,d2):
#     global res
#     people_num = [0]*(6)
#     arr_tmp = [[0]*(N+1) for _ in range(N+1)]
#     marking_five(x,y,d1,d2, arr_tmp)
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if 1 <= i < x+d1 and 1 <= j <= y:
#                 if arr_tmp[i][j] == 5:
#                     break
#                 arr_tmp[i][j] = 1
#             if 1 <= i <= x+d2 and y < j <= N:
#                 if arr_tmp[i][j] == 5:
#                     break
#                 arr_tmp[i][j] = 2
#             if x+d1 <= i <= N and 1 <= j < y-d1+d2:
#                 if arr_tmp[i][j] == 5:
#                     break
#                 arr_tmp[i][j] = 3
#             if x+d2 < i <= N and y-d1+d2 <= j <= N:
#                 if arr_tmp[i][j] == 5:
#                     break
#                 arr_tmp[i][j] = 4
#     for i in range(1,N+1):
#         for j in range(1, N+1):
#             if arr_tmp[i][j] == 0 or arr_tmp[i][j] == 5:
#                 people_num[5] += arr[i][j]
#             else:
#                 people_num[arr_tmp[i][j]] += arr[i][j]
#     people_min = min(people_num[1:])
#     people_max = max(people_num[1:])
#     res = min(res, abs(people_max-people_min))
#
#
#
#
# N = int(input())
# arr = [[]]
# for _ in range(N):
#     arr.append([0] + list(map(int, input().split())))
# res = math.inf
# for x in range(1, N+1):
#     for y in range(1, N+1):
#         for d1 in range(1, N+1):
#             for d2 in range(1, N+1):
#                 if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
#                         checking_area(x,y,d1,d2)
# print(res)

# # v3
# import math
#
# def marking_five(x,y,d1,d2, arr_tmp):
#     for i in range(d1+1):
#         arr_tmp[x+i][x-i] = 5
#         arr_tmp[x + d2 + i][y + d2 - i] = 5
#     for i in range(d2+1):
#         arr_tmp[x+i][y+i] = 5
#         arr_tmp[x + d1 + i][y - d1 + i] = 5
#
#
# def checking_area(x,y,d1,d2):
#     global res
#     people_num = [0]*6
#     arr_tmp = [[0]*(N+1) for _ in range(N+1)]
#     marking_five(x,y,d1,d2, arr_tmp)
#     for i in range(x+1, x+d1+d2):
#         trg = False
#         for j in range(1, N+1):
#             if arr_tmp[i][j] == 5:
#                 trg = not trg
#             if trg:
#                 arr_tmp[i][j] = 5
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#                 if 1 <= i < x+d1 and 1 <= j <= y and arr_tmp[i][j] == 0:
#                     people_num[1] += arr[i][j]
#                 if 1 <= i <= x+d2 and y < j <= N and arr_tmp[i][j] == 0:
#                     people_num[2] += arr[i][j]
#                 if x+d1 <= i <= N and 1 <= j < y-d1+d2 and arr_tmp[i][j] == 0:
#                     people_num[3] += arr[i][j]
#                 if x+d2 < i <= N and y-d1+d2 <= j <= N and arr_tmp[i][j] == 0:
#                     people_num[4] += arr[i][j]
#                 if arr_tmp[i][j] == 5:
#                     people_num[5] += arr[i][j]
#     people_min = min(people_num[1:])
#     people_max = max(people_num[1:])
#     res = min(res, people_max-people_min)
#
#
# N = int(input())
# arr = [[]]
# for _ in range(N):
#     arr.append([0] + list(map(int, input().split())))
# res = math.inf
# for x in range(1, N+1):
#     for y in range(1, N+1):
#         for d1 in range(1, N+1):
#             for d2 in range(1, N+1):
#                 if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
#                         checking_area(x,y,d1,d2)
# print(res)

# v4
import math

def marking_five(x,y,d1,d2, arr_tmp):
    for i in range(d1+1):
        arr_tmp[x+i][y-i] = 5
        arr_tmp[x + d2 + i][y + d2 - i] = 5
    for i in range(d2+1):
        arr_tmp[x+i][y+i] = 5
        arr_tmp[x + d1 + i][y - d1 + i] = 5


def checking_area(x,y,d1,d2):
    global res
    people_num = [0]*6
    arr_tmp = [[0]*(N+1) for _ in range(N+1)]
    marking_five(x,y,d1,d2, arr_tmp)
    for i in range(x+1, x+d1+d2):
        trg = False
        for j in range(1, N+1):
            if arr_tmp[i][j] == 5:
                trg = not trg
            if trg:
                arr_tmp[i][j] = 5
    for i in range(1, N+1):
        for j in range(1, N+1):
                if 1 <= i < x+d1 and 1 <= j <= y and arr_tmp[i][j] == 0:
                    people_num[1] += arr[i][j]
                if 1 <= i <= x+d2 and y < j <= N and arr_tmp[i][j] == 0:
                    people_num[2] += arr[i][j]
                if x+d1 <= i <= N and 1 <= j < y-d1+d2 and arr_tmp[i][j] == 0:
                    people_num[3] += arr[i][j]
                if x+d2 < i <= N and y-d1+d2 <= j <= N and arr_tmp[i][j] == 0:
                    people_num[4] += arr[i][j]
                if arr_tmp[i][j] == 5:
                    people_num[5] += arr[i][j]
    people_min = min(people_num[1:])
    people_max = max(people_num[1:])
    res = min(res, people_max-people_min)


N = int(input())
arr = [[]]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))
res = math.inf
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                        checking_area(x,y,d1,d2)
print(res)