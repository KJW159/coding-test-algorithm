# baekjoon_17135 캐슬 디펜스
# # v1
# from collections import deque
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r== 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
#
# def kill(archers, arr_copy, M,N):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#     queue = deque()
#
#     for n in range(len(N)):
#         queue.append(archers)
#         archer1, archer2, archer3 = archers
#         visited = [[[0] * M for _ in range(N)] for __ in range(3)]
#         visited[archer1[0]][archer1[1]] = 1
#         visited[archer2[0]][archer2[1]] = 1
#         visited[archer3[0]][archer3[1]] = 1
#
#         while queue:
#             archer1, archer2, archer3 = queue.popleft()
#             for c in range(4):
#                 x =
#
#
#
#
#
#
#
# N, M, D = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
#
#
# archers_position = [(N,i) for i in range(M)]
#
# for archers in combinations1(archers_position, 3):
#     arr_copy =[arr[k][:] for k in range(N)]
#     kill(archers, arr_copy,M,N)

# v2
# from itertools import combinations
#
# def killing_enemy(archer_position):
#     enemy_list = [[],[],[]]
#     enemy_killed = set()
#     cnt_tmp = 0
#     for k in range(3):
#         a_i, a_j = archer_position[k]
#         for i in range(N):
#             for j in range(M):
#                 if arr_tmp[i][j] == 1:
#                     distance = (abs(a_i - i)+abs(a_j - j))
#                     if distance <= D:
#                         enemy_list[k].append((i,j,distance))
#         if enemy_list[k]:
#             enemy_list[k].sort(key=lambda x: (x[2],x[1]))
#             enemy_killed.add((enemy_list[k][0][0],enemy_list[k][0][1]))
#     if enemy_killed:
#         cnt_tmp += len(enemy_killed)
#         for enemy in enemy_killed:
#             arr_tmp[enemy[0]][enemy[1]] = 0
#     return cnt_tmp
#
# def moving_enemy():
#     trg = False
#     for i in range(N-1,-1,-1):
#         for j in range(M):
#             if arr_tmp[i][j] == 1:
#                 trg = True
#                 past = i
#                 now = i + 1
#                 if now == N:
#                     arr_tmp[past][j] = 0
#                     continue
#                 arr_tmp[past][j] = 0
#                 arr_tmp[now][j] = 1
#     return trg
#
#
# N, M, D = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# archers = [[N, i] for i in range(M)]
# res = 0
# for archer_position in combinations(archers, 3):
#     arr_tmp = [arr[a][:] for a in range(N)]
#     cnt = 0
#     while True:
#         cnt += killing_enemy(archer_position)
#         trg = moving_enemy()
#         if not trg:
#             res = max(res, cnt)
#             break
# print(res)


# v3

def combinations1(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield[arr[i]]
        else:
            for next in combinations1(arr[i+1:], r-1):
                yield [arr[i]] + next


def killing_enemy(archer_position):
    enemy_list = [[],[],[]]
    enemy_killed = set()
    cnt_tmp = 0
    for k in range(3):
        a_i, a_j = archer_position[k]
        for i in range(N):
            for j in range(M):
                if arr_tmp[i][j] == 1:
                    distance = (abs(a_i - i)+abs(a_j - j))
                    if distance <= D:
                        enemy_list[k].append((i,j,distance))
        if enemy_list[k]:
            enemy_list[k].sort(key=lambda x: (x[2],x[1]))
            enemy_killed.add((enemy_list[k][0][0],enemy_list[k][0][1]))
    if enemy_killed:
        cnt_tmp += len(enemy_killed)
        for enemy in enemy_killed:
            arr_tmp[enemy[0]][enemy[1]] = 0
    return cnt_tmp

def moving_enemy():
    trg = False
    for i in range(N-1,-1,-1):
        for j in range(M):
            if arr_tmp[i][j] == 1:
                trg = True
                past = i
                now = i + 1
                if now == N:
                    arr_tmp[past][j] = 0
                    continue
                arr_tmp[past][j] = 0
                arr_tmp[now][j] = 1
    return trg


N, M, D = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

archers = [[N, i] for i in range(M)]
res = 0
for archer_position in combinations1(archers, 3):
    arr_tmp = [arr[a][:] for a in range(N)]
    cnt = 0
    while True:
        cnt += killing_enemy(archer_position)
        trg = moving_enemy()
        if not trg:
            res = max(res, cnt)
            break
print(res)