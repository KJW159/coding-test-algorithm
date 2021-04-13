# baekjoon_19238 스타트 택시

# v1
# from collections import deque
#
# def bfs(taxi, F):
#     visited = [[-1]*N for _ in range(N)]
#     queue = deque()
#     waiting_list = []
#     queue.append(taxi)
#     visited[taxi[0]][taxi[1]] = 0
#     trg_tmp = False
#     while queue:
#         t1, t2 = queue.popleft()
#         for c in range(4):
#             x = t1 + dx[c]
#             y = t2 + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == -1 and arr[x][y] != 1:
#                 queue.append([x,y])
#                 visited[x][y] = visited[t1][t2] + 1
#                 if arr[x][y] == 2:
#                     waiting_list.append([x,y,visited[x][y]])
#     if waiting_list:
#         waiting_list.sort(key=lambda x:(x[2],x[0],x[1]))
#         p1, p2, distance = waiting_list[0]
#         if distance < F:
#             trg_tmp = True
#             arr[p1][p2] = 0
#             F -= distance
#             taxi = [p1, p2]
#     return trg_tmp, taxi, F
#
#
# def taking_passenger(taxi, F):
#     visited = [[-1]*N for _ in range(N)]
#     queue = deque()
#     queue.append(taxi)
#     visited[taxi[0]][taxi[1]] = 0
#     trg_tmp = False
#     for i in range(M):
#         if passengers[i][0] == taxi[0] and passengers[i][1] == taxi[1]:
#             destination = [passengers[i][2], passengers[i][3]]
#             break
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         if s_i == destination[0] and s_j == destination[1]:
#             if (F - visited[s_i][s_j]) >= 0:
#                 trg_tmp = True
#                 F = F - visited[s_i][s_j] + (2*visited[s_i][s_j])
#                 taxi = [s_i, s_j]
#                 break
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == -1 and arr[x][y] != 1:
#                 queue.append([x, y])
#                 visited[x][y] = visited[s_i][s_j] + 1
#     return trg_tmp, taxi, F
#
#
#
#
# N, M, F = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# passengers = []
# t1, t2 = map(int,input().split())
# # 위치, 연료
# taxi = [t1-1, t2-1]
# fuel = F
# cnt =  0
# for _ in range(M):
#     p1,p2,d1,d2 = map(int, input().split())
#     arr[p1-1][p2-1] = 2
#     passengers.append([p1-1, p2-1, d1-1, d2-1])
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = 0
#
# while True:
#     trg1, taxi, F = bfs(taxi, F)
#     if trg1:
#         trg2, taxi, F = taking_passenger(taxi, F)
#         if not trg2:
#             res = -1
#             break
#         else:
#             cnt += 1
#             if cnt == M:
#                 res = F
#                 break
#     else:
#         res = -1
#         break
#
# print(res)


# v2
# from collections import deque
#
# def bfs(taxi, F):
#     visited = [[-1]*N for _ in range(N)]
#     queue = deque()
#     waiting_list = []
#     queue.append(taxi)
#     visited[taxi[0]][taxi[1]] = 0
#
#     if arr[taxi[0]][taxi[1]] == 2:
#         waiting_list.append([taxi[0],taxi[1], 0])
#
#     trg_tmp = False
#     while queue:
#         t1, t2 = queue.popleft()
#         for c in range(4):
#             x = t1 + dx[c]
#             y = t2 + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == -1 and arr[x][y] != 1:
#                 queue.append([x,y])
#                 visited[x][y] = visited[t1][t2] + 1
#                 if arr[x][y] == 2:
#                     waiting_list.append([x,y,visited[x][y]])
#     if waiting_list:
#         waiting_list.sort(key=lambda x:(x[2],x[0],x[1]))
#         p1, p2, distance = waiting_list[0]
#         if distance < F:
#             trg_tmp = True
#             arr[p1][p2] = 0
#             F -= distance
#             taxi = [p1, p2]
#     return trg_tmp, taxi, F
#
#
# def taking_passenger(taxi, F):
#     visited = [[-1]*N for _ in range(N)]
#     queue = deque()
#     queue.append(taxi)
#     visited[taxi[0]][taxi[1]] = 0
#     trg_tmp = False
#     for i in range(M):
#         if passengers[i][0] == taxi[0] and passengers[i][1] == taxi[1]:
#             destination = [passengers[i][2], passengers[i][3]]
#             break
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         if s_i == destination[0] and s_j == destination[1]:
#             if (F - visited[s_i][s_j]) >= 0:
#                 trg_tmp = True
#                 F = F - visited[s_i][s_j] + (2*visited[s_i][s_j])
#                 taxi = [s_i, s_j]
#                 break
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < N and visited[x][y] == -1 and arr[x][y] != 1:
#                 queue.append([x, y])
#                 visited[x][y] = visited[s_i][s_j] + 1
#     return trg_tmp, taxi, F
#
#
#
#
# N, M, F = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# passengers = []
# t1, t2 = map(int,input().split())
# # 위치, 연료
# taxi = [t1-1, t2-1]
# fuel = F
# cnt =  0
# for _ in range(M):
#     p1,p2,d1,d2 = map(int, input().split())
#     arr[p1-1][p2-1] = 2
#     passengers.append([p1-1, p2-1, d1-1, d2-1])
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = 0
#
# while True:
#     trg1, taxi, F = bfs(taxi, F)
#     if trg1:
#         trg2, taxi, F = taking_passenger(taxi, F)
#         if not trg2:
#             res = -1
#             break
#         else:
#             cnt += 1
#             if cnt == M:
#                 res = F
#                 break
#     else:
#         res = -1
#         break
#
# print(res)

# re-v1
# from collections import defaultdict, deque
#
# def taking_people():
#     queue = deque()
#     queue.append(taxi)
#
#     visited = [[-1]*N for _ in range(N)]
#     visited[taxi[0]][taxi[1]] = 0
#     people_tmp = []
#     if city[taxi[0]][taxi[1]] == 2:
#         people_tmp.append([taxi[0],taxi[1],0])
#
#     while queue:
#         t_i, t_j = queue.popleft()
#         for c in range(4):
#             x = t_i + dx[c]
#             y = t_j + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if city[x][y] == 0 and visited[x][y] == -1:
#                     queue.append([x,y])
#                     visited[x][y] = visited[t_i][t_j] + 1
#                 if city[x][y] == 2 and visited[x][y] == -1:
#                     queue.append([x,y])
#                     visited[x][y] = visited[t_i][t_j] + 1
#                     people_tmp.append([x,y,visited[x][y]])
#     if people_tmp:
#         people_tmp.sort(key=lambda x:(x[2],x[0],x[1]))
#         return people_tmp[0]
#     else:
#         return [0,0,-1]
#
# def going_destination(s_i, s_j, fuel):
#     e_i, e_j = people[s_i,s_j]
#     queue = deque()
#     queue.append([s_i, s_j])
#
#     visited = [[-1]*N for _ in range(N)]
#     visited[s_i][s_j] = 0
#     distance_tmp = 0
#     while queue:
#         s_x, s_y = queue.popleft()
#         if s_x == e_i and s_y == e_j:
#             distance_tmp = visited[s_x][s_y]
#             break
#         for c in range(4):
#             x = s_x + dx[c]
#             y = s_y + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if city[x][y] != 1 and visited[x][y] == -1:
#                     queue.append([x,y])
#                     visited[x][y] = visited[s_x][s_y]+1
#
#     if (fuel-distance_tmp) >= 0:
#         return 1, distance_tmp, e_i, e_j
#     else:
#         return 0, 0, e_i, e_j
#
#
# N, M, fuel = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
# t1,t2 = list(map(int, input().split()))
# taxi = [t1-1,t2-1]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# people = defaultdict(list)
# people_num = M
# for _ in range(M):
#     s_i, s_j, e_i, e_j = map(int, input().split())
#     people[s_i-1,s_j-1] = [e_i-1, e_j-1]
#     city[s_i-1][s_j-1] = 2
# for m in range(M):
#     p_x, p_y, distance = taking_people()
#     if distance != -1:
#         fuel -= distance
#         city[p_x][p_y] = 0
#         taxi = [p_x, p_y]
#     else:
#         break
#     if fuel > 0:
#         trg, distance, e_i, e_j = going_destination(p_x, p_y, fuel)
#         if trg == 1:
#             fuel -= distance
#             fuel += (distance*2)
#             people_num -= 1
#             taxi = [e_i, e_j]
#             city[e_i][e_j] = 0
#         else:
#             break
#
# if people_num != 0:
#     print(-1)
# else:
#     print(fuel)


# re-v2
# from collections import defaultdict, deque
#
# def taking_people():
#     queue = deque()
#     queue.append(taxi)
#
#     visited = [[-1]*N for _ in range(N)]
#     visited[taxi[0]][taxi[1]] = 0
#     people_tmp = []
#     if city[taxi[0]][taxi[1]] == 2:
#         people_tmp.append([taxi[0],taxi[1],0])
#
#     while queue:
#         t_i, t_j = queue.popleft()
#         for c in range(4):
#             x = t_i + dx[c]
#             y = t_j + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if city[x][y] == 0 and visited[x][y] == -1:
#                     queue.append([x,y])
#                     visited[x][y] = visited[t_i][t_j] + 1
#                 if city[x][y] == 2 and visited[x][y] == -1:
#                     queue.append([x,y])
#                     visited[x][y] = visited[t_i][t_j] + 1
#                     people_tmp.append([x,y,visited[x][y]])
#     if people_tmp:
#         people_tmp.sort(key=lambda x:(x[2],x[0],x[1]))
#         return people_tmp[0]
#     else:
#         return [0,0,-1]
#
# def going_destination(s_i, s_j, fuel):
#     e_i, e_j = people[s_i,s_j]
#     queue = deque()
#     queue.append([s_i, s_j])
#
#     visited = [[-1]*N for _ in range(N)]
#     visited[s_i][s_j] = 0
#     distance_tmp = 0
#     trg = False
#     while queue:
#         s_x, s_y = queue.popleft()
#         if s_x == e_i and s_y == e_j:
#             distance_tmp = visited[s_x][s_y]
#             trg = True
#             break
#         for c in range(4):
#             x = s_x + dx[c]
#             y = s_y + dy[c]
#             if 0 <= x < N and 0 <= y < N:
#                 if city[x][y] != 1 and visited[x][y] == -1:
#                     queue.append([x,y])
#                     visited[x][y] = visited[s_x][s_y]+1
#     if (fuel-distance_tmp) >= 0 and trg:
#         return 1, distance_tmp, e_i, e_j
#     else:
#         return 0, 0, e_i, e_j
#
#
# N, M, fuel = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
# t1,t2 = list(map(int, input().split()))
# taxi = [t1-1,t2-1]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# people = defaultdict(list)
# people_num = M
# for _ in range(M):
#     s_i, s_j, e_i, e_j = map(int, input().split())
#     people[s_i-1,s_j-1] = [e_i-1, e_j-1]
#     city[s_i-1][s_j-1] = 2
# for m in range(M):
#     p_x, p_y, distance = taking_people()
#     if distance != -1:
#         fuel -= distance
#         city[p_x][p_y] = 0
#         taxi = [p_x, p_y]
#     else:
#         break
#     if fuel > 0:
#         trg, distance, e_i, e_j = going_destination(p_x, p_y, fuel)
#         if trg == 1:
#             fuel -= distance
#             fuel += (distance*2)
#             people_num -= 1
#             taxi = [e_i, e_j]
#         else:
#             break
#
# if people_num != 0:
#     print(-1)
# else:
#     print(fuel)


# re-v3
from collections import defaultdict, deque

def taking_people():
    queue = deque()
    queue.append(taxi)

    visited = [[-1]*N for _ in range(N)]
    visited[taxi[0]][taxi[1]] = 0
    people_tmp = []
    if city[taxi[0]][taxi[1]] == 2:
        people_tmp.append([taxi[0],taxi[1],0])

    while queue:
        t_i, t_j = queue.popleft()
        for c in range(4):
            x = t_i + dx[c]
            y = t_j + dy[c]
            if 0 <= x < N and 0 <= y < N:
                if city[x][y] == 0 and visited[x][y] == -1:
                    queue.append([x,y])
                    visited[x][y] = visited[t_i][t_j] + 1
                if city[x][y] == 2 and visited[x][y] == -1:
                    queue.append([x,y])
                    visited[x][y] = visited[t_i][t_j] + 1
                    people_tmp.append([x,y,visited[x][y]])
    if people_tmp:
        people_tmp.sort(key=lambda x:(x[2],x[0],x[1]))
        return people_tmp[0]
    else:
        return [0,0,-1]

def going_destination(s_i, s_j, fuel):
    e_i, e_j = people[s_i,s_j]
    queue = deque()
    queue.append([s_i, s_j])

    visited = [[-1]*N for _ in range(N)]
    visited[s_i][s_j] = 0
    distance_tmp = 0
    trg = False
    while queue:
        s_x, s_y = queue.popleft()
        if s_x == e_i and s_y == e_j:
            distance_tmp = visited[s_x][s_y]
            trg = True
            break
        for c in range(4):
            x = s_x + dx[c]
            y = s_y + dy[c]
            if 0 <= x < N and 0 <= y < N:
                if city[x][y] != 1 and visited[x][y] == -1:
                    queue.append([x,y])
                    visited[x][y] = visited[s_x][s_y]+1
    if (fuel-distance_tmp) >= 0 and trg:
        return 1, distance_tmp, e_i, e_j
    else:
        return 0, 0, e_i, e_j


N, M, fuel = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
t1,t2 = list(map(int, input().split()))
taxi = [t1-1,t2-1]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

people = defaultdict(list)
people_num = M
for _ in range(M):
    s_i, s_j, e_i, e_j = map(int, input().split())
    people[s_i-1,s_j-1] = [e_i-1, e_j-1]
    city[s_i-1][s_j-1] = 2
for m in range(M):
    p_x, p_y, distance = taking_people()
    if distance != -1:
        fuel -= distance
        city[p_x][p_y] = 0
        taxi = [p_x, p_y]
    else:
        break
    if fuel > 0:
        trg, distance2, e_i, e_j = going_destination(p_x, p_y, fuel)
        if trg == 1:
            fuel -= distance2
            fuel += (distance2*2)
            people_num -= 1
            taxi = [e_i, e_j]
        else:
            break

if people_num != 0:
    print(-1)
else:
    print(fuel)
