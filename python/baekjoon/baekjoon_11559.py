# baekjoon_11559 Puyo Puyo

# v1
# from collections import deque
#
# def bfs(i,j):
#     queue = deque()
#     color = arr[i][j]
#
#     queue.append([i,j])
#     visited[i][j] = 1
#     puyo_nums = 1
#     puyo_deleted = [[i,j]]
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if visited[x][y] == 0 and arr[x][y] == color:
#                     queue.append([x, y])
#                     visited[x][y] = 1
#                     puyo_deleted.append([x,y])
#                     puyo_nums += 1
#
#     if puyo_nums >= 4:
#         for p_i, p_j in puyo_deleted:
#             arr[p_i][p_j] = '.'
#         return True
#     else:
#         return False
#
# def falling_puyo():
#     for i in range(N-2, -1, -1):
#         for j in range(M):
#             if arr[i][j] != '.':
#                 x = i
#                 y = j
#                 while True:
#                     x += 1
#                     if 0 <= x < N:
#                         if arr[x][y] != '.':
#                             arr[x - 1][y] = arr[i][j]
#                             arr[i][j] = '.'
#                             break
#                     else:
#                         break
#
#
# N, M = 12, 6
# arr = [list(input()) for _ in range(N)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# trg1 = True
# res = 0
#
# while True:
#     if not trg1:
#         break
#
#     trg2 = False
#     visited = [[0]*M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if visited[i][j] == 0 and arr[i][j] != ".":
#                 if bfs(i,j):
#                     res += 1
#                     trg2 = True
#     falling_puyo()
#     print(arr)
#     if not trg2:
#         trg1 = False
# print(res)


# v2
# from collections import deque
#
# def bfs(i,j):
#     queue = deque()
#     color = arr[i][j]
#
#     queue.append([i,j])
#     visited[i][j] = 1
#     puyo_nums = 1
#     puyo_deleted = [[i,j]]
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if visited[x][y] == 0 and arr[x][y] == color:
#                     queue.append([x, y])
#                     visited[x][y] = 1
#                     puyo_deleted.append([x,y])
#                     puyo_nums += 1
#
#     if puyo_nums >= 4:
#         for p_i, p_j in puyo_deleted:
#             arr[p_i][p_j] = '.'
#         return True
#     else:
#         return False
#
#
#
#
# def falling_puyo():
#     for i in range(N-2, -1, -1):
#         for j in range(M):
#             if arr[i][j] != '.' and arr[i+1][j] == '.':
#                 x = i
#                 y = j
#                 while True:
#                     x += 1
#                     if 0 <= x < N:
#                         # if arr[x][y] == '.':
#                         #     continue
#                         if arr[x][y] != '.':
#                             arr[x - 1][y] = arr[i][j]
#                             arr[i][j] = '.'
#                             break
#                     else:
#                         arr[x-1][y] = arr[i][j]
#                         arr[i][j] = '.'
#                         break
#
#
# N, M = 12, 6
# arr = [list(input()) for _ in range(N)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# trg1 = True
# res = 0
#
# while True:
#     if not trg1:
#         break
#
#     trg2 = False
#     visited = [[0]*M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if visited[i][j] == 0 and arr[i][j] != ".":
#                 if bfs(i,j):
#                     res += 1
#                     trg2 = True
#     falling_puyo()
#     if not trg2:
#         trg1 = False
# print(res)

# v3
from collections import deque

def bfs(i,j):
    queue = deque()
    color = arr[i][j]

    queue.append([i,j])
    visited[i][j] = 1
    puyo_nums = 1
    puyo_deleted = [[i,j]]

    while queue:
        s_i, s_j = queue.popleft()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if visited[x][y] == 0 and arr[x][y] == color:
                    queue.append([x, y])
                    visited[x][y] = 1
                    puyo_deleted.append([x,y])
                    puyo_nums += 1

    if puyo_nums >= 4:
        for p_i, p_j in puyo_deleted:
            arr[p_i][p_j] = '.'
        return True
    else:
        return False




def falling_puyo():
    for i in range(N-2, -1, -1):
        for j in range(M):
            if arr[i][j] != '.' and arr[i+1][j] == '.':
                x = i
                y = j
                while True:
                    x += 1
                    if 0 <= x < N:
                        # if arr[x][y] == '.':
                        #     continue
                        if arr[x][y] != '.':
                            arr[x - 1][y] = arr[i][j]
                            arr[i][j] = '.'
                            break
                    else:
                        arr[x-1][y] = arr[i][j]
                        arr[i][j] = '.'
                        break


N, M = 12, 6
arr = [list(input()) for _ in range(N)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

trg1 = True
res = 0

while True:
    if not trg1:
        break

    trg2 = False
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] != ".":
                if bfs(i,j):
                    trg2 = True
    falling_puyo()
    if not trg2:
        trg1 = False
    else:
        res +=1
print(res)

