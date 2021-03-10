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
from collections import deque

def bfs(taxi, F):
    visited = [[-1]*N for _ in range(N)]
    queue = deque()
    waiting_list = []
    queue.append(taxi)
    visited[taxi[0]][taxi[1]] = 0

    if arr[taxi[0]][taxi[1]] == 2:
        waiting_list.append([taxi[0],taxi[1], 0])

    trg_tmp = False
    while queue:
        t1, t2 = queue.popleft()
        for c in range(4):
            x = t1 + dx[c]
            y = t2 + dy[c]
            if 0 <= x < N and 0 <= y < N and visited[x][y] == -1 and arr[x][y] != 1:
                queue.append([x,y])
                visited[x][y] = visited[t1][t2] + 1
                if arr[x][y] == 2:
                    waiting_list.append([x,y,visited[x][y]])
    if waiting_list:
        waiting_list.sort(key=lambda x:(x[2],x[0],x[1]))
        p1, p2, distance = waiting_list[0]
        if distance < F:
            trg_tmp = True
            arr[p1][p2] = 0
            F -= distance
            taxi = [p1, p2]
    return trg_tmp, taxi, F


def taking_passenger(taxi, F):
    visited = [[-1]*N for _ in range(N)]
    queue = deque()
    queue.append(taxi)
    visited[taxi[0]][taxi[1]] = 0
    trg_tmp = False
    for i in range(M):
        if passengers[i][0] == taxi[0] and passengers[i][1] == taxi[1]:
            destination = [passengers[i][2], passengers[i][3]]
            break

    while queue:
        s_i, s_j = queue.popleft()
        if s_i == destination[0] and s_j == destination[1]:
            if (F - visited[s_i][s_j]) >= 0:
                trg_tmp = True
                F = F - visited[s_i][s_j] + (2*visited[s_i][s_j])
                taxi = [s_i, s_j]
                break
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < N and visited[x][y] == -1 and arr[x][y] != 1:
                queue.append([x, y])
                visited[x][y] = visited[s_i][s_j] + 1
    return trg_tmp, taxi, F




N, M, F = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
passengers = []
t1, t2 = map(int,input().split())
# 위치, 연료
taxi = [t1-1, t2-1]
fuel = F
cnt =  0
for _ in range(M):
    p1,p2,d1,d2 = map(int, input().split())
    arr[p1-1][p2-1] = 2
    passengers.append([p1-1, p2-1, d1-1, d2-1])

dx = [0,-1,0,1]
dy = [-1,0,1,0]
res = 0

while True:
    trg1, taxi, F = bfs(taxi, F)
    if trg1:
        trg2, taxi, F = taking_passenger(taxi, F)
        if not trg2:
            res = -1
            break
        else:
            cnt += 1
            if cnt == M:
                res = F
                break
    else:
        res = -1
        break

print(res)