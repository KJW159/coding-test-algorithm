# baekjoon_19236 청소년 상어

#v1
# def moving_fish(fish):
#     fish_num, direction, f_i, f_j = fish
#     x = f_i + dx[direction]
#     y = f_j + dy[direction]
#     tmp = [0,0]
#     if 0 <= x < 4 and 0 <= y < 4:
#         if sea[x][y][0] < 17:
#             tmp[0] = sea[x][y][0]
#             tmp[1] = sea[x][y][1]
#
#             sea[x][y] = [fish_num, direction]
#             sea[f_i][f_j] = tmp
#             return
#     for i in range(1,8):
#         direction = (direction+i) % 8
#         x = f_i + dx[direction]
#         y = f_j + dy[direction]
#         if 0 <= x < 4 and 0 <= y < 4:
#             if sea[x][y][0] < 17:
#                 tmp[0] = sea[x][y][0]
#                 tmp[1] = sea[x][y][1]
#
#                 sea[x][y] = [fish_num, direction]
#                 sea[f_i][f_j] = tmp
#                 return
#
#
# sea = [[] for _ in range(4)]
# fish_input = [list(map(int,input().split())) for _ in range(4)]
# shark = [17, 0]
# fish_nums = []
# res = 0
# trg = [1,1]
# # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# dx = [2,-1,-1,0,1,1,1,0,-1]
# dy = [2,0,-1,-1,-1,0,1,1,1]
#
# for i in range(4):
#     for j in range(0,7,2):
#         a,b = fish_input[i][j:j+2]
#         sea[i].append([a,b])
#
# for i in range(4):
#     for j in range(4):
#         fish_nums.append([sea[i][j][0],sea[i][j][1],i,j])
# fish_nums.sort(key=lambda x:x[0])
#
#
# while True:
#     if sea[0][0][0]:
#         shark[1] = sea[0][0][1]
#         for i in range(len(fish_nums)):
#             if fish_nums[i][0] == sea[0][0][0]:
#                 fish_nums.pop(i)
#                 break
#         res += sea[0][0][0]
#     else:
#         trg[0] = 0
#     sea[0][0][0] = shark[0]
#     sea[0][0][1] = shark[1]
#
#     # 물고기 이동
#     for fish in fish_nums:
#         moving_fish(fish)
#
#     # 상어 이동
#     s_i, s_j = 0,0
#     while True:
#         s_x = s_i + dx[shark[1]]
#         s_y = s_j + dy[shark[1]]
#
#         if 0 <= s_x < 4 and 0 <= s_y < 4:
#             s_i = s_x
#             s_j = s_y
#             continue
#         else:
#             if sea[s_i][s_j][0]:
#                 res += sea[s_i][s_j][0]
#                 shark[1] = sea[s_i][s_j][1]
#                 sea[s_i][s_j] = [0,0]
#             else:
#                 trg[1] = 0
#         break
#     if trg[0] == 0 and trg[1] == 0:
#         break
#     else:
#         trg = [1,1]
#
# print(res)

# v2
# def moving_fish(fish):
#     fish_num, direction, f_i, f_j = fish
#     x = f_i + dx[direction]
#     y = f_j + dy[direction]
#     tmp = [0,0]
#     if 0 <= x < 4 and 0 <= y < 4:
#         if sea[x][y][0] < 17:
#             tmp[0] = sea[x][y][0]
#             tmp[1] = sea[x][y][1]
#
#             sea[x][y] = [fish_num, direction]
#             sea[f_i][f_j] = tmp
#             return
#     for i in range(1,8):
#         direction = (direction+i) % 8
#         x = f_i + dx[direction]
#         y = f_j + dy[direction]
#         if 0 <= x < 4 and 0 <= y < 4:
#             if sea[x][y][0] < 17:
#                 tmp[0] = sea[x][y][0]
#                 tmp[1] = sea[x][y][1]
#
#                 sea[x][y] = [fish_num, direction]
#                 sea[f_i][f_j] = tmp
#                 return
#
#
# sea = [[] for _ in range(4)]
# fish_input = [list(map(int,input().split())) for _ in range(4)]
# shark = [17, 0]
# fish_nums = []
# res = 0
# trg = 1
# # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# dx = [2,-1,-1,0,1,1,1,0,-1]
# dy = [2,0,-1,-1,-1,0,1,1,1]
#
# for i in range(4):
#     for j in range(0,7,2):
#         a,b = fish_input[i][j:j+2]
#         sea[i].append([a,b])
#
# print(sea)
# for i in range(4):
#     for j in range(4):
#         fish_nums.append([sea[i][j][0],sea[i][j][1],i,j])
# fish_nums.sort(key=lambda x:x[0])
#
#
# while True:
#     if 0< sea[0][0][0] < 17:
#         shark[1] = sea[0][0][1]
#         for i in range(len(fish_nums)):
#             if fish_nums[i][0] == sea[0][0][0]:
#                 fish_nums.pop(i)
#                 break
#         res += sea[0][0][0]
#     # else:
#     #     trg[0] = 0
#     sea[0][0][0] = shark[0]
#     sea[0][0][1] = shark[1]
#
#     # 물고기 이동
#     for fish in fish_nums:
#         moving_fish(fish)
#     # print(sea)
#     # print(fish_nums)
#     # 상어 이동
#     s_i, s_j = 0,0
#     while True:
#         s_x = s_i + dx[shark[1]]
#         s_y = s_j + dy[shark[1]]
#
#         if 0 <= s_x < 4 and 0 <= s_y < 4:
#             s_i = s_x
#             s_j = s_y
#         else:
#             if sea[s_i][s_j][0]:
#                 res += sea[s_i][s_j][0]
#                 for i in range(len(fish_nums)):
#                     if fish_nums[i][0] == sea[s_i][s_j][0]:
#                         fish_nums.pop(i)
#                         break
#                 shark[1] = sea[s_i][s_j][1]
#                 sea[s_i][s_j] = [0,0]
#             else:
#                 trg = 0
#             break
#
#     if trg == 0:
#         break
#     else:
#         trg = 1
#
# print(res)


# v3
# def moving_fish():
#     # 물고기 이동
#     for i in range(1, 17):
#         if not fish_nums[i]:
#             continue
#         x, y = fish_nums[i][0], fish_nums[i][1]
#         print(sea[x][y])
#         direction = sea[x][y][1]
#         tmp = [0,0]
#         for j in range(8):
#             direction = (direction + j) % 8
#             nx = x + dx[direction]
#             ny = y + dy[direction]
#             if 0 <= nx < 4 and 0 <= ny < 4:
#                 if sea[nx][ny][0] != 17:
#                     tmp[0] = sea[nx][ny][0]
#                     tmp[1] = sea[nx][ny][1]
#
#                     sea[nx][ny] = sea[x][y]
#                     sea[x][y] = tmp
#                     return
#
# def shark_dfs(x,y,shark_d,cnt):
#     global res, sea, fish_nums
#     moving_fish()
#     # 상어 이동
#     while True:
#         nx = x + dx[shark_d]
#         ny = y + dy[shark_d]
#         if not (0 <= nx < 4 and 0 <= ny < 4):
#             res = max(res, cnt)
#             return
#         if not sea[nx][ny]:
#             x, y = nx, ny
#             continue
#         sea_tmp = [sea[i][:] for i in range(4)]
#         fish_nums_tmp = [fish_nums[i][:] for i in range(17)]
#
#         position, fish_tmp = fish_nums[sea[nx][ny][0]], sea[nx][ny]
#         fish_nums[sea[nx][ny][0]] = []
#         sea[nx][ny] = []
#         shark_dfs(nx,ny,fish_tmp[1],cnt+fish_tmp[0])
#         sea, fish_nums = sea_tmp, fish_nums_tmp
#         x, y = nx, ny
#
#
# sea = [[] for _ in range(4)]
# fish_input = [list(map(int,input().split())) for _ in range(4)]
# fish_nums = [[] for _ in range(17)]
# res = 0
# trg = 1
# # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# dx = [2,-1,-1,0,1,1,1,0,-1]
# dy = [2,0,-1,-1,-1,0,1,1,1]
#
# # 지도에 번호, 방향
# for i in range(4):
#     for j in range(0,7,2):
#         a,b = fish_input[i][j:j+2]
#         sea[i].append([a,b])
#         fish_nums[a] =[i, j//2]
#
# shark_d = sea[0][0][1]
# res += sea[0][0][0]
# fish_nums[sea[0][0][0]][0] = -1
# sea[0][0][0] = 17
# sea[0][0][1] = shark_d
#
# shark_dfs(0,0,shark_d,res)
# print(res)



# v4
# def moving_fish(s_i, s_j):
#     # 물고기 이동
#     for i in range(1, 17):
#         if fish_nums[i]:
#             x, y = fish_nums[i][0], fish_nums[i][1]
#             # print(sea[x][y])
#             direction = sea[x][y][1]
#
#             for j in range(8):
#                 direction = (direction + j) % 8
#                 nx = x + dx[direction]
#                 ny = y + dy[direction]
#                 if 0 <= nx < 4 and 0 <= ny < 4:
#                     if nx != s_i and ny != s_j:
#                         tmp = sea[nx][ny]
#                         sea[nx][ny] = sea[x][y]
#                         sea[x][y] = tmp
#                         break
#
# def shark_dfs(x,y,shark_d,cnt):
#     global res, sea, fish_nums
#     moving_fish(x,y)
#     # 상어 이동
#     while True:
#         nx = x + dx[shark_d]
#         ny = y + dy[shark_d]
#         if not (0 <= nx < 4 and 0 <= ny < 4):
#             res = max(res, cnt)
#             return
#         if not sea[nx][ny]:
#             x, y = nx, ny
#             continue
#         sea_tmp = [sea[i][:] for i in range(4)]
#         fish_nums_tmp = [fish_nums[i][:] for i in range(17)]
#
#         position, fish_tmp = fish_nums[sea[nx][ny][0]], sea[nx][ny]
#         fish_nums[sea[nx][ny][0]] = []
#         sea[nx][ny] = []
#
#         shark_dfs(nx,ny,fish_tmp[1],cnt+fish_tmp[0])
#         print(position)
#         fish_nums[sea[nx][ny][0]] = position
#         sea[nx][ny] = fish_tmp
#         sea, fish_nums = sea_tmp, fish_nums_tmp
#         x, y = nx, ny
#
#
# sea = [[] for _ in range(4)]
# fish_input = [list(map(int,input().split())) for _ in range(4)]
# fish_nums = [[] for _ in range(17)]
# res = 0
# trg = 1
# # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# dx = [2,-1,-1,0,1,1,1,0,-1]
# dy = [2,0,-1,-1,-1,0,1,1,1]
#
# # 지도에 번호, 방향
# for i in range(4):
#     for j in range(0,7,2):
#         a,b = fish_input[i][j:j+2]
#         sea[i].append([a,b])
#         fish_nums[a] =[i, j//2]
#
# shark_d = sea[0][0][1]
# res += sea[0][0][0]
# fish_nums[sea[0][0][0]] = []
# # sea[0][0] = [17, shark_d]
# sea[0][0] = []
#
# shark_dfs(0,0,shark_d,res)
# print(res)

# v5
# import copy
# def moving_fish(s_i, s_j):
#     # 물고기 이동
#     for i in range(16):
#         if fish_nums[i]:
#             x, y = fish_nums[i][0], fish_nums[i][1]
#             direction = sea[x][y][1]
#
#             for j in range(9):
#                 nx = x + dx[direction]
#                 ny = y + dy[direction]
#                 # if 0 <= nx < 4 and 0 <= ny < 4:
#                 #     if nx != s_i and ny != s_j:
#                 #         # sea[x][y][0], sea[nx][ny][0] = sea[nx][ny][0], sea[x][y][0]
#                 #         # sea[x][y][1], sea[nx][ny][1] = sea[nx][ny][1], direction
#                 #         if sea[nx][ny]:
#                 #             fish_nums[sea[nx][ny][0]] = [x, y]
#                 #         fish_nums[sea[x][y][0]] = [nx, ny]
#                 #         tmp = sea[nx][ny]
#                 #         sea[nx][ny] = sea[x][y]
#                 #         sea[x][y] = tmp
#                 #         break
#                 # direction = (direction + 1) % 8
#                 if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == s_i and ny == s_j):
#                     direction = (direction + 1) % 8
#                     continue
#                 if sea[nx][ny]:
#                     fish_nums[sea[nx][ny][0]] = [x, y]
#                 sea[nx][ny], sea[x][y] = sea[x][y], sea[nx][ny]
#                 fish_nums[i] = [nx, ny]
#                 break
#
# def shark_dfs(x,y,shark_d,cnt):
#     global res, sea, fish_nums
#     moving_fish(x,y)
#     # 상어 이동
#     while True:
#         nx = x + dx[shark_d]
#         ny = y + dy[shark_d]
#         if not 0 <= nx < 4 or not 0 <= ny < 4:
#             res = max(res, cnt)
#             return
#         if not sea[nx][ny]:
#             x, y = nx, ny
#             continue
#         sea_tmp = copy.deepcopy(sea)
#         fish_nums_tmp = copy.deepcopy(fish_nums)
#
#         position, fish_tmp = fish_nums[sea[nx][ny][0]], sea[nx][ny]
#         fish_nums[sea[nx][ny][0]] = []
#         sea[nx][ny] = []
#
#         shark_dfs(nx,ny,fish_tmp[1],cnt+fish_tmp[0]+1)
#
#         sea, fish_nums = sea_tmp, fish_nums_tmp
#         fish_nums[sea[nx][ny][0]] = position
#         sea[nx][ny] = fish_tmp
#         x, y = nx, ny
#
#
# sea = [[] for _ in range(4)]
# fish_input = [list(map(int,input().split())) for _ in range(4)]
# fish_nums = [[] for _ in range(16)]
# res = 0
# trg = 1
# # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# # dx = [2,-1,-1,0,1,1,1,0,-1]
# # dy = [2,0,-1,-1,-1,0,1,1,1]
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,-1,-1,-1,0,1,1,1]
#
# # 지도에 번호, 방향
# for i in range(4):
#     for j in range(0,7,2):
#         a,b = fish_input[i][j:j+2]
#         sea[i].append([a-1,b-1])
#         fish_nums[a-1] =[i, j//2]
# print(sea)
# print(fish_nums)
# res = 0
# shark_d = sea[0][0][1]
# cnt = sea[0][0][0] + 1
# fish_nums[sea[0][0][0]] = []
# # sea[0][0] = [17, shark_d]
# sea[0][0] = []
#
# shark_dfs(0,0,shark_d,cnt)
# print(res)


# v6
import copy
def moving_fish(s_i, s_j):
    # 물고기 이동
    for i in range(16):
        if fish_nums[i]:
            x, y = fish_nums[i][0], fish_nums[i][1]
            # direction = sea[x][y][1]

            for j in range(9):
                nx = x + dx[sea[x][y][1]]
                ny = y + dy[sea[x][y][1]]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == s_i and ny == s_j):
                    sea[x][y][1] = (sea[x][y][1] + 1) % 8
                    continue
                if sea[nx][ny]:
                    fish_nums[sea[nx][ny][0]] = [x, y]
                sea[nx][ny], sea[x][y] = sea[x][y], sea[nx][ny]
                fish_nums[i] = [nx, ny]
                break

def shark_dfs(x,y,shark_d,cnt):
    global res, sea, fish_nums
    moving_fish(x,y)
    # 상어 이동
    while True:
        nx = x + dx[shark_d]
        ny = y + dy[shark_d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            res = max(res, cnt)
            return
        if not sea[nx][ny]:
            x, y = nx, ny
            continue
        sea_tmp = copy.deepcopy(sea)
        fish_nums_tmp = copy.deepcopy(fish_nums)

        position, fish_tmp = fish_nums[sea[nx][ny][0]], sea[nx][ny]
        fish_nums[sea[nx][ny][0]] = []
        sea[nx][ny] = []

        shark_dfs(nx,ny, fish_tmp[1], cnt+fish_tmp[0]+1)

        sea, fish_nums = sea_tmp, fish_nums_tmp
        fish_nums[sea[nx][ny][0]] = position
        sea[nx][ny] = fish_tmp
        x, y = nx, ny


sea = [[] for _ in range(4)]
fish_input = [list(map(int,input().split())) for _ in range(4)]
fish_nums = [[] for _ in range(16)]
res = 0
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]


for i in range(4):
    for j in range(0,7,2):
        a,b = fish_input[i][j:j+2]
        sea[i].append([a-1,b-1])
        fish_nums[a-1] =[i, j//2]

res = 0
shark_d = sea[0][0][1]
cnt = sea[0][0][0] + 1
fish_nums[sea[0][0][0]] = []
sea[0][0] = []

shark_dfs(0,0,shark_d,cnt)
print(res)
