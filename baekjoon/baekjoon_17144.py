# baekjoon_17144 미세먼지 안녕!

# v1
# def spreading_dust(s_i, s_j):
#     spreaded_dust = room[s_i][s_j]//5
#     spreading_cnt = 0
#     for c in range(4):
#         x = s_i + dx[c]
#         y = s_j + dy[c]
#         if 0 <= x < R and 0 <= y < C and room[x][y] != -1:
#             room_tmp[x][y] += spreaded_dust
#             spreading_cnt += 1
#     room[s_i][s_j] -= (spreaded_dust*spreading_cnt)
#
#
# def moving_dust(k):
#     a_i, a_j = air_cleaners[k]
#     x, y = a_i, a_j
#     dust_curr = 0
#     while True:
#         dust_tmp = dust_curr
#         if y == C - 1:
#             break
#         y += 1
#         if room[x][y] >= 0:
#             dust_curr = room[x][y]
#         room[x][y] = dust_tmp
#
#     while True:
#         dust_tmp = dust_curr
#         if k == 0:
#             if x == 0:
#                 break
#             x -= 1
#         elif k == 1:
#             if x == R-1:
#                 break
#             x += 1
#         if room[x][y] >= 0:
#             dust_curr = room[x][y]
#         room[x][y] = dust_tmp
#
#     while True:
#         dust_tmp = dust_curr
#         if y == 0:
#             break
#         y -= 1
#         if room[x][y] >= 0:
#             dust_curr = room[x][y]
#         room[x][y] = dust_tmp
#
#     while True:
#         dust_tmp = dust_curr
#         # if x == a_i and y == a_j:
#         #     break
#         if k == 0:
#             x += 1
#         elif k == 1:
#             x -= 1
#
#         if room[x][y] >= 0:
#             dust_curr = room[x][y]
#
#         if x == a_i and y == a_j:
#             break
#         else:
#             room[x][y] = dust_tmp
#
#
# R, C, T = map(int, input().split())
# room = [list(map(int, input().split())) for _ in range(R)]
# air_cleaners = []
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# for i in range(R):
#     if room[i][0] == -1:
#         air_cleaners.append([i,0])
#
# for t in range(T):
#     room_tmp = [[0]*C for _ in range(R)]
#     # 미세먼지 확산
#     for i in range(R):
#         for j in range(C):
#             if room[i][j] > 0:
#                 spreading_dust(i,j)
#     # 미세먼지 갱신
#     for i in range(R):
#         for j in range(C):
#             if room_tmp[i][j] > 0 and room[i][j] != -1:
#                 room[i][j] += room_tmp[i][j]
#
#     # 바람
#     for k in range(2):
#         moving_dust(k)
# res = 0
# for i in range(R):
#     for j in range(C):
#         if room[i][j] > 0:
#             res += room[i][j]
# print(res)


# v2
def spreading_dust(s_i, s_j):
    spreaded_dust = room[s_i][s_j]//5
    spreading_cnt = 0
    for c in range(4):
        x = s_i + dx[c]
        y = s_j + dy[c]
        if 0 <= x < R and 0 <= y < C and room[x][y] != -1:
            room_tmp[x][y] += spreaded_dust
            spreading_cnt += 1
    room[s_i][s_j] -= (spreaded_dust*spreading_cnt)


def moving_dust(k):
    a_i, a_j = air_cleaners[k]
    pre_dust= 0
    if k == 0:
        for j in range(a_j+1,C):
            room[a_i][j], pre_dust = pre_dust, room[a_i][j]
        for i in range(a_i-1,-1,-1):
            room[i][C-1], pre_dust = pre_dust, room[i][C-1]
        for j in range(C-2, -1, -1):
            room[0][j], pre_dust = pre_dust, room[0][j]
        for i in range(1, a_i):
            room[i][0], pre_dust = pre_dust, room[i][0]
    else:
        for j in range(a_j+1, C):
            room[a_i][j], pre_dust = pre_dust, room[a_i][j]
        for i in range(a_i+1,R):
            room[i][C-1], pre_dust = pre_dust, room[i][C-1]
        for j in range(C-2, -1, -1):
            room[R-1][j], pre_dust = pre_dust, room[R-1][j]
        for i in range(R-2, a_i, -1):
            room[i][0], pre_dust = pre_dust, room[i][0]


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
air_cleaners = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(R):
    if room[i][0] == -1:
        air_cleaners.append([i,0])

for t in range(T):
    room_tmp = [[0]*C for _ in range(R)]
    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                spreading_dust(i,j)
    # 미세먼지 갱신
    for i in range(R):
        for j in range(C):
            if room_tmp[i][j] > 0 and room[i][j] != -1:
                room[i][j] += room_tmp[i][j]

    # 바람
    for k in range(2):
        moving_dust(k)
res = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            res += room[i][j]
print(res)