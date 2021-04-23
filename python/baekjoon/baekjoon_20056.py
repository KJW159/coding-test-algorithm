# baekjoon_20056 마법사 상어와 파이어볼

# v1
# def moving_fire():
#     for position, infos in fire_balls.items():
#         for info in infos:
#             for j in range(info[1]):
#                 x = position[0]+dx[info[2]]
#                 y = position[1]+dy[info[2]]
#                 if 0 <= x < N and 0 <= y < N:
#                     continue
#                 else:
#                     break
#                     # arr[x][y] += 1
#                     # arr[position[0]][position[0]] -= 1
#             fire_balls[(x, y)].append(info)
#             fire_balls[position].remove(info)
#
# def mixing_fire():
#     for position in fire_balls:
#         if len(fire_balls[position]) >= 2:
#             mass = 0
#             speed = 0
#             direction_past = fire_balls[position][0][2] % 2
#             trg = True
#             k = 0
#             fire_cnt = 0
#             for infos in fire_balls[position]:
#                 for info in infos:
#                     mass += info[0]
#                     speed += info[1]
#                     fire_cnt += 1
#                     direction = info[2] % 2
#                     if not trg:
#                         continue
#                     else:
#                         if direction != direction_past:
#                             trg = False
#                             k = 1
#             mass //= 5
#             speed //= fire_cnt
#             if mass == 0:
#                 fire_balls[position] = []
#                 continue
#             else:
#                 for j in range(k,8,2):
#                     x = position[0] + dx[j]
#                     y = position[1] + dy[j]
#                     fire_balls[(x,y)].append([mass,speed,j])
#             fire_balls[position] = []
#
# from collections import defaultdict
#
# N, M, K = map(int, input().split())
# fire_balls = defaultdict(list)
# arr = [[0]*(N+1) for _ in range(N+1)]
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     arr[r][c] = 1
#     fire_balls[(r,c)].append([m,s,d])
#
#
# for i in range(K):
#     moving_fire()
#     mixing_fire()
#
# res = 0
# for infos in fire_balls.values():
#     for info in infos:
#         res += info[0]
# print(res)


# v2
# def moving_fire():
#     fire_tmp = []
#     for position, infos in fire_balls.items():
#         for info in infos:
#             p_i, p_j = position
#             trg = True
#             for j in range(info[1]):
#                 x = p_i+dx[info[2]]
#                 y = p_j+dy[info[2]]
#                 if 1 <= x < N+1 and 1 <= y < N+1:
#                     p_i = x
#                     p_j = y
#                 else:
#                     arr[p_i][p_j] += 1
#                     fire_tmp.append([p_i, p_j, info[0], info[1], info[2]])
#                     trg = False
#                     break
#             if trg:
#                 arr[x][y] += 1
#                 fire_tmp.append([x, y, info[0], info[1], info[2]])
#             arr[position[0]][position[0]] -= 1
#             fire_balls[position].remove(info)
#     for fire in fire_tmp:
#         fire_balls[(x,y)].append([fire[2], fire[3], fire[4]])
#
# def mixing_fire(f_i,f_j):
#             mass = 0
#             speed = 0
#             direction_past = fire_balls[(f_i,f_j)][0][2] % 2
#             trg = True
#             k = 0
#             fire_cnt = 0
#             for info in fire_balls[(f_i,f_j)]:
#                 mass += info[0]
#                 speed += info[1]
#                 fire_cnt += 1
#                 direction = info[2] % 2
#                 if not trg:
#                     continue
#                 else:
#                     if direction != direction_past:
#                         trg = False
#                         k = 1
#             mass //= 5
#             speed //= fire_cnt
#             if mass == 0:
#                 fire_balls[(f_i,f_j)] = []
#             else:
#                 for j in range(k,8,2):
#                     x = f_i+ dx[j]
#                     y = f_j + dy[j]
#                     fire_balls[(x,y)].append([mass,speed,j])
#                     arr[x][y] += 1
#             fire_balls[(f_i,f_j)] = []
#             arr[f_i][f_j] = 0
#
# from collections import defaultdict
#
# N, M, K = map(int, input().split())
# fire_balls = defaultdict(list)
# arr = [[0]*(N+1) for _ in range(N+1)]
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     arr[r][c] = 1
#     fire_balls[(r,c)].append([m,s,d])
#
#
# for _ in range(K):
#     moving_fire()
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] >= 2:
#                 print(i,j,arr[i][j], len(fire_balls[(i,j)]))
#                 mixing_fire(i,j)
#
# res = 0
# for infos in fire_balls.values():
#     for info in infos:
#         res += info[0]
# print(res)

# v3
# def moving_fire(s_i, s_j):
#         fire_balls_tmp = copy.deepcopy(fire_balls[s_i][s_j])
#         for info in fire_balls_tmp:
#             p_i, p_j = s_i, s_j
#             for _ in range(info[1]):
#                 x = p_i+dx[info[2]]
#                 y = p_j+dy[info[2]]
#                 if 1 <= x < N+1 and 1 <= y < N+1:
#                     p_i = x
#                     p_j = y
#                 else:
#                     break
#             arr[s_i][s_j] -= 1
#             fire_balls[s_i][s_j].popleft()
#             arr[p_i][p_j] += 1
#             fire_balls[p_i][p_j].append(info)
#
# def mixing_fire(f_i,f_j):
#             mass = 0
#             speed = 0
#             direction_past = fire_balls[f_i][f_j][0][2] % 2
#             k = 0
#             fire_cnt = arr[f_i][f_j]
#             for info in fire_balls[f_i][f_j]:
#                 mass += info[0]
#                 speed += info[1]
#                 direction = info[2] % 2
#                 if direction != direction_past:
#                     k = 1
#             mass //= 5
#             speed //= fire_cnt
#             if mass != 0:
#                 for j in range(k,8,2):
#                     x = f_i+ dx[j]
#                     y = f_j + dy[j]
#                     fire_balls[x][y].append([mass, speed ,j])
#                     arr[x][y] += 1
#             fire_balls[f_i][f_j] = deque
#             arr[f_i][f_j] = 0
#
# from collections import deque
# import copy
# N, M, K = map(int, input().split())
# deque = deque()
# fire_balls = [[deque for _ in range(N+1)] for __ in range(N+1)]
# arr = [[0]*(N+1) for _ in range(N+1)]
#
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     arr[r][c] = 1
#     fire_balls[r][c].append([m,s,d])
#
#
# for _ in range(K):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] >= 1:
#                 moving_fire(i,j)
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] >= 2:
#                 mixing_fire(i,j)
#
# res = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] > 0:
#             for info in fire_balls[i][j]:
#                 res += info[0]
# print(res)


# v4
# from collections import deque
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
#
# N, M, K = map(int, input().split())
# q = deque()
# arr = [[deque() for _ in range(N+1)] for _ in range(N+1)]
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     arr[r][c].append([m, s, d])
#     q.append([r, c])
#
# for _ in range(K):
#     temp = []
#     qlen = len(q)
#     for _ in range(qlen):
#         x, y = q.popleft()
#         for _ in range(len(arr[x][y])):
#             m, s, d = arr[x][y].popleft()
#             nx = (s * dx[d] + x) % N
#             ny = (s * dy[d] + y) % N
#             q.append([nx, ny])
#             temp.append([nx, ny, m, s, d])
#
#     for x, y, m, s, d in temp:
#         arr[x][y].append([m, s, d])
#
#     for i in range(N):
#         for j in range(N):
#             if len(arr[i][j]) > 1:
#                 nm, ns, odd, even, flag = 0, 0, 0, 0, 0
#                 for idx, [m, s, d] in enumerate(arr[i][j]):
#                     nm += m
#                     ns += s
#                     if idx == 0:
#                         if d % 2 == 0:
#                             even = 1
#                         else:
#                             odd = 1
#                     else:
#                         if even == 1 and d % 2 == 1:
#                             flag = 1
#                         elif odd == 1 and d % 2 == 0:
#                             flag = 1
#
#                 nm //= 5
#                 ns //= len(arr[i][j])
#                 arr[i][j] = deque()
#                 if nm != 0:
#                     for idx in range(4):
#                         nd = 2 * idx if flag == 0 else 2 * idx + 1
#                         arr[i][j].append([nm, ns, nd])
#     print(arr)
# res = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]:
#             for info in arr[i][j]:
#                 res += info[0]
# print(res)



# re-v1
# from collections import defaultdict
# import copy, math
#
# N, M, K = map(int, input().split())
# # arr = [[0]*N for _ in range(N)]
# fire_balls = defaultdict(list)
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     fire_balls[r-1,c-1].append([m,s,d])
#     # arr[r-1][c-1] += 1
#
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
#
#
# for k in range(K):
#     # 이동하기, m,s,d
#     fire_balls_tmp = defaultdict(list)
#     for key in fire_balls:
#         for fire_ball in fire_balls[key]:
#             x = key[0]
#             y = key[1]
#             for i in range(fire_ball[1]):
#                 x += dx[fire_ball[2]]
#                 y += dy[fire_ball[2]]
#             x %= N
#             y %= N
#             fire_balls_tmp[x,y].append(fire_ball)
#
#     fire_balls = copy.deepcopy(fire_balls_tmp)
#     fire_balls_tmp = defaultdict(list)
#
#     # 2번 내용, m,s,d
#     for key in fire_balls:
#         ball_nums = len(fire_balls[key])
#         if ball_nums >= 2:
#             mass = 0
#             speed = 0
#             direction = 0
#             trg1 = fire_balls[key][0][2] % 2
#             trg2 = True
#             for fire_ball in fire_balls[key]:
#                 mass += fire_ball[0]
#                 speed += fire_ball[1]
#                 if trg2:
#                     if fire_ball[2] % 2 != trg1:
#                         trg2 = False
#             mass = math.floor(mass/5)
#             if mass != 0:
#                 speed = math.floor(speed/ball_nums)
#                 x = key[0]
#                 y = key[1]
#                 if trg2:
#                     start = 0
#                 else:
#                     start = 1
#                 for i in range(start, 8, 2):
#                     nx = (x + dx[i]) % N
#                     ny = (y + dy[i]) % N
#                     fire_balls_tmp[nx,ny].append([mass, speed, i])
#             else:
#                 fire_balls[key] = []
#     fire_balls = copy.deepcopy(fire_balls_tmp)
#
# res = 0
# for key in fire_balls:
#     for fire_ball in fire_balls[key]:
#          res += fire_ball[0]
#
# print(res)

# re-v2

# from collections import defaultdict
# import copy, math
#
# N, M, K = map(int, input().split())
# # arr = [[0]*N for _ in range(N)]
# fire_balls = defaultdict(list)
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     fire_balls[r-1,c-1].append([m,s,d])
#     # arr[r-1][c-1] += 1
#
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
#
#
# for k in range(K):
#     # 이동하기, m,s,d
#     fire_balls_tmp = defaultdict(list)
#     for key in fire_balls:
#         for fire_ball in fire_balls[key]:
#             x = key[0]
#             y = key[1]
#             for i in range(fire_ball[1]):
#                 x += dx[fire_ball[2]]
#                 y += dy[fire_ball[2]]
#             x %= N
#             y %= N
#             fire_balls_tmp[x,y].append(fire_ball)
#
#     fire_balls = copy.deepcopy(fire_balls_tmp)
#     fire_balls_tmp = defaultdict(list)
#
#     # 2번 내용, m,s,d
#     for key in fire_balls:
#         ball_nums = len(fire_balls[key])
#         if ball_nums >= 2:
#             mass = 0
#             speed = 0
#             direction = 0
#             trg1 = fire_balls[key][0][2] % 2
#             trg2 = True
#             for fire_ball in fire_balls[key]:
#                 mass += fire_ball[0]
#                 speed += fire_ball[1]
#                 if trg2:
#                     if fire_ball[2] % 2 != trg1:
#                         trg2 = False
#             mass = math.floor(mass/5)
#             if mass != 0:
#                 speed = math.floor(speed/ball_nums)
#                 x = key[0]
#                 y = key[1]
#                 if trg2:
#                     start = 0
#                 else:
#                     start = 1
#                 tmp = []
#                 for i in range(start, 8, 2):
#                     tmp.append([mass, speed, i])
#                 fire_balls_tmp[x,y] = tmp
#             else:
#                 fire_balls[key] = []
#     fire_balls = copy.deepcopy(fire_balls_tmp)
#
# res = 0
# print(fire_balls)
# for key in fire_balls:
#     for fire_ball in fire_balls[key]:
#          res += fire_ball[0]
#
# print(res)

# re-v3
# from collections import defaultdict
# import copy, math
#
# N, M, K = map(int, input().split())
# # arr = [[0]*N for _ in range(N)]
# fire_balls = defaultdict(list)
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     fire_balls[r-1,c-1].append([m,s,d])
#     # arr[r-1][c-1] += 1
#
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
#
#
# for k in range(K):
#     # 이동하기, m,s,d
#     fire_balls_tmp = defaultdict(list)
#     for key in fire_balls:
#         for fire_ball in fire_balls[key]:
#             x = key[0]
#             y = key[1]
#             for i in range(fire_ball[1]):
#                 x += dx[fire_ball[2]]
#                 y += dy[fire_ball[2]]
#             x %= N
#             y %= N
#             fire_balls_tmp[x,y].append(fire_ball)
#
#     fire_balls = copy.deepcopy(fire_balls_tmp)
#
#     # 2번 내용, m,s,d
#     for key in fire_balls:
#         ball_nums = len(fire_balls[key])
#         if ball_nums >= 2:
#             mass = 0
#             speed = 0
#             direction = 0
#             trg1 = fire_balls[key][0][2] % 2
#             trg2 = True
#             for fire_ball in fire_balls[key]:
#                 mass += fire_ball[0]
#                 speed += fire_ball[1]
#                 if trg2:
#                     if fire_ball[2] % 2 != trg1:
#                         trg2 = False
#             mass = math.floor(mass/5)
#             if mass != 0:
#                 speed = math.floor(speed/ball_nums)
#                 if trg2:
#                     start = 0
#                 else:
#                     start = 1
#                 tmp = []
#                 for i in range(start, 8, 2):
#                     tmp.append([mass, speed, i])
#                 fire_balls[key[0],key[1]] = tmp
#             else:
#                 fire_balls[key[0],key[1]] = []
#
# res = 0
# for key in fire_balls:
#     for fire_ball in fire_balls[key]:
#          res += fire_ball[0]
#
# print(res)


# re-v4
# from collections import defaultdict
# import math
#
# N, M, K = map(int, input().split())
# fire_balls = defaultdict(list)
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     fire_balls[r-1,c-1].append([m,s,d])
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
#
# for k in range(K):
#     fire_balls_tmp = defaultdict(list)
#     for key in fire_balls:
#         for fire_ball in fire_balls[key]:
#             x = key[0]
#             y = key[1]
#             for i in range(fire_ball[1]):
#                 x += dx[fire_ball[2]]
#                 y += dy[fire_ball[2]]
#             x %= N
#             y %= N
#             fire_balls_tmp[x,y].append(fire_ball)
#
#     fire_balls = defaultdict(list)
#
#     for key in fire_balls_tmp:
#         ball_nums = len(fire_balls_tmp[key])
#         if ball_nums >= 2:
#             mass = 0
#             speed = 0
#             direction = 0
#             trg1 = fire_balls_tmp[key][0][2] % 2
#             trg2 = True
#             for fire_ball in fire_balls_tmp[key]:
#                 mass += fire_ball[0]
#                 speed += fire_ball[1]
#                 if trg2:
#                     if fire_ball[2] % 2 != trg1:
#                         trg2 = False
#             mass = math.floor(mass/5)
#             if mass != 0:
#                 speed = math.floor(speed/ball_nums)
#                 if trg2:
#                     start = 0
#                 else:
#                     start = 1
#                 tmp = []
#                 for i in range(start, 8, 2):
#                     tmp.append([mass, speed, i])
#                 fire_balls[key[0],key[1]] = tmp
#         else:
#             fire_balls[key[0],key[1]] = fire_balls_tmp[key]
#
# res = 0
# for key in fire_balls:
#     for fire_ball in fire_balls[key]:
#          res += fire_ball[0]
#
# print(res)

# re-v5

# from collections import defaultdict
# import math

# N, M, K = map(int, input().split())
# fire_balls = defaultdict(list)
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     fire_balls[r-1,c-1].append([m,s,d])
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
#
# for k in range(K):
#     fire_balls_tmp = defaultdict(list)
#     for key in fire_balls:
#         for fire_ball in fire_balls[key]:
#             x = key[0]
#             y = key[1]
#             x = (x + dx[fire_ball[2]] * fire_ball[1]) % N
#             y = (y + dy[fire_ball[2]] * fire_ball[1]) % N
#             fire_balls_tmp[x,y].append(fire_ball)
#
#     fire_balls = defaultdict(list)
#
#     for key in fire_balls_tmp:
#         ball_nums = len(fire_balls_tmp[key])
#         if ball_nums >= 2:
#             mass = 0
#             speed = 0
#             direction = 0
#             trg1 = fire_balls_tmp[key][0][2] % 2
#             trg2 = True
#             for fire_ball in fire_balls_tmp[key]:
#                 mass += fire_ball[0]
#                 speed += fire_ball[1]
#                 if trg2:
#                     if fire_ball[2] % 2 != trg1:
#                         trg2 = False
#             mass = math.floor(mass/5)
#             if mass != 0:
#                 speed = math.floor(speed/ball_nums)
#                 if trg2:
#                     start = 0
#                 else:
#                     start = 1
#                 for i in range(start, 8, 2):
#                     fire_balls[key[0],key[1]].append([mass, speed, i])
#         else:
#             fire_balls[key[0],key[1]] = fire_balls_tmp[key]
#
# res = 0
# for key in fire_balls:
#     for fire_ball in fire_balls[key]:
#          res += fire_ball[0]
#
# print(res)

# re-v6
# import sys
# from collections import defaultdict
# input = sys.stdin.readline
#
# N,M,K = map(int, input().split())
# balls = defaultdict(list)
# for _ in range(M):
#     r,c,m,s,d = map(int, input().split())
#     balls[(r-1,c-1)].append([m,s,d])
#
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
#
# for _ in range(K):
#     ball_tmp1 = []
#     for key in balls:
#         i, j = key
#         for ball in balls[key]:
#             m, s, d = ball
#             x = (i + dx[d]*s) % N
#             y = (j + dy[d]*s) % N
#             ball_tmp1.append([x,y,m,s,d])
#             # balls[(x,y)].append([m,s,d])
#     balls = defaultdict(list)
#     for tmp in ball_tmp1:
#         balls[(tmp[0],tmp[1])].append([tmp[2],tmp[3],tmp[4]])
#
#     ball_tmp2 = []
#     for key in balls:
#         ball_nums = len(balls[key])
#         if ball_nums >= 2:
#             mass = 0
#             speed = 0
#             direction = balls[key][0][2] % 2
#             trg = True
#             for ball in balls[key]:
#                 mass += ball[0]
#                 speed += ball[1]
#                 if direction != (ball[2]%2):
#                     trg = False
#             mass = int(mass/5)
#             speed = int(speed/ball_nums)
#             if mass != 0:
#                 if trg:
#                     start = 0
#                 else:
#                     start = 1
#                 i , j = key
#                 for c in range(start,8,2):
#                     x = (i + dx[c]) % N
#                     y = (j + dy[c]) % N
#                     # balls[x,y].append([mass, speed, c])
#                     ball_tmp2.append([x,y,mass,speed,c])
#                 balls[key] = []
#             else:
#                 balls[key] = []
#     if ball_tmp2:
#         for tmp in ball_tmp2:
#             balls[(tmp[0], tmp[1])].append([tmp[2], tmp[3], tmp[4]])
#     print(balls)
# res = 0
# for key in balls:
#     for ball in balls[key]:
#         res += ball[0]
# print(res)

# re-v3

import sys
from collections import defaultdict
input = sys.stdin.readline

N,M,K = map(int, input().split())
balls = defaultdict(list)
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    balls[(r-1,c-1)].append([m,s,d])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    ball_tmp1 = []
    for key in balls:
        i, j = key
        for ball in balls[key]:
            m, s, d = ball
            x = (i + dx[d]*s) % N
            y = (j + dy[d]*s) % N
            ball_tmp1.append([x,y,m,s,d])
            # balls[(x,y)].append([m,s,d])
    balls = defaultdict(list)
    for tmp in ball_tmp1:
        balls[(tmp[0],tmp[1])].append([tmp[2],tmp[3],tmp[4]])

    ball_tmp2 = []
    for key in balls:
        ball_nums = len(balls[key])
        if ball_nums >= 2:
            mass = 0
            speed = 0
            direction = balls[key][0][2] % 2
            trg = True
            for ball in balls[key]:
                mass += ball[0]
                speed += ball[1]
                if direction != (ball[2]%2):
                    trg = False
            mass = int(mass/5)
            speed = int(speed/ball_nums)
            if mass != 0:
                if trg:
                    start = 0
                else:
                    start = 1
                i , j = key
                for c in range(start,8,2):
                    ball_tmp2.append([i,j,mass,speed,c])
                balls[key] = []
            else:
                balls[key] = []
    if ball_tmp2:
        for tmp in ball_tmp2:
            balls[(tmp[0], tmp[1])].append([tmp[2], tmp[3], tmp[4]])
res = 0
for key in balls:
    for ball in balls[key]:
        res += ball[0]
print(res)






