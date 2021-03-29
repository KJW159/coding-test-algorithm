# baekjoon_14499 주사위 굴리기

# v1
# N,M, s_x, s_y, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# orders = list(map(int, input().split()))
#
# dice_value = [0]*7
# side_num = [0,3,4,2,5]
# # 현재 윗면 아랫면
# current = [1,6]
#
# # 오른쪽 1, 왼쪽 2, 위쪽 3, 아랫쪽 4
# dx = [0,0,0,-1,1]
# dy = [0,1,-1,0,0]
#
# def moving(order):
#     bottom_tmp = side_num[order]
#     top_tmp = 7-bottom_tmp
#     side_num[order] = current[0]
#     if order == 1:
#         side_num[2] = current[1]
#     elif order == 2:
#         side_num[1] =  current[1]
#     elif order == 3:
#         side_num[4] = current[1]
#     elif order == 4:
#         side_num[3] = current[1]
#     current[0] = top_tmp
#     current[1] = bottom_tmp
#
# for order in orders:
#     x = s_x + dx[order]
#     y = s_y + dy[order]
#     if 0 <= x < N and 0 <= y < M:
#         moving(order)
#         if arr[x][y] == 0:
#             arr[x][y] = dice_value[current[1]]
#         else:
#             dice_value[current[1]] = arr[x][y]
#             arr[x][y] = 0
#         print(dice_value[current[0]])
#         s_x, s_y = x, y


# v2
N,M, s_x, s_y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

dice_value = [0]*7
side_num = [0,3,4,2,5]
# 현재 윗면 아랫면
current = [1,6]

# 오른쪽 1, 왼쪽 2, 위쪽 3, 아랫쪽 4
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

def moving(order):
    bottom_tmp = side_num[order]
    top_tmp = 7-bottom_tmp
    side_num[order] = current[0]
    if order == 1:
        side_num[2] = current[1]
    elif order == 2:
        side_num[1] =  current[1]
    elif order == 3:
        side_num[4] = current[1]
    elif order == 4:
        side_num[3] = current[1]
    current[0] = top_tmp
    current[1] = bottom_tmp

for order in orders:
    x = s_x + dx[order]
    y = s_y + dy[order]
    if 0 <= x < N and 0 <= y < M:
        moving(order)
        if arr[x][y] == 0:
            arr[x][y] = dice_value[current[1]]
        else:
            dice_value[current[1]] = arr[x][y]
            arr[x][y] = 0
        s_x, s_y = x, y
        print(dice_value[current[0]])
    else:
        continue