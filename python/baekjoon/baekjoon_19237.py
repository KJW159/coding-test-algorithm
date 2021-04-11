# # baekjoon_19237 어른 상어
# # v1
#
# def checking_dir(shark):
#     global total_shark
#
#     shark_curr = curr_dir[shark]
#     s_i, s_j = sharks[shark]
#
#     move_trg = False
#     for c in range(4):
#         curr_tmp = pri_dir[shark][shark_curr][c]
#         s_x = s_i + dx[curr_tmp]
#         s_y = s_j + dy[curr_tmp]
#         if 0 <= s_x < N and 0 <= s_y < N:
#             if sea[s_x][s_y] == 0:
#                 sea[s_x][s_y] = shark
#                 gas_time[s_x][s_y] = K
#                 curr_dir[shark] = curr_tmp
#                 sharks[shark] = [s_x, s_y]
#                 move_trg = True
#                 break
#             if sea[s_x][s_y] != 0 and sharks[sea[s_x][s_y]] == [s_x,s_y]:
#                 if sea[s_x][s_y] > shark:
#                     continue
#                 total_shark -= 1
#                 sharks[sea[s_i][s_j]] = [-1, -1]
#                 move_trg = True
#                 break
#     if not move_trg:
#         for c in range(1,5):
#             s_x = s_i + dx[c]
#             s_y = s_j + dx[c]
#             if 0 <= s_x < N and 0 <= s_y < N and sea[s_x][s_y] == shark:
#                 gas_time[s_x][s_y] = K
#                 curr_dir[shark] = c
#                 sharks[shark] = [s_x, s_y]
#
#
# # 입력
# N, M, K = map(int, input().split())
# sea = []
# # 상어 현재 위치
# sharks = [[] for _ in range(M+1)]
# for i in range(N):
#     sea_tmp = list(map(int, input().split()))
#     for j in range(N):
#         if sea_tmp[j] != 0:
#             sharks[sea_tmp[j]] = [i,j]
#     sea.append(sea_tmp)
#
# # 상어 냄새 시간
# gas_time =[[0]*N for _ in range(N)]
# for i in range(1, M+1):
#     gas_time[sharks[i][0]][sharks[i][1]] = K
# # 현재 보고 있는 방향
# curr_dir =[0]
# curr_dir.extend(list(map(int, input().split())))
#
# # 우선 순위 테이블
# pri_dir = [[] for _ in range(M+1)]
# for i in range(1,M+1):
#     pri_dir[i].append([])
#     for j in range(4):
#         dir_tmp = list(map(int, input().split()))
#         pri_dir[i].append(dir_tmp)
#
# total_shark = M
# res = 0
# dx = [0,-1,1,0,0]
# dy = [0,0,0,-1,1]
#
# while True:
#     if total_shark == 1 or res > 1000:
#         break
#     for i in range(1, M+1):
#         if sharks[i] != [-1,-1]:
#             checking_dir(i)
#     for nx in range(N):
#         for ny in range(N):
#             if sea[nx][ny] != 0 and sharks[sea[nx][ny]] != [nx, ny]:
#                 gas_time[nx][ny] -= 1
#                 if gas_time[nx][ny] == 0:
#                     sea[nx][ny] = 0
#     res += 1
# if res <= 1000:
#     print(res)
# else:
#     print(-1)


# v2
# def checking_dir(shark):
#     global total_shark
#
#     shark_curr = curr_dir[shark]
#     s_i, s_j = sharks[shark]
#
#     move_trg = False
#     for c in range(4):
#         curr_tmp = pri_dir[shark][shark_curr][c]
#         s_x = s_i + dx[curr_tmp]
#         s_y = s_j + dy[curr_tmp]
#         if 0 <= s_x < N and 0 <= s_y < N:
#             if sea[s_x][s_y] == 0:
#                 sea[s_x][s_y] = shark
#                 gas_time[s_x][s_y] = K
#                 curr_dir[shark] = curr_tmp
#                 sharks[shark] = [s_x, s_y]
#                 move_trg = True
#                 break
#             if sea[s_x][s_y] != 0 and sharks[sea[s_x][s_y]] == [s_x,s_y]:
#                 if sea[s_x][s_y] > shark:
#                     continue
#                 total_shark -= 1
#                 sharks[sea[s_i][s_j]] = [-1, -1]
#                 move_trg = True
#                 break
#     if not move_trg:
#         for c in range(4):
#             curr_tmp = pri_dir[shark][shark_curr][c]
#             s_x = s_i + dx[curr_tmp]
#             s_y = s_j + dy[curr_tmp]
#             if 0 <= s_x < N and 0 <= s_y < N and sea[s_x][s_y] == shark:
#                 gas_time[s_x][s_y] = K
#                 curr_dir[shark] = curr_tmp
#                 sharks[shark] = [s_x, s_y]
#                 break
#
#
# # 입력
# N, M, K = map(int, input().split())
# sea = []
# # 상어 현재 위치
# sharks = [[] for _ in range(M+1)]
# for i in range(N):
#     sea_tmp = list(map(int, input().split()))
#     for j in range(N):
#         if sea_tmp[j] != 0:
#             sharks[sea_tmp[j]] = [i,j]
#     sea.append(sea_tmp)
#
# # 상어 냄새 시간
# gas_time =[[0]*N for _ in range(N)]
# for i in range(1, M+1):
#     gas_time[sharks[i][0]][sharks[i][1]] = K
# # 현재 보고 있는 방향
# curr_dir =[0]
# curr_dir.extend(list(map(int, input().split())))
#
# # 우선 순위 테이블
# pri_dir = [[] for _ in range(M+1)]
# for i in range(1,M+1):
#     pri_dir[i].append([])
#     for j in range(4):
#         dir_tmp = list(map(int, input().split()))
#         pri_dir[i].append(dir_tmp)
#
# total_shark = M
# res = 0
# dx = [0,-1,1,0,0]
# dy = [0,0,0,-1,1]
#
# while True:
#     if total_shark == 1 or res > 1000:
#         break
#     for i in range(1, M+1):
#         if sharks[i] != [-1,-1]:
#             checking_dir(i)
#     for nx in range(N):
#         for ny in range(N):
#             if sea[nx][ny] != 0 and sharks[sea[nx][ny]] != [nx, ny]:
#                 gas_time[nx][ny] -= 1
#                 if gas_time[nx][ny] == 0:
#                     sea[nx][ny] = 0
#     res += 1
# if res <= 1000:
#     print(res)
# else:
#     print(-1)


# v3
# def checking_dir(shark):
#     global total_shark
#
#     shark_curr = curr_dir[shark]
#     s_i, s_j = sharks[shark]
#
#     for c in range(4):
#         curr_tmp = pri_dir[shark][shark_curr][c]
#         s_x = s_i + dx[curr_tmp]
#         s_y = s_j + dy[curr_tmp]
#         if 0 <= s_x < N and 0 <= s_y < N:
#             if sea[s_x][s_y] == 0 and gas_time[s_x][s_y] == K:
#                 for s in range(1,shark):
#                     if sharks[s] == [s_x, s_y]:
#                         total_shark -= 1
#                         sharks[shark] = [-1, -1]
#                         return
#             if sea[s_x][s_y] == 0 and gas_time[s_x][s_y] == 0:
#                 # sea[s_x][s_y] = shark
#                 gas_time[s_x][s_y] = K
#                 curr_dir[shark] = curr_tmp
#                 sharks[shark] = [s_x, s_y]
#                 return
#
#     for c in range(4):
#         curr_tmp = pri_dir[shark][shark_curr][c]
#         s_x = s_i + dx[curr_tmp]
#         s_y = s_j + dy[curr_tmp]
#         if 0 <= s_x < N and 0 <= s_y < N and sea[s_x][s_y] == shark:
#             gas_time[s_x][s_y] = K
#             curr_dir[shark] = curr_tmp
#             sharks[shark] = [s_x, s_y]
#             return
#     return
#
#
# # 입력
# N, M, K = map(int, input().split())
# sea = []
# # 상어 현재 위치
# sharks = [[] for _ in range(M+1)]
# for i in range(N):
#     sea_tmp = list(map(int, input().split()))
#     for j in range(N):
#         if sea_tmp[j] != 0:
#             sharks[sea_tmp[j]] = [i,j]
#     sea.append(sea_tmp)
#
# # 상어 냄새 시간
# gas_time =[[0]*N for _ in range(N)]
# for i in range(1, M+1):
#     gas_time[sharks[i][0]][sharks[i][1]] = K
# # 현재 보고 있는 방향
# curr_dir =[0]
# curr_dir.extend(list(map(int, input().split())))
#
# # 우선 순위 테이블
# pri_dir = [[] for _ in range(M+1)]
# for i in range(1,M+1):
#     pri_dir[i].append([])
#     for j in range(4):
#         dir_tmp = list(map(int, input().split()))
#         pri_dir[i].append(dir_tmp)
#
# total_shark = M
# res = 0
# dx = [0,-1,1,0,0]
# dy = [0,0,0,-1,1]
#
# while True:
#     if total_shark == 1 or res > 1000:
#         break
#     for i in range(1, M+1):
#         if sharks[i] != [-1,-1]:
#             checking_dir(i)
#     for j in range(1, M+1):
#         if sharks[j] != [-1,-1]:
#             sea[sharks[j][0]][sharks[j][1]] = j
#     for nx in range(N):
#         for ny in range(N):
#             if sea[nx][ny] != 0 and sharks[sea[nx][ny]] != [nx, ny]:
#                 gas_time[nx][ny] -= 1
#                 if gas_time[nx][ny] == 0:
#                     sea[nx][ny] = 0
#     res += 1
# if res <= 1000:
#     print(res)
# else:
#     print(-1)


# v4
def checking_dir(shark):
    global total_shark

    shark_curr = curr_dir[shark]
    s_i, s_j = sharks[shark]

    for c in range(4):
        curr_tmp = pri_dir[shark][shark_curr][c]
        s_x = s_i + dx[curr_tmp]
        s_y = s_j + dy[curr_tmp]
        if 0 <= s_x < N and 0 <= s_y < N and sea[s_x][s_y] == 0:
            # 잡아 먹힘
            if gas_time[s_x][s_y] == K:
                for s in range(1,shark):
                    if sharks[s] == [s_x, s_y]:
                        total_shark -= 1
                        sharks[shark] = [-1, -1]
                        return
            # 빈 공간 이동
            if gas_time[s_x][s_y] == 0:
                gas_time[s_x][s_y] = K
                curr_dir[shark] = curr_tmp
                sharks[shark] = [s_x, s_y]
                return
# 이동할 수 있는 곳이 없을때
    for c in range(4):
        curr_tmp = pri_dir[shark][shark_curr][c]
        s_x = s_i + dx[curr_tmp]
        s_y = s_j + dy[curr_tmp]
        if 0 <= s_x < N and 0 <= s_y < N and sea[s_x][s_y] == shark:
            gas_time[s_x][s_y] = K
            curr_dir[shark] = curr_tmp
            sharks[shark] = [s_x, s_y]
            return


# 입력
N, M, K = map(int, input().split())
sea = []
# 상어 현재 위치
sharks = [[] for _ in range(M+1)]
for i in range(N):
    sea_tmp = list(map(int, input().split()))
    for j in range(N):
        if sea_tmp[j] != 0:
            sharks[sea_tmp[j]] = [i,j]
    sea.append(sea_tmp)

# 상어 냄새 시간
gas_time =[[0]*N for _ in range(N)]
for i in range(1, M+1):
    gas_time[sharks[i][0]][sharks[i][1]] = K
# 현재 보고 있는 방향
curr_dir =[0]
curr_dir.extend(list(map(int, input().split())))

# 우선 순위 테이블
pri_dir = [[] for _ in range(M+1)]
for i in range(1,M+1):
    pri_dir[i].append([])
    for j in range(4):
        dir_tmp = list(map(int, input().split()))
        pri_dir[i].append(dir_tmp)

total_shark = M
res = 0
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

while True:
    if total_shark == 1 or res > 1000:
        break
    for i in range(1, M+1):
        if sharks[i] != [-1,-1]:
            checking_dir(i)

    # 상어 최종 위치에 상어 번호 표시하기
    for j in range(1, M+1):
        if sharks[j] != [-1,-1]:
            sea[sharks[j][0]][sharks[j][1]] = j
    for nx in range(N):
        for ny in range(N):
            if sea[nx][ny] != 0 and sharks[sea[nx][ny]] != [nx, ny]:
                gas_time[nx][ny] -= 1
                if gas_time[nx][ny] == 0:
                    sea[nx][ny] = 0
    res += 1
if res <= 1000:
    print(res)
else:
    print(-1)