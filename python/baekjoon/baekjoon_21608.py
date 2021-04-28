# baekjoon_21608 상어 초등학교

# v1
# from collections import deque
#
# N = int(input())
# total_num = N*N
# room = [[0]*N for _ in range(N)]
# wanted_std = [[] for _ in range(total_num+1)]
# std_position = [[] for _ in range(total_num+1)]
# std_list = deque()
# for _ in range(total_num):
#     std_num, w1, w2, w3, w4 = map(int, input().split())
#     wanted_std[std_num] = [w1,w2,w3,w4]
#     std_list.append(std_num)
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# happy = [0,1,10,100,1000]
# for i in range(total_num):
#     std = std_list[i]
#     if i == 0:
#         room[1][1] = std
#         std_position[std] = [1,1]
#     else:
#         near_position = []
#         for w_std in wanted_std[std]:
#             # 좋아하는 친구가 앉아 있으면 주변의 빈 공간 찾기.
#             if std_position[w_std]:
#                 w_x, w_y = std_position[w_std]
#                 for c in range(4):
#                     x = w_x + dx[c]
#                     y = w_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             near_position.append([x,y])
#         position_tmp = []
#         if near_position:
#             # 좋아하는 친구 근처 빈 공간의 상하좌우 체크하기.
#             for z_x, z_y in near_position:
#                 w_std_cnt = 0
#                 zero_cnt = 0
#                 for c in range(4):
#                     x = z_x + dx[c]
#                     y = z_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             zero_cnt += 1
#                         if room[x][y] in wanted_std[std]:
#                             w_std_cnt += 1
#                 position_tmp.append([w_std_cnt, zero_cnt, z_x, z_y])
#         else:
#         # # 좋아하는 친구 있는 경우.
#         # if position_tmp:
#         #     position_tmp.sort(key = lambda x: (-x[0],-x[1], x[2], x[3]))
#             for nx in range(N):
#                 for ny in range(N):
#                     zero_cnt = 0
#                     if room[nx][ny] == 0:
#                         for c in range(4):
#                             x = nx + dx[c]
#                             y = ny + dy[c]
#                             if 0 <= x < N and 0 <= y < N:
#                                 if room[nx][ny] == 0:
#                                     zero_cnt += 1
#                         position_tmp.append([0, zero_cnt, nx, ny])
#         if position_tmp:
#             position_tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
#             p1,p2,p3,p4 = position_tmp[0]
#             room[p3][p4] = std
#             std_position[std] = [p3,p4]
#
# res = 0
# for s_x in range(N):
#     for s_y in range(N):
#         std = room[s_x][s_y]
#         cnt = 0
#         for c in range(4):
#             x = s_x + dx[c]
#             y = s_y + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if room[x][y] in wanted_std[std]:
#                     cnt += 1
#         res += happy[cnt]
# print(res)


# v2
# from collections import deque
#
# N = int(input())
# total_num = N*N
# room = [[0]*N for _ in range(N)]
# wanted_std = [[] for _ in range(total_num+1)]
# std_position = [[] for _ in range(total_num+1)]
# std_list = deque()
# for _ in range(total_num):
#     std_num, w1, w2, w3, w4 = map(int, input().split())
#     wanted_std[std_num] = [w1,w2,w3,w4]
#     std_list.append(std_num)
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# happy = [0,1,10,100,1000]
# for i in range(total_num):
#     std = std_list[i]
#     if i == 0:
#         room[1][1] = std
#         std_position[std] = [1,1]
#     else:
#         near_position = []
#         for w_std in wanted_std[std]:
#             # 좋아하는 친구가 앉아 있으면 주변의 빈 공간 찾기.
#             if std_position[w_std]:
#                 w_x, w_y = std_position[w_std]
#                 for c in range(4):
#                     x = w_x + dx[c]
#                     y = w_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             near_position.append([x,y])
#         position_tmp = []
#         if near_position:
#             # 좋아하는 친구 근처 빈 공간의 상하좌우 체크하기.
#             for z_x, z_y in near_position:
#                 w_std_cnt = 0
#                 zero_cnt = 0
#                 for c in range(4):
#                     x = z_x + dx[c]
#                     y = z_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             zero_cnt += 1
#                         if room[x][y] in wanted_std[std]:
#                             w_std_cnt += 1
#                 position_tmp.append([w_std_cnt, zero_cnt, z_x, z_y])
#         else:
#             for nx in range(N):
#                 for ny in range(N):
#                     zero_cnt = 0
#                     if room[nx][ny] == 0:
#                         for c in range(4):
#                             x = nx + dx[c]
#                             y = ny + dy[c]
#                             if 0 <= x < N and 0 <= y < N:
#                                 if room[x][y] == 0:
#                                     zero_cnt += 1
#                         position_tmp.append([0, zero_cnt, nx, ny])
#         if position_tmp:
#             position_tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
#             p1,p2,p3,p4 = position_tmp[0]
#             room[p3][p4] = std
#             std_position[std] = [p3,p4]
#
# res = 0
# for s_x in range(N):
#     for s_y in range(N):
#         std = room[s_x][s_y]
#         cnt = 0
#         for c in range(4):
#             x = s_x + dx[c]
#             y = s_y + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if room[x][y] in wanted_std[std]:
#                     cnt += 1
#         res += happy[cnt]
# print(res)


# # v3- 실수 버전
#
# from collections import deque
#
# N = int(input())
# total_num = N*N
# room = [[0]*N for _ in range(N)]
# wanted_std = [[] for _ in range(total_num+1)]
# std_position = [[] for _ in range(total_num+1)]
# std_list = deque()
# for _ in range(total_num):
#     std_num, w1, w2, w3, w4 = map(int, input().split())
#     wanted_std[std_num] = [w1,w2,w3,w4]
#     std_list.append(std_num)
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# happy = [0,1,10,100,1000]
# for i in range(total_num):
#     std = std_list[i]
#     if i == 0:
#         room[1][1] = std
#         std_position[std] = [1,1]
#     else:
#         near_position = []
#         for w_std in wanted_std[std]:
#             if std_position[w_std]:
#                 w_x, w_y = std_position[w_std]
#                 for c in range(4):
#                     x = w_x + dx[c]
#                     y = w_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             near_position.append([x,y])
#         position_tmp = []
#         if near_position:
#             for z_x, z_y in near_position:
#                 w_std_cnt = 0
#                 zero_cnt = 0
#                 for c in range(4):
#                     x = z_x + dx[c]
#                     y = z_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             zero_cnt += 1
#                         if room[x][y] in wanted_std[std]:
#                             w_std_cnt += 1
#                 position_tmp.append([w_std_cnt, zero_cnt, z_x, z_y])
#         else:
#             for nx in range(N):
#                 for ny in range(N):
#                     zero_cnt = 0
#                     if room[nx][ny] == 0:
#                         for c in range(4):
#                             x = nx + dx[c]
#                             y = ny + dy[c]
#                             if 0 <= x < N and 0 <= y < N:
#                                 if room[x][y] == 0:
#                                     zero_cnt += 1
#                         position_tmp.append([0, zero_cnt, nx, ny])
#         if position_tmp:
#             position_tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
#             p1,p2,p3,p4 = position_tmp[0]
#             room[p3][p4] = std
#             std_position[std] = [p3,p4]
#
# res = 0
# for s_x in range(N):
#     for s_y in range(N):
#         std = room[s_x][s_y]
#         std1 = room[s_x][s_y]
#         cnt = 0
#         for c in range(4):
#             x = s_x + dx[c]
#             y = s_y + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 room1 = room[x][y]
#                 if room[x][y] in wanted_std[std]:
#                     cnt += 1
#         res += happy[cnt]
# print(res)

# v4
#
# from collections import deque
#
# N = int(input())
# total_num = N*N
# room = [[0]*N for _ in range(N)]
# wanted_std = [[] for _ in range(total_num+1)]
# std_position = [[] for _ in range(total_num+1)]
# std_list = deque()
# for _ in range(total_num):
#     std_num, w1, w2, w3, w4 = map(int, input().split())
#     wanted_std[std_num] = [w1,w2,w3,w4]
#     std_list.append(std_num)
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# happy = [0,1,10,100,1000]
# for i in range(total_num):
#     std = std_list[i]
#     if i == 0:
#         room[1][1] = std
#         std_position[std] = [1,1]
#     else:
#         near_position = set()
#         for w_std in wanted_std[std]:
#             if std_position[w_std]:
#                 w_x, w_y = std_position[w_std]
#                 for c in range(4):
#                     x = w_x + dx[c]
#                     y = w_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             near_position.add((x,y))
#         position_tmp = []
#         if near_position:
#             for z_x, z_y in near_position:
#                 w_std_cnt = 0
#                 zero_cnt = 0
#                 for c in range(4):
#                     x = z_x + dx[c]
#                     y = z_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             zero_cnt += 1
#                         if room[x][y] in wanted_std[std]:
#                             w_std_cnt += 1
#                 position_tmp.append([w_std_cnt, zero_cnt, z_x, z_y])
#         else:
#             for nx in range(N):
#                 for ny in range(N):
#                     zero_cnt = 0
#                     if room[nx][ny] == 0:
#                         for c in range(4):
#                             x = nx + dx[c]
#                             y = ny + dy[c]
#                             if 0 <= x < N and 0 <= y < N:
#                                 if room[x][y] == 0:
#                                     zero_cnt += 1
#                         position_tmp.append([0, zero_cnt, nx, ny])
#         if position_tmp:
#             position_tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
#             p1,p2,p3,p4 = position_tmp[0]
#             room[p3][p4] = std
#             std_position[std] = [p3,p4]
#
# res = 0
# for s_x in range(N):
#     for s_y in range(N):
#         std = room[s_x][s_y]
#         std1 = room[s_x][s_y]
#         cnt = 0
#         for c in range(4):
#             x = s_x + dx[c]
#             y = s_y + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 room1 = room[x][y]
#                 if room[x][y] in wanted_std[std]:
#                     cnt += 1
#         res += happy[cnt]
# print(res)


# v5
# from collections import deque
#
# N = int(input())
# total_num = N*N
# room = [[0]*N for _ in range(N)]
# wanted_std = [[] for _ in range(total_num+1)]
# std_position = [[] for _ in range(total_num+1)]
# std_list = deque()
# for _ in range(total_num):
#     std_num, w1, w2, w3, w4 = map(int, input().split())
#     wanted_std[std_num] = [w1,w2,w3,w4]
#     std_list.append(std_num)
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# happy = [0,1,10,100,1000]
# for i in range(total_num):
#     std = std_list[i]
#     if i == 0:
#         room[1][1] = std
#         std_position[std] = [1,1]
#     else:
#         near_position = set()
#         for w_std in wanted_std[std]:
#             if std_position[w_std]:
#                 w_x, w_y = std_position[w_std]
#                 for c in range(4):
#                     x = w_x + dx[c]
#                     y = w_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             near_position.add((x,y))
#         position_tmp = []
#         if near_position:
#             for z_x, z_y in near_position:
#                 w_std_cnt = 0
#                 zero_cnt = 0
#                 for c in range(4):
#                     x = z_x + dx[c]
#                     y = z_y + dy[c]
#                     if 0 <= x < N and 0 <= y < N:
#                         if room[x][y] == 0:
#                             zero_cnt += 1
#                         if room[x][y] in wanted_std[std]:
#                             w_std_cnt += 1
#                 position_tmp.append([w_std_cnt, zero_cnt, z_x, z_y])
#             position_tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
#         else:
#             for nx in range(N):
#                 for ny in range(N):
#                     zero_cnt = 0
#                     if room[nx][ny] == 0:
#                         for c in range(4):
#                             x = nx + dx[c]
#                             y = ny + dy[c]
#                             if 0 <= x < N and 0 <= y < N:
#                                 if room[x][y] == 0:
#                                     zero_cnt += 1
#                         position_tmp.append([0, zero_cnt, nx, ny])
#             position_tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
#         if position_tmp:
#             # position_tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
#             p1,p2,p3,p4 = position_tmp[0]
#             room[p3][p4] = std
#             std_position[std] = [p3,p4]
#
# res = 0
# for s_x in range(N):
#     for s_y in range(N):
#         std = room[s_x][s_y]
#         std1 = room[s_x][s_y]
#         cnt = 0
#         for c in range(4):
#             x = s_x + dx[c]
#             y = s_y + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 room1 = room[x][y]
#                 if room[x][y] in wanted_std[std]:
#                     cnt += 1
#         res += happy[cnt]
# print(res)


# v6
from collections import deque

N = int(input())
total_num = N*N
room = [[0]*N for _ in range(N)]
wanted_std = [[] for _ in range(total_num+1)]
std_position = [[] for _ in range(total_num+1)]
std_list = deque()
for _ in range(total_num):
    std_num, w1, w2, w3, w4 = map(int, input().split())
    wanted_std[std_num] = [w1,w2,w3,w4]
    std_list.append(std_num)

dx = [0,-1,0,1]
dy = [-1,0,1,0]
happy = [0,1,10,100,1000]
for i in range(total_num):
    std = std_list[i]
    if i == 0:
        room[1][1] = std
        # std_position[std] = [1,1]
    else:
        near_position = []
        for x in range(N):
            for y in range(N):
                if room[x][y] == 0:
                    std_cnt = 0
                    empty_cnt = 0
                    for c in range(4):
                        nx = x + dx[c]
                        ny = y + dy[c]
                        if 0 <= nx < N and 0 <= ny < N:
                            if room[nx][ny] == 0:
                                empty_cnt += 1
                            if room[nx][ny] in wanted_std[std]:
                                std_cnt += 1
                    near_position.append([std_cnt, empty_cnt,x,y])
        if near_position:
            near_position.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
            p1,p2,p3,p4 = near_position[0]
            room[p3][p4] = std
res = 0
for s_x in range(N):
    for s_y in range(N):
        std = room[s_x][s_y]
        # std1 = room[s_x][s_y]
        cnt = 0
        for c in range(4):
            x = s_x + dx[c]
            y = s_y + dy[c]
            if 0 <= x < N and 0 <= y < N:
                # room1 = room[x][y]
                if room[x][y] in wanted_std[std]:
                    cnt += 1
        res += happy[cnt]
print(res)





