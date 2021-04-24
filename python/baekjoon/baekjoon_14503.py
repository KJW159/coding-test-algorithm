# baekjoon_14503 로봇청소기

# v1
# def checking_left(r_i,r_j,direction, rotating):
#     x = r_i + dx[direction]
#     y = r_j + dy[direction]
#     trg_tmp = False
#     if 0 <= x < N and 0 <= y < M:
#         if visited[x][y] == 0 and room[x][y] == 0:
#             trg_tmp = True
#     if direction-1 < 0:
#         direction = 4
#     return trg_tmp, [x ,y, direction, rotating]
#
#
# def moving_backward(r_i, r_j, direction, rotating):
#     move_tmp = False
#     bx = 0
#     by = 0
#     if direction == 0:
#         bx = r_i + dx[3]
#         by = r_j + dy[3]
#     elif direction == 1:
#         bx = r_i + dx[0]
#         by = r_j + dy[0]
#     elif direction == 2:
#         bx = r_i + dx[1]
#         by = r_j + dy[1]
#     elif direction == 3:
#         bx = r_i + dx[2]
#         by = r_j + dy[2]
#
#     if 0 <= bx < N and 0 <= by < M:
#         if room[bx][by] == 0:
#             move_tmp = True
#             return move_tmp, [bx, by, direction, rotating]
#     return move_tmp, [r_i, r_j, direction, rotating]
#
# N, M = map(int, input().split())
# robot = list(map(int, input().split()))
# room = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# rotating = 0
# robot.append(rotating)
#
# stack = []
# stack.append(robot)
# visited[robot[0]][robot[1]] = 1
# clean_cnt = 1
#
# # 해당 방향(인덱스)에 따른 탐색 방향
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
#
# while stack:
#     r_i, r_j, direction, rotating = stack.pop()
#     clean, robot = checking_left(r_i, r_j, direction, rotating)
#     if clean:
#         robot[2] -= 1
#         robot[3] = 0
#         stack.append(robot)
#         visited[robot[0]][robot[1]] = 1
#         clean_cnt += 1
#     if not clean and robot[3] < 4:
#         rotating += 1
#         if direction-1 < 0:
#             direction = 4
#         stack.append([r_i, r_j, direction-1, rotating])
#     if not clean and robot[3] == 4:
#         rotating = 0
#         move, robot = moving_backward(r_i, r_j, direction, rotating)
#         if move:
#             stack.append(robot)
#         else:
#             break
# print(clean_cnt)

# v2
#
# def checking_left(r_i,r_j,direction, rotating):
#     x = r_i + dx[direction]
#     y = r_j + dy[direction]
#     trg_tmp = False
#     if 0 <= x < N and 0 <= y < M:
#         if visited[x][y] == 0 and room[x][y] == 0:
#             trg_tmp = True
#     if direction-1 < 0:
#         direction = 4
#     return trg_tmp, [x ,y, direction, rotating]
#
#
# def moving_backward(r_i, r_j, direction, rotating):
#     move_tmp = False
#     back_d = (direction + 3) % 4
#     bx = r_i + dx[back_d]
#     by = r_j + dy[back_d]
#
#     if 0 <= bx < N and 0 <= by < M:
#         if room[bx][by] == 0:
#             move_tmp = True
#             return move_tmp, [bx, by, direction, rotating]
#     return move_tmp, [r_i, r_j, direction, rotating]
#
# N, M = map(int, input().split())
# robot = list(map(int, input().split()))
# room = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# rotating = 0
# robot.append(rotating)
#
# stack = []
# stack.append(robot)
# visited[robot[0]][robot[1]] = 1
# clean_cnt = 1
#
# # 해당 방향(인덱스)에 따른 탐색 방향
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
#
# while stack:
#     r_i, r_j, direction, rotating = stack.pop()
#     clean, robot = checking_left(r_i, r_j, direction, rotating)
#     if clean:
#         robot[2] -= 1
#         robot[3] = 0
#         stack.append(robot)
#         visited[robot[0]][robot[1]] = 1
#         clean_cnt += 1
#     if not clean and robot[3] < 4:
#         rotating += 1
#         if direction-1 < 0:
#             direction = 4
#         stack.append([r_i, r_j, direction-1, rotating])
#     if not clean and robot[3] == 4:
#         rotating = 0
#         move, robot = moving_backward(r_i, r_j, direction, rotating)
#         if move:
#             stack.append(robot)
#         else:
#             break
# print(clean_cnt)

# v3

# def dfs(robot):
#     r_i, r_j, direction = robot
#     stack = [robot]
#     visited[r_i][r_j] = 1
#     cnt_tmp = 1
#
#     while stack:
#         r_i, r_j, direction = stack.pop()
#         for c in range(4):
#             x = r_i + dx[rotation[direction]]
#             y = r_j + dy[rotation[direction]]
#             if 0 <= x < N and 0 <= y < M:
#                 if visited[x][y] == 0 and room[x][y] == 0:
#                     stack.append([x, y, rotation[direction]])
#                     visited[x][y] = 1
#                     cnt_tmp += 1
#                     break
#             direction = rotation[direction]
#             if c == 3:
#                 backward = (direction + 2) % 4
#                 bx = r_i + dx[backward]
#                 by = r_j + dy[backward]
#                 if 0 <= bx < N and 0 <= by < M:
#                     if room[bx][by] == 1:
#                         return cnt_tmp
#
#                     if room[bx][by] == 0:
#                         stack.append([bx, by, direction])
#
# N, M = map(int, input().split())
# robot = list(map(int, input().split()))
# room = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
#
# rotation = [3,0,1,2]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# clean_cnt = dfs(robot)
# print(clean_cnt)


# re-v1

# def cleaning():
#     stack = []
#     stack.append(robot)
#     arr[robot[0]][robot[1]] = 2
#     cnt = 1
#     r_cnt = 0
#
#     while stack:
#         r, c, d = stack.pop()
#         if r_cnt == 4:
#             d_tmp = (d+2) % 4
#         else:
#             d_tmp = (d+3) % 4
#         x = r + dx[d_tmp]
#         y = c + dy[d_tmp]
#         if 0 <= x < N and 0 <= y < M:
#             if r_cnt < 4:
#                 if arr[x][y] == 0:
#                     stack.append([x,y,d_tmp])
#                     cnt += 1
#                     arr[x][y] = 2
#                     r_cnt = 0
#                 if arr[x][y] != 0:
#                     stack.append([r,c,d_tmp])
#                     r_cnt += 1
#             if r_cnt == 4:
#                 if arr[x][y] == 2 or arr[x][y] == 0:
#                     stack.append([x,y,d_tmp])
#                 if arr[x][y] == 1:
#                     return cnt
#     return cnt
#
# N, M = map(int, input().split())
#
# # r,c,d
# robot = list(map(int, input().split()))
#
# # 0 공간 1 벽 2 청소함
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# # 0 상, 1 오, 2 하, 3 좌
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# res = cleaning()
# print(res)



# re-v2
# def cleaning():
#     stack = []
#     stack.append(robot)
#     arr[robot[0]][robot[1]] = 2
#     cnt = 1
#     r_cnt = 0
#
#     while stack:
#         r, c, d = stack.pop()
#         if r_cnt == 3:
#             d_tmp = (d+2) % 4
#         else:
#             d_tmp = (d+3) % 4
#         x = r + dx[d_tmp]
#         y = c + dy[d_tmp]
#         if 0 <= x < N and 0 <= y < M:
#             if r_cnt == 3:
#                 if arr[x][y] != 1:
#                     stack.append([x,y,d])
#                     r_cnt = 0
#                 else:
#                     return cnt
#             else:
#                 if arr[x][y] == 0:
#                     stack.append([x,y,d_tmp])
#                     cnt += 1
#                     arr[x][y] = 2
#                     r_cnt = 0
#                 if arr[x][y] != 0:
#                     stack.append([r,c,d_tmp])
#                     r_cnt += 1
#     return cnt
#
# N, M = map(int, input().split())
#
# # r,c,d
# robot = list(map(int, input().split()))
#
# # 0 공간 1 벽 2 청소함
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# # 0 상, 1 오, 2 하, 3 좌
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# res = cleaning()
# print(res)


# re-v3
# def cleaning():
#     stack = []
#     stack.append(robot)
#     arr[robot[0]][robot[1]] = 2
#     cnt = 1
#
#     while stack:
#         r, c, d = stack.pop()
#         x = r
#         y = c
#         d_tmp = d
#         for i in range(4):
#             d_tmp = (d_tmp+3) % 4
#             nx = x + dx[d_tmp]
#             ny = y + dy[d_tmp]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if arr[nx][ny] == 0:
#                     stack.append([nx, ny, d_tmp])
#                     cnt += 1
#                     arr[nx][ny] = 2
#                     break
#
#             if i == 3:
#                 d_tmp2 = d_tmp
#                 d_tmp = (d_tmp+2) % 4
#                 nx = x + dx[d_tmp]
#                 ny = y + dy[d_tmp]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if arr[nx][ny] != 1:
#                         stack.append([nx, ny, d_tmp2])
#                     if arr[nx][ny] == 1:
#                         return cnt
#
#     return cnt
#
# N, M = map(int, input().split())
#
# # r,c,d
# robot = list(map(int, input().split()))
#
# # 0 공간 1 벽 2 청소함
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# # 0 상, 1 오, 2 하, 3 좌
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# res = cleaning()
# print(res)


# re-v4
# def cleaning():
#     stack = []
#     stack.append(robot)
#     arr[robot[0]][robot[1]] = 2
#     cnt = 1
#
#     while stack:
#         r, c, d = stack.pop()
#         for i in range(4):
#             d = (d+3) % 4
#             nx = r + dx[d]
#             ny = c + dy[d]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if arr[nx][ny] == 0:
#                     stack.append([nx, ny, d])
#                     cnt += 1
#                     arr[nx][ny] = 2
#                     break
#
#             if i == 3:
#                 d_tmp = d
#                 d = (d+2) % 4
#                 nx = r + dx[d]
#                 ny = c + dy[d]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if arr[nx][ny] != 1:
#                         stack.append([nx, ny, d_tmp])
#                     if arr[nx][ny] == 1:
#                         return cnt
#
#     return cnt
#
# N, M = map(int, input().split())
#
# # r,c,d
# robot = list(map(int, input().split()))
#
# # 0 공간 1 벽 2 청소함
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# # 0 상, 1 오, 2 하, 3 좌
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# print(cleaning())

# re-v5

def cleaning(robot):
    cnt = 0

    while True:
        r_i, r_j, r_d = robot
        if room[r_i][r_j] == 0:
            room[r_i][r_j] = 2
            cnt += 1
        for i in range(4):
            # r_d = (r_d+1) % 4
            r_d = (r_d + 3) % 4
            r_x = r_i + dx[r_d]
            r_y = r_j + dy[r_d]
            if room[r_x][r_y] == 0:
                robot = [r_x, r_y, r_d]
                break
            if i == 3:
                r_d2 = (r_d+2)%4
                r_x = r_i + dx[r_d2]
                r_y = r_j + dy[r_d2]
                if room[r_x][r_y] == 1:
                    return cnt
                else:
                    robot = [r_x, r_y, r_d]

N, M = map(int, input().split())

robot = list(map(int, input().split()))
room = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

print(cleaning(robot))















