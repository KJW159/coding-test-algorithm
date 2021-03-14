# baekjoon_17140 이차원 배열과 연산
# v1
# def r_operation():
#     max_row_len = 0
#     N = len(arr[0])
#     for i in range(N):
#         max_num = max(arr[i])
#         counts = [[i,0] for i in range(max_num+1)]
#         new_row = []
#         for num in arr[i]:
#             counts[num][1] += 1
#         counts.sort(key=lambda x: (x[0],x[1]))
#         for j in range(max_num+1):
#             if counts[j][0] == 0 or counts[j][1] == 0:
#                 continue
#             new_row.extend(counts[j])
#         new_row_len = len(new_row)
#         if new_row_len >= 100:
#             new_row = new_row[:100]
#         arr[i] = new_row
#         max_row_len = max(max_row_len, new_row_len)
#     # 0 채우기.
#     for i in range(N):
#         len_gap = max_row_len-len(arr[i])
#         if len_gap != 0:
#             arr[i].extend([0]*len_gap)
#
# def c_operation():
#     max_col_len = 0
#     M = len(arr)
#     N = len(arr[0])
#     for i in range(N):
#         col = []
#         max_num = 0
#         for j in range(M):
#             col.append(arr[j][i])
#             max_num = max(max_num, arr[j][i])
#         counts = [[i, 0] for i in range(max_num + 1)]
#         new_col = []
#         for num in col:
#             counts[num][1] += 1
#         counts.sort(key=lambda x: (x[0],x[1]))
#         for x in range(max_num+1):
#             if counts[x][0] == 0 or counts[x][1] == 0:
#                 continue
#             new_col.extend(counts[x])
#         new_col_len = len(new_col)
#         if new_col_len >= 100:
#             new_col = new_col[:100]
#         max_col_len = max(max_col_len, new_col_len)
#         for j in range()
#
#
#
# r,c,k = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(3)]
#
# cnt = 0
# while True:
#     if len(arr[0]) >= len(arr):
#         r_operation()
#         cnt += 1
#     if len(arr[0]) < len(arr):
#         c_operation()
#         cnt += 1
#     if arr[r-1][c-1] == k:
#         break
# print(cnt)



# v2
def operation(operation, arr):
    if operation == 1:
        arr = list(zip(*arr))
    max_len = 0
    N = len(arr)
    for i in range(N):
        max_num = max(arr[i])
        counts = [[x,0] for x in range(max_num+1)]
        new_row = []
        for num in arr[i]:
            counts[num][1] += 1
        counts.sort(key=lambda x: (x[1], x[0]))
        for j in range(max_num+1):
            if counts[j][0] == 0 or counts[j][1] == 0:
                continue
            new_row.extend(counts[j])
        new_row_len = len(new_row)
        if new_row_len >= 100:
            new_row = new_row[:100]
        arr[i] = new_row
        max_len = max(max_len, new_row_len)
    # 0 채우기.
    for i in range(N):
        len_gap = max_len-len(arr[i])
        if len_gap != 0:
            arr[i].extend([0]*len_gap)
    if operation == 1:
        arr = list(zip(*arr))

    return arr

r,c,k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]

cnt = 0
while True:
    if 0<= r-1 < len(arr) and 0<= c-1 < len(arr[0]):
        if arr[r-1][c-1] == k:
            break
    if len(arr) >= len(arr[0]):
        arr = operation(0, arr)
        cnt += 1
    elif len(arr) < len(arr[0]):
        arr = operation(1, arr)
        cnt += 1
    if cnt > 100:
        cnt = -1
        break

print(cnt)