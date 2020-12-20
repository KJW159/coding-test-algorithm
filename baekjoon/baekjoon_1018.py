# baekjoon_1018
import copy

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def check_color(i_x, j_y, color, x_s, x_e, y_s, y_e):
    cnt_tmp = 0
    for c in range(4):
        x = i_x+dx[c]
        y = j_y+dy[c]
        if x_s <= x < x_e and y_s <= y < y_e:
            if color == arr_tmp[x][y] and color == 'W':
                arr_tmp[x][y] = 'B'
                cnt_tmp += 1
            elif color == arr_tmp[x][y] and color == 'B':
                arr_tmp[x][y] = 'W'
                cnt_tmp += 1
    return cnt_tmp

M, N = list(map(int, input().split()))
arr = [list(input()) for k in range(M)]


i_s = 0
j_s = 0
min_cnt = M * N
if 8 <= M <= 50 and 8 <= N <= 50:
    for i_s in range(M):
        for j_s in range(N):
            if 0 <= i_s+7 < M and 0 <= j_s+7 < N:
                for k in range(2):
                    arr_tmp = copy.deepcopy(arr)
                    cnt = 0
                    x_s, x_e = i_s, i_s+8
                    y_s, y_e = j_s, j_s+8
                    if k == 1 and arr_tmp[x_s][y_s] == 'W':
                        arr_tmp[x_s][y_s] = 'B'
                        cnt += 1
                    elif k == 1 and arr_tmp[x_s][y_s] == 'B':
                        arr_tmp[x_s][y_s] = 'W'
                        cnt += 1
                    for i in range(x_s, x_e):
                        for j in range(y_s, y_e):
                            color = arr_tmp[i][j]
                            cnt += check_color(i, j, color, x_s, x_e, y_s, y_e)
                    if cnt < min_cnt:
                        min_cnt = cnt

    print(f'{min_cnt}')

