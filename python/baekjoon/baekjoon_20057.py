# baekjoon_20057 마법사 상어와 토네이도
# import math
# def moving(x,y,direction):
#     curr = arr[x][y]
#     total_dust = 0
#     res_tmp = 0
#     for c in range(9):
#         if direction == 0:
#             nx = x + left[c][0]
#             ny = y + left[c][1]
#             dust = math.floor(left[c][2]*0.01*curr)
#             total_dust += dust
#             if 0 <= nx < N and 0 <= ny <N:
#                 arr[nx][ny] += dust
#             else:
#                 if x == 0 and y == 0:
#                     res_tmp += dust
#         elif direction == 1:
#             nx = x + down[c][0]
#             ny = y + down[c][1]
#             dust = math.floor(down[c][2] * 0.01 * curr)
#             total_dust += dust
#             if 0 <= nx < N and 0 <= ny < N:
#                 arr[nx][ny] += dust
#             else:
#                 if x == 0 and y == 0:
#                     res_tmp += dust
#         elif direction == 2:
#             nx = x + right[c][0]
#             ny = y + right[c][1]
#             dust = math.floor(right[c][2] * 0.01 * curr)
#             total_dust += dust
#             if 0 <= nx < N and 0 <= ny < N:
#                 arr[nx][ny] += dust
#             else:
#                 if x == 0 and y == 0:
#                     res_tmp += dust
#         else:
#             nx = x + up[c][0]
#             ny = y + up[c][1]
#             dust = math.floor(up[c][2] * 0.01 * curr)
#             total_dust += dust
#             if 0 <= nx < N and 0 <= ny < N:
#                 arr[nx][ny] += dust
#             else:
#                 if x == 0 and y == 0:
#                     res_tmp += dust
#     dust_a = curr-total_dust
#     ax = x+dx[direction]
#     ay = y+dy[direction]
#     if 0 <= ax < N and 0 <= ay < N:
#         arr[ax][ay] += dust_a
#     else:
#         if x == 0 and y == 0:
#             res_tmp += arr[ax][ay]
#             print(res_tmp, arr[x][y])
#     return res_tmp
#
# # 왼쪽(0), 5,10,7,1,2, a
# left = [(0,-2,5),(-1,-1,10),(-1,0,7),(-1,1,1),(-2,0,2),(1,-1,10),(1,0,7),(1,1,1),(2,0,2)]
# # 아래쪽(1)
# down = [(2,0,5),(1,-1,10),(0,-1,7),(-1,-1,1),(0,-2,2),(1,1,10),(0,1,7),(-1,1,1),(0,2,2)]
# # 오른쪽(2)
# right = [(0,2,5),(-1,1,10),(-1,0,7),(-1,-1,1),(-2,0,2),(1,1,10),(1,0,7),(1,-1,1),(2,0,2)]
# # 위쪽(3)
# up = [(-2,0,5),(-1,-1,10),(0,-1,7),(1,-1,1),(0,-2,2),(-1,1,10),(0,1,7),(1,1,1),(0,2,2)]
#
#
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]
# s_i = N//2
# s_j = N//2
#
# idx = 1
# res = 0
# while True:
#     if idx % 2:
#         for i in range(2):
#             if res:
#                 break
#             for _ in range(idx):
#                 past = arr[s_i][s_j]
#                 x = s_i + dx[i]
#                 y = s_j + dy[i]
#                 if 0 <= x < N and 0 <= y < N:
#                     res = moving(x,y,i)
#                     if res:
#                         break
#                     arr[x][y] = past
#                     s_i, s_j = x, y
#
#     else:
#         for i in range(2, 4):
#             if res:
#                 break
#             for _ in range(idx):
#                 past = arr[s_i][s_j]
#                 x = s_i + dx[i]
#                 y = s_j + dy[i]
#                 if 0 <= x < N and 0 <= y < N:
#                     res = moving(x,y,i)
#                     if res:
#                         break
#                     arr[x][y] = past
#                     s_i, s_j = x, y
#     if res:
#         break
#     idx +=1
# print(res)


# v2
# import math
# def moving(x,y,direction):
#     global res
#     curr = arr[x][y]
#     total_dust = 0
#     for c in range(9):
#         if direction == 0:
#             nx = x + left[c][0]
#             ny = y + left[c][1]
#             dust = math.floor(left[c][2]*0.01*curr)
#             total_dust += dust
#             if 0 <= nx < N and 0 <= ny <N:
#                 arr[nx][ny] += dust
#             else:
#                 res += dust
#         elif direction == 1:
#             nx = x + down[c][0]
#             ny = y + down[c][1]
#             dust = math.floor(down[c][2] * 0.01 * curr)
#             total_dust += dust
#             if 0 <= nx < N and 0 <= ny < N:
#                 arr[nx][ny] += dust
#             else:
#                 res += dust
#         elif direction == 2:
#             nx = x + right[c][0]
#             ny = y + right[c][1]
#             dust = math.floor(right[c][2] * 0.01 * curr)
#             total_dust += dust
#             if 0 <= nx < N and 0 <= ny < N:
#                 arr[nx][ny] += dust
#             else:
#                 res += dust
#         else:
#             nx = x + up[c][0]
#             ny = y + up[c][1]
#             dust = math.floor(up[c][2] * 0.01 * curr)
#             total_dust += dust
#             if 0 <= nx < N and 0 <= ny < N:
#                 arr[nx][ny] += dust
#             else:
#                 res += dust
#     dust_a = curr-total_dust
#     ax = x+dx[direction]
#     ay = y+dy[direction]
#     if 0 <= ax < N and 0 <= ay < N:
#         arr[ax][ay] += dust_a
#     else:
#         res += dust_a
#
#
# # 왼쪽(0), 5,10,7,1,2, a
# left = [(0,-2,5),(-1,-1,10),(-1,0,7),(-1,1,1),(-2,0,2),(1,-1,10),(1,0,7),(1,1,1),(2,0,2)]
# # 아래쪽(1)
# down = [(2,0,5),(1,-1,10),(0,-1,7),(-1,-1,1),(0,-2,2),(1,1,10),(0,1,7),(-1,1,1),(0,2,2)]
# # 오른쪽(2)
# right = [(0,2,5),(-1,1,10),(-1,0,7),(-1,-1,1),(-2,0,2),(1,1,10),(1,0,7),(1,-1,1),(2,0,2)]
# # 위쪽(3)
# up = [(-2,0,5),(-1,-1,10),(0,-1,7),(1,-1,1),(0,-2,2),(-1,1,10),(0,1,7),(1,1,1),(0,2,2)]
#
#
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]
# s_i = N//2
# s_j = N//2
#
# idx = 1
# res = 0
# trg = False
# while True:
#     if idx % 2:
#         for i in range(2):
#             if trg:
#                 break
#             for _ in range(idx):
#                 past = arr[s_i][s_j]
#                 x = s_i + dx[i]
#                 y = s_j + dy[i]
#                 if 0 <= x < N and 0 <= y < N:
#                     moving(x,y,i)
#                     if x == 0 and y == 0:
#                         trg = True
#                         break
#                     arr[x][y] = past
#                     s_i, s_j = x, y
#
#     else:
#         for i in range(2, 4):
#             if trg:
#                 break
#             for _ in range(idx):
#                 past = arr[s_i][s_j]
#                 x = s_i + dx[i]
#                 y = s_j + dy[i]
#                 if 0 <= x < N and 0 <= y < N:
#                     moving(x,y,i)
#                     if x == 0 and y == 0:
#                         trg = True
#                         break
#                     arr[x][y] = past
#                     s_i, s_j = x, y
#     if trg:
#         break
#     idx +=1
# print(res)


# re-v1
# import math
#
# N = int(input())
# sand = [list(map(int, input().split())) for _ in range(N)]
#
# # 왼쪽0, 아래1, 오른쪽2, 위3
# wind_direction = [
#     [(0,-2,0.05),(-1,-1,0.1),(1,-1,0.1),(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,1,0.01),(1,1,0.01),(0,-1,0)],
#     [(2,0,0.05),(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(1,-1,0.1),(1,1,0.1),(1,0,0)],
#     [(0,2,0.05),(-1,-1,0.01),(1,-1,0.01),(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,1,0.1),(1,1,0.1),(0,1,0)],
#     [(-2,0,0.05),(-1,-1,0.1),(-1,1,0.1),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(1,-1,0.01),(1,1,0.01),(-1,0,0)],
#
# ]
# # 왼쪽0, 아래1, 오른쪽2, 위3
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
#
# start_x = N//2
# start_y = N//2
# res = 0
# i = 0
# trg = False
# while True:
#     i += 1
#     # 홀수, 왼쪽, 아래
#     if i % 2 == 1:
#         d_1 = 0
#         d_2 = 1
#     # 짝수, 오른쪽, 위
#     else:
#         d_1 = 2
#         d_2 = 3
#     for j in range(d_1, d_2+1):
#         # 이동, k는 이동 칸수
#         for k in range(i):
#             x = start_x + dx[j]
#             y = start_y + dy[j]
#             # 비율 있는 곳
#             if 0 <= x < N and 0 <= y < N:
#                 sand_y = sand[x][y]
#                 sand_tmp = 0
#                 for w in range(9):
#                     nx = x + wind_direction[j][w][0]
#                     ny = y + wind_direction[j][w][1]
#                     moving_sand = math.floor(wind_direction[j][w][2] * sand_y)
#                     # moving_sand = int(wind_direction[j][w][2] * sand_y)
#                     sand_tmp += moving_sand
#                     if 0 <= nx < N and 0 <= ny < N:
#                         sand[nx][ny] += moving_sand
#                     else:
#                         res += moving_sand
#                 # 알파
#                 nx = x + wind_direction[j][9][0]
#                 ny = y + wind_direction[j][9][1]
#                 sand_a = sand_y - sand_tmp
#                 if 0 <= nx < N and 0 <= ny < N:
#                     sand[nx][ny] += sand_a
#                 else:
#                     res += sand_a
#                 sand[x][y] = sand[start_x][start_y]
#                 start_x, start_y = x, y
#             if start_x == 0 and start_y == 0:
#                 trg = True
#                 break
#         if trg:
#             break
#     if trg:
#         break
# print(res)


# re-v2


import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 좌, 하, 우, 상 순서. 8까지 비율, 9는 a임.
sand_rate = [
    [(0,-2,0.05),(-1,-1,0.1),(1,-1,0.1),(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,1,0.01),(1,1,0.01),(0,-1)],
    [(2,0,0.05),(1,-1,0.1),(1,1,0.1),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(-1,-1,0.01),(-1,1,0.01),(1,0)],
    [(0,2,0.05),(-1,1,0.1),(1,1,0.1),(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),(0,1)],
    [(-2,0,0.05),(-1,-1,0.1),(-1,1,0.1),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(1,-1,0.01),(1,1,0.01),(-1,0)]
]

s_x, s_y = N//2, N//2
res = 0
trg = False
for i in range(1, N+1):
    if i % 2 == 1:
        start = 0
        end = 2
    else:
        start = 2
        end = 4
    # 좌,하 , 상,우 정해줌.
    for j in range(start, end):
        # 아래는 이동 칸 수만큼 for문 돌림.
        for k in range(i):
            moving_sand = 0
            x = s_x + dx[j]
            y = s_y + dy[j]
            sand_x = arr[s_x][s_y]
            sand_y = arr[x][y]
            for c in range(9):
                nx = x + sand_rate[j][c][0]
                ny = y + sand_rate[j][c][1]
                sand_tmp = int(sand_y * sand_rate[j][c][2])
                if 0 <= nx < N and 0 <= ny < N:
                    arr[nx][ny] += sand_tmp
                else:
                    res += sand_tmp
                moving_sand += sand_tmp
            nx = x + sand_rate[j][9][0]
            ny = y + sand_rate[j][9][1]
            sand_a = sand_y - moving_sand
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += sand_a
            else:
                res += sand_a
            arr[x][y] = sand_x
            arr[s_x][s_y] = 0
            s_x, s_y = x, y
            if s_x == 0 and s_y == 0:
                trg = True
                break
        if trg:
            break
    if trg:
        break
print(res)












































