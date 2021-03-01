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



import math
def moving(x,y,direction):
    global res
    curr = arr[x][y]
    total_dust = 0
    for c in range(9):
        if direction == 0:
            nx = x + left[c][0]
            ny = y + left[c][1]
            dust = math.floor(left[c][2]*0.01*curr)
            total_dust += dust
            if 0 <= nx < N and 0 <= ny <N:
                arr[nx][ny] += dust
            else:
                res += dust
        elif direction == 1:
            nx = x + down[c][0]
            ny = y + down[c][1]
            dust = math.floor(down[c][2] * 0.01 * curr)
            total_dust += dust
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += dust
            else:
                res += dust
        elif direction == 2:
            nx = x + right[c][0]
            ny = y + right[c][1]
            dust = math.floor(right[c][2] * 0.01 * curr)
            total_dust += dust
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += dust
            else:
                res += dust
        else:
            nx = x + up[c][0]
            ny = y + up[c][1]
            dust = math.floor(up[c][2] * 0.01 * curr)
            total_dust += dust
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += dust
            else:
                res += dust
    dust_a = curr-total_dust
    ax = x+dx[direction]
    ay = y+dy[direction]
    if 0 <= ax < N and 0 <= ay < N:
        arr[ax][ay] += dust_a
    else:
        res += dust_a


# 왼쪽(0), 5,10,7,1,2, a
left = [(0,-2,5),(-1,-1,10),(-1,0,7),(-1,1,1),(-2,0,2),(1,-1,10),(1,0,7),(1,1,1),(2,0,2)]
# 아래쪽(1)
down = [(2,0,5),(1,-1,10),(0,-1,7),(-1,-1,1),(0,-2,2),(1,1,10),(0,1,7),(-1,1,1),(0,2,2)]
# 오른쪽(2)
right = [(0,2,5),(-1,1,10),(-1,0,7),(-1,-1,1),(-2,0,2),(1,1,10),(1,0,7),(1,-1,1),(2,0,2)]
# 위쪽(3)
up = [(-2,0,5),(-1,-1,10),(0,-1,7),(1,-1,1),(0,-2,2),(-1,1,10),(0,1,7),(1,1,1),(0,2,2)]


dx = [0,1,0,-1]
dy = [-1,0,1,0]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
s_i = N//2
s_j = N//2

idx = 1
res = 0
trg = False
while True:
    if idx % 2:
        for i in range(2):
            if trg:
                break
            for _ in range(idx):
                past = arr[s_i][s_j]
                x = s_i + dx[i]
                y = s_j + dy[i]
                if 0 <= x < N and 0 <= y < N:
                    moving(x,y,i)
                    if x == 0 and y == 0:
                        trg = True
                        break
                    arr[x][y] = past
                    s_i, s_j = x, y

    else:
        for i in range(2, 4):
            if trg:
                break
            for _ in range(idx):
                past = arr[s_i][s_j]
                x = s_i + dx[i]
                y = s_j + dy[i]
                if 0 <= x < N and 0 <= y < N:
                    moving(x,y,i)
                    if x == 0 and y == 0:
                        trg = True
                        break
                    arr[x][y] = past
                    s_i, s_j = x, y
    if trg:
        break
    idx +=1
print(res)


