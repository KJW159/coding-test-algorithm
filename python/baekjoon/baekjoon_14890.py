# # baekjoon_14890 경사로
#
# #v1
#
# def finding_path(k):
#     global res
#     if k == 0 or k == 1:
#         arr_shape = 1
#     if k == 2 or k == 3:
#         arr_shape = 2
#
#     for i in range(N):
#         slope_cnt = 0
#         slope = False
#         for j in range(N-1):
#             if arr[i][j] == arr[i][j + 1]:
#                 if slope:
#                     if slope_cnt < L:
#                         slope_cnt += 1
#                     if slope_cnt == L:
#                         slope = False
#                         slope_cnt = 0
#                         if j + 1 == N - 1 and [i, arr_shape] not in path:
#                             res += 1
#                             path.append([i, arr_shape])
#                 else:
#                     if j + 1 == N - 1 and [i, arr_shape] not in path:
#                         res += 1
#                         path.append([i, arr_shape])
#                     continue
#             elif (arr[i][j] - arr[i][j + 1]) == 1:
#                 if slope:
#                     # if slope_cnt != 0:
#                     break
#                 if not slope:
#                     if slope_cnt == 0:
#                         slope = True
#             else:
#                 break
#
#
# def finding_path_back(k):
#     global res
#     if k == 0 or k == 1:
#         arr_shape = 1
#     if k == 2 or k == 3:
#         arr_shape = 2
#
#     for i in range(N):
#         slope_cnt = 0
#         slope = False
#         for j in range(N-1, 0, -1):
#             if arr[i][j] == arr[i][j-1]:
#                 if slope:
#                     if slope_cnt < L:
#                         slope_cnt += 1
#                     if slope_cnt == L:
#                         slope = False
#                         slope_cnt = 0
#                         if j-1 == 0 and [i, arr_shape] not in path:
#                             res += 1
#                             path.append([i, arr_shape])
#                 else:
#                     if j-1 == 0 and [i, arr_shape] not in path:
#                         res += 1
#                         path.append([i, arr_shape])
#                     continue
#             elif (arr[i][j] - arr[i][j-1]) == 1:
#                 if slope:
#                     # if slope_cnt != 0:
#                     break
#                 if not slope:
#                     if slope_cnt == 0:
#                         slope = True
#             else:
#                 break
#
#
# N, L = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# path = []
#
# start = 0
# end = N
# step = 1
#
# for k in range(4):
#
#     if k == 0 or k == 2:
#         if k == 2:
#             arr = list(zip(*arr))
#         finding_path(k)
#     if k == 1 or k == 3:
#         finding_path_back(k)
# print(res)

# v2

def checking_move(row_tmp):
    slope = [False for _ in range(N)]
    for i in range(N-1):
        if row_tmp[i] == row_tmp[i+1]:
            continue
        if abs(row_tmp[i] - row_tmp[i+1]) > 1:
            return False
        if row_tmp[i] > row_tmp[i+1]:
            height = row_tmp[i+1]
            for j in range(i+1, i+1+L):
                if 0 <= j < N:
                    if row_tmp[j] != height:
                        return False
                    if slope[j]:
                        return False
                    if row_tmp[j] == height and not slope[j]:
                        slope[j] = True
                else:
                    return False
        else:
            height = row_tmp[i]
            for j in range(i, i-L,-1):
                if 0 <= j < N:
                    if row_tmp[j] != height:
                        return False
                    if slope[j]:
                        return False
                    if row_tmp[j] == height and not slope[j]:
                        slope[j] = True
                else:
                    return False
    return True

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0
for k in range(2):
    for row in arr:
        if checking_move(row):
            res += 1
    arr = list(zip(*arr))
print(res)





