#baekjoon_17070 파이프 옮기기1

# v1
# def moving_row(pipe):
#     p1, p2, direction = pipe
#     x2 = p2[0] + row[0]
#     y2 = p2[1] + row[1]
#     if 0 <= x2 < N and 0 <= y2 < N and house[x2][y2] != 1:
#         x1 = p1[0] + row[0]
#         y1 = p1[1] + row[1]
#         pipe_tmp = [[x1,y1],[x2,y2],0]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_column(pipe):
#     p1, p2, direction = pipe
#     x2 = p2[0] + column[0]
#     y2 = p2[1] + column[1]
#     if 0 <= x2 < N and 0 <= y2 < N and house[x2][y2] != 1:
#         x1 = p1[0] + column[0]
#         y1 = p1[1] + column[1]
#         pipe_tmp = [[x1, y1], [x2, y2], 1]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_diagonal(pipe):
#     p1, p2, direction = pipe
#
#     for i in range(1, 4):
#         x2 = p2[0] + diagonal[i][0]
#         y2 = p2[1] + diagonal[i][1]
#         if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N or house[x2][y2] == 1:
#             return False, pipe
#     x1 = p1[0] + diagonal[0][0]
#     y1 = p1[1] + diagonal[0][1]
#     # x2 = p2[0] + diagonal[3][0]
#     # y2 = p2[1] + diagonal[3][1]
#     pipe_tmp = [[x1,y1],[x2,y2],2]
#     return True, pipe_tmp
#
#
# def dfs(pipe):
#     global res
#     curr1, curr2, direction = pipe
#     if curr2[0] == N-1 and curr2[1] == N-1:
#         res += 1
#         return
#     if direction == 0:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             dfs(new_pipe)
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             dfs(new_pipe)
#     elif direction == 1:
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             dfs(new_pipe)
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             dfs(new_pipe)
#     else:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             dfs(new_pipe)
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             dfs(new_pipe)
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             dfs(new_pipe)
#
#
#
# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
#
# # 현재 위치, 상태, 0 가로, 1 세로, 2 대각선.
# pipe = [[0,0],[0,1],0]
# res = 0
#
# # 가로 (x,y),시작점, 끝점, 끝점을 기준으로 체크.
# row = [0,1]
# # 세로
# column = [1,0]
# # 대각선, 2열부터 체크만,
# diagonal = [[0,1],[0,1],[1,0],[1,1]]
#
# dfs(pipe)
#
# print(res)




# v2
# def moving_row(pipe):
#     p1, p2, direction = pipe
#     x2 = p2[0] + row[0]
#     y2 = p2[1] + row[1]
#     if 0 <= x2 < N and 0 <= y2 < N and house[x2][y2] != 1:
#         x1 = p1[0] + row[0]
#         y1 = p1[1] + row[1]
#         pipe_tmp = [[x1,y1],[x2,y2],0]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_column(pipe):
#     p1, p2, direction = pipe
#     x2 = p2[0] + column[0]
#     y2 = p2[1] + column[1]
#     if 0 <= x2 < N and 0 <= y2 < N and house[x2][y2] != 1:
#         x1 = p1[0] + column[0]
#         y1 = p1[1] + column[1]
#         pipe_tmp = [[x1, y1], [x2, y2], 1]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_diagonal(pipe):
#     p1, p2, direction = pipe
#
#     for i in range(1, 4):
#         x2 = p2[0] + diagonal[i][0]
#         y2 = p2[1] + diagonal[i][1]
#         if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N or house[x2][y2] == 1:
#             return False, pipe
#     x1 = p1[0] + diagonal[0][0]
#     y1 = p1[1] + diagonal[0][1]
#     # x2 = p2[0] + diagonal[3][0]
#     # y2 = p2[1] + diagonal[3][1]
#     pipe_tmp = [[x1,y1],[x2,y2],2]
#     return True, pipe_tmp
#
#
# def dfs(pipe):
#     global res
#     curr1, curr2, direction = pipe
#     if house[curr2[0]][curr2[1]] == 2:
#         res += 1
#         return True
#     if curr2[0] == N - 1 and curr2[1] == N - 1:
#         res += 1
#         return True
#
#     if direction == 0:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#     elif direction == 1:
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#     else:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#
#
#
# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
#
# # 현재 위치, 상태, 0 가로, 1 세로, 2 대각선.
# pipe = [[0,0],[0,1],0]
# res = 0
#
# # 가로 (x,y),시작점, 끝점, 끝점을 기준으로 체크.
# row = [0,1]
# # 세로
# column = [1,0]
# # 대각선, 2열부터 체크만,
# diagonal = [[0,1],[0,1],[1,0],[1,1]]
#
# dfs(pipe)
#
# print(res)


# v3
# def moving_row(pipe):
#     p1, p2, direction = pipe
#     x2 = p2[0] + row[0]
#     y2 = p2[1] + row[1]
#     if 0 <= x2 < N and 0 <= y2 < N and house[x2][y2] != 1:
#         x1 = p1[0] + row[0]
#         y1 = p1[1] + row[1]
#         pipe_tmp = [[x1,y1],[x2,y2],0]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_column(pipe):
#     p1, p2, direction = pipe
#     x2 = p2[0] + column[0]
#     y2 = p2[1] + column[1]
#     if 0 <= x2 < N and 0 <= y2 < N and house[x2][y2] != 1:
#         x1 = p1[0] + column[0]
#         y1 = p1[1] + column[1]
#         pipe_tmp = [[x1, y1], [x2, y2], 1]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_diagonal(pipe):
#     p1, p2, direction = pipe
#
#     for i in range(1, 4):
#         x2 = p2[0] + diagonal[i][0]
#         y2 = p2[1] + diagonal[i][1]
#         if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N or house[x2][y2] == 1:
#             return False, pipe
#     x1 = p1[0] + diagonal[0][0]
#     y1 = p1[1] + diagonal[0][1]
#     # x2 = p2[0] + diagonal[3][0]
#     # y2 = p2[1] + diagonal[3][1]
#     pipe_tmp = [[x1,y1],[x2,y2],2]
#     return True, pipe_tmp
#
#
# def dfs(pipe):
#     global res
#     curr1, curr2, direction = pipe
#     if curr2[0] == N - 1 and curr2[1] == N - 1:
#         res += 1
#         return True
#     if house[curr2[0]][curr2[1]] == 2:
#         res += 1
#         return True
#     # if house[curr2[0]][curr2[1]] == 2 and direction == 2:
#     #     res +=
#     #     return True
#     if direction == 2:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] = 2
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#
#     if direction == 0:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#
#     if direction == 1:
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             if dfs(new_pipe):
#                 house[new_pipe[0][0]][new_pipe[0][1]] =2
#
#
#
#
# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
#
# # 현재 위치, 상태, 0 가로, 1 세로, 2 대각선.
# pipe = [[0,0],[0,1],0]
# res = 0
#
# # 가로 (x,y),시작점, 끝점, 끝점을 기준으로 체크.
# row = [0,1]
# # 세로
# column = [1,0]
# # 대각선, 2열부터 체크만,
# diagonal = [[0,1],[0,1],[1,0],[1,1]]
#
# dfs(pipe)
#
# print(res)



# v4
# def moving_row(pipe):
#     p1, direction = pipe
#     y2 = p1[1] + 1
#     if 0 <= p1[0] < N and 0 <= y2 < N and house[p1[0]][y2] != 1:
#         pipe_tmp = [[p1[0],y2],0]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_column(pipe):
#     p1, direction = pipe
#     x2 = p1[0] + 1
#     if 0 <= x2 < N and 0 <= p1[1] < N and house[x2][p1[1]] != 1:
#         pipe_tmp = [[x2, p1[1]], 1]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_diagonal(pipe):
#     p1, direction = pipe
#     for i in range(3):
#         x2 = p1[0] + diagonal[i][0]
#         y2 = p1[1] + diagonal[i][1]
#         if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N or house[x2][y2] == 1:
#             return False, pipe
#     pipe_tmp = [[x2,y2],2]
#     return True, pipe_tmp
#
#
# def dfs(pipe):
#     global res
#     curr, direction = pipe
#     if curr[0] == N-1 and curr[1] == N-1:
#         res += 1
#         return
#     if direction == 0:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             dfs(new_pipe)
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             dfs(new_pipe)
#     elif direction == 1:
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             dfs(new_pipe)
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             dfs(new_pipe)
#     else:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             dfs(new_pipe)
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             dfs(new_pipe)
#         trg, new_pipe = moving_diagonal(pipe)
#         if trg:
#             dfs(new_pipe)
#


#
#
# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
#
# # 현재 위치, 상태, 0 가로, 1 세로, 2 대각선.
# pipe = [[0,1],0]
# res = 0
# # 가로 (x,y),시작점, 끝점, 끝점을 기준으로 체크.
# row = [0,1]
# # 세로
# column = [1,0]
# # 대각선, 2열부터 체크만,
# diagonal = [[0,1],[1,0],[1,1]]
#
# dfs(pipe)
#
# print(res)

# v5
# def moving_row(pipe):
#     p1, direction = pipe
#     y2 = p1[1] + 1
#     if 0 <= p1[0] < N and 0 <= y2 < N and house[p1[0]][y2] != 1:
#         pipe_tmp = [[p1[0],y2],0]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_column(pipe):
#     p1, direction = pipe
#     x2 = p1[0] + 1
#     if 0 <= x2 < N and 0 <= p1[1] < N and house[x2][p1[1]] != 1:
#         pipe_tmp = [[x2, p1[1]], 1]
#         return True, pipe_tmp
#     return False, pipe
#
# def moving_diagonal(pipe):
#     p1, direction = pipe
#     for i in range(3):
#         x2 = p1[0] + diagonal[i][0]
#         y2 = p1[1] + diagonal[i][1]
#         if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N or house[x2][y2] == 1:
#             return False, pipe
#     pipe_tmp = [[x2,y2],2]
#     return True, pipe_tmp
#
#
# def dfs(pipe):
#     global res
#     curr, direction = pipe
#     if curr[0] == N-1 and curr[1] == N-1:
#         res += 1
#         return
#
#     if direction == 0 or direction == 2:
#         trg, new_pipe = moving_row(pipe)
#         if trg:
#             dfs(new_pipe)
#     if direction == 1 or direction == 2:
#         trg, new_pipe = moving_column(pipe)
#         if trg:
#             dfs(new_pipe)
#
#     trg, new_pipe = moving_diagonal(pipe)
#     if trg:
#         dfs(new_pipe)
#
#
#
# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
#
# # 현재 위치, 상태, 0 가로, 1 세로, 2 대각선.
# pipe = [[0,1],0]
# res = 0
# # 대각선
# diagonal = [[0,1],[1,0],[1,1]]
#
# dfs(pipe)
# print(res)

# v6

def dfs(i,j,k):
    global res
    if i == N-1 and j == N-1:
        res += 1
        return

    if k == 0 or k == 2:
        y = j + 1
        if 0 <= i < N and 0 <= y < N and house[i][y] != 1:
            dfs(i,y,0)
    if k == 1 or k == 2:
        x = i + 1
        if 0 <= x < N and 0 <= j < N and house[x][j] != 1:
            dfs(x,j,1)
    # 대각선
    x = i + 1
    y = j + 1
    if 0 <= x < N and 0 <= y < N:
        if house[i][j+1] == 0 and house[i+1][j] == 0 and house[x][y]==0:
            dfs(x, y, 2)


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
# 가로 0, 세로 1, 대각선 2

res = 0
dfs(0,1,0)
print(res)